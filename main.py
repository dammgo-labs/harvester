import argparse
import os
import sys
import requests
import time
from dotenv import load_dotenv

# Cargar credenciales seguras
load_dotenv()

# Asegurar que importamos los modulos desde el root
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.lens_parser import LensParser
from core.bouncer import Bouncer
from core.ledger import Ledger
from connectors.rss_pull import parse_rss_feed

def generate_markdown_drop(dto, lens, output_dir):
    date_str = time.strftime("%Y-%m-%d")
    # Generar un nombre seguro para Windows
    safe_title = "".join([c if c.isalnum() else "_" for c in dto.title[:30]])
    filename = f"{date_str}_Scout_{lens.config.get('project', 'Unknown')}_{safe_title}.md"
    filepath = os.path.join(output_dir, filename)
    
    content = f"""---
tipo: scout_report
lente_usado: {lens.config.get('project', 'Unknown')}
fecha_descubrimiento: {date_str}
---

# 💎 {dto.title}
**Fuente Original:** {dto.source_url}
**Nivel de Pureza:** Determinado por Harvester (Filtro Regex Aprobado)

## 🧠 Payload (Texto Crudo Filtrado)
{dto.content}

> *Nota: Este archivo fue generado automáticamente por Harvester. Listo para evaluación cognitiva por atlas-scout.*
"""
    os.makedirs(output_dir, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath

def main():
    parser = argparse.ArgumentParser(description="Harvester - Deterministic OSINT Pre-processor")
    parser.add_argument("--lens", required=True, help="Path to the SCOUT_LENS.json contract")
    args = parser.parse_args()

    print(f"[*] Initializing Harvester with Lens: {args.lens}")
    
    try:
        lens = LensParser(args.lens)
    except FileNotFoundError as e:
        print(f"[!] Error: {e}")
        return

    bouncer = Bouncer(lens.bullshit_filter, lens.deep_keywords)
    ledger_path = os.path.join(os.path.dirname(__file__), "ledger.db")
    ledger = Ledger(ledger_path)
    
    print(f"[*] Drop path resolved to: {lens.drop_path}")
    
    rss_sources = lens.target_sources.get("rss", [])
    
    if not rss_sources:
        print("[*] No RSS feeds defined in SCOUT_LENS.json. Exiting.")
        return

    gems_found = 0
    noise_dropped = 0
    duplicate_skipped = 0

    for feed_url in rss_sources:
        print(f"[*] Fetching RSS feed: {feed_url}")
        try:
            response = requests.get(feed_url, timeout=10)
            response.raise_for_status()
            dtos = parse_rss_feed(response.text)
        except Exception as e:
            print(f"[!] Failed to fetch {feed_url}: {e}")
            continue

        for dto in dtos:
            if ledger.is_processed(dto.source_url):
                duplicate_skipped += 1
                continue
            
            # Anotamos en el ledger sin importar si pasa o no.
            # No queremos volver a gastar CPU evaluando basura conocida.
            ledger.mark_processed(dto.source_url)
            
            # El Cadenero evalúa el DTO Soberano
            combined_text = f"{dto.title} {dto.content}"
            if bouncer.passes_filter(combined_text):
                print(f"[+] GEM FOUND: {dto.title}")
                generate_markdown_drop(dto, lens, lens.drop_path)
                gems_found += 1
            else:
                noise_dropped += 1

    print(f"[*] Harvester run complete.")
    print(f"    - Duplicados saltados: {duplicate_skipped}")
    print(f"    - Ruido destruido: {noise_dropped}")
    print(f"    - Joyas encontradas: {gems_found}")

if __name__ == "__main__":
    main()
