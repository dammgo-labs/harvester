from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass(frozen=True)
class HarvesterPayloadDTO:
    """
    Sovereign DTO (Muro Anti-Corrupción).
    Este objeto inmutable es la única estructura de datos que el Core 
    (Bouncer/Ledger) aceptará de la capa de Infraestructura (Connectors).
    Aisla al Dominio de librerías externas (ej. feedparser, requests).
    """
    source_url: str
    title: str
    content: str
    published_at: Optional[datetime] = None
    source_type: str = "unknown"
