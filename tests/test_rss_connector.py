import pytest
from core.dtos import HarvesterPayloadDTO
from connectors.rss_pull import parse_rss_feed

def test_parse_rss_feed_returns_sovereign_dtos():
    """
    TDD: Validamos que el conector de RSS convierta exitosamente el texto crudo 
    (XML/RSS) en nuestro Sovereign DTO (HarvesterPayloadDTO).
    """
    dummy_rss = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
    <channel>
      <title>Dummy Physics Feed</title>
      <item>
        <title>Quantum Coherence in Microtubules</title>
        <link>http://example.com/paper/123</link>
        <description>This paper discusses phase coherence.</description>
      </item>
    </channel>
    </rss>
    """
    
    dtos = parse_rss_feed(dummy_rss)
    
    assert len(dtos) == 1
    assert isinstance(dtos[0], HarvesterPayloadDTO)
    assert dtos[0].title == "Quantum Coherence in Microtubules"
    assert dtos[0].source_url == "http://example.com/paper/123"
    assert "phase coherence" in dtos[0].content
    assert dtos[0].source_type == "rss"
