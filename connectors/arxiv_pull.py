import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from core.dtos import HarvesterPayloadDTO

def fetch_arxiv_results(keyword: str, max_results: int = 10) -> list[HarvesterPayloadDTO]:
    """
    Fetches articles from arXiv using the provided keyword and maps them to Sovereign DTOs.
    """
    base_url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": f"all:{keyword}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }
    
    response = requests.get(base_url, params=params, timeout=10)
    response.raise_for_status()
    
    return parse_arxiv_xml(response.text)

def parse_arxiv_xml(xml_content: str) -> list[HarvesterPayloadDTO]:
    dtos = []
    try:
        root = ET.fromstring(xml_content)
    except ET.ParseError:
        return dtos
        
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    
    for entry in root.findall('atom:entry', ns):
        title_el = entry.find('atom:title', ns)
        title = title_el.text.strip().replace('\n', ' ') if title_el is not None and title_el.text else "No Title"
        
        id_el = entry.find('atom:id', ns)
        source_url = id_el.text.strip() if id_el is not None and id_el.text else ""
        
        summary_el = entry.find('atom:summary', ns)
        content = summary_el.text.strip().replace('\n', ' ') if summary_el is not None and summary_el.text else ""
        
        published_el = entry.find('atom:published', ns)
        published_at = None
        if published_el is not None and published_el.text:
            try:
                time_str = published_el.text.strip()
                published_at = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")
            except ValueError:
                pass
                
        dto = HarvesterPayloadDTO(
            source_url=source_url,
            title=title,
            content=content,
            published_at=published_at,
            source_type="arxiv"
        )
        dtos.append(dto)
        
    return dtos
