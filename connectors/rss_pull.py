import feedparser
from typing import List
from core.dtos import HarvesterPayloadDTO

def parse_rss_feed(raw_rss_content: str) -> List[HarvesterPayloadDTO]:
    """
    Toma un string crudo de XML/RSS, lo parsea usando feedparser,
    y devuelve una lista de Sovereign DTOs (Muro Anti-Corrupción).
    """
    feed = feedparser.parse(raw_rss_content)
    dtos = []
    
    for entry in feed.entries:
        title = entry.get('title', 'No Title')
        link = entry.get('link', '')
        # El contenido RSS suele venir en summary o description
        content = entry.get('summary', entry.get('description', ''))
        
        dto = HarvesterPayloadDTO(
            source_url=link,
            title=title,
            content=content,
            source_type="rss"
        )
        dtos.append(dto)
        
    return dtos
