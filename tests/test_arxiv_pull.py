import pytest
from datetime import datetime
from connectors.arxiv_pull import parse_arxiv_xml

def test_parse_arxiv_xml():
    xml_data = """<?xml version="1.0" encoding="UTF-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
      <entry>
        <id>http://arxiv.org/abs/2101.00123v1</id>
        <updated>2021-01-01T00:00:00Z</updated>
        <published>2021-01-01T00:00:00Z</published>
        <title>Testing Quantum Computing</title>
        <summary>This is an abstract about quantum computing.</summary>
      </entry>
      <entry>
        <id>http://arxiv.org/abs/2101.00124v1</id>
        <updated>2021-01-02T00:00:00Z</updated>
        <published>2021-01-02T00:00:00Z</published>
        <title>Another Paper
        with newline</title>
        <summary>Summary with
        newline.</summary>
      </entry>
    </feed>
    """
    
    dtos = parse_arxiv_xml(xml_data)
    
    assert len(dtos) == 2
    assert dtos[0].title == "Testing Quantum Computing"
    assert dtos[0].source_url == "http://arxiv.org/abs/2101.00123v1"
    assert dtos[0].content == "This is an abstract about quantum computing."
    assert dtos[0].source_type == "arxiv"
    assert isinstance(dtos[0].published_at, datetime)
    assert dtos[0].published_at.year == 2021
    
    assert dtos[1].title == "Another Paper         with newline"
    assert dtos[1].content == "Summary with         newline."
