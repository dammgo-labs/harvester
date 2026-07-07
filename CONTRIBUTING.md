# Contributing to Harvester

Thank you for your interest in contributing to **Harvester**! 
To maintain the integrity and longevity of this project, we strictly enforce the **dammgo labs V5 Architecture** rules.

## 🛠️ Adding a New Connector

Harvester is designed to be easily extensible. If you want to add support for a new data source (e.g., Reddit, HackerNews, X), you must build a new Connector inside the `connectors/` directory.

### Mandatory Rules for Connectors:

1. **Test-Driven Development (TDD):**
   You MUST write a `pytest` inside the `tests/` directory (e.g., `test_reddit_connector.py`) *before* writing the connector logic. Prove that it fails, then make it pass.
2. **The Sovereign DTO (Anti-Corruption Wall):**
   Your connector cannot return raw JSON dictionaries, API responses, or proprietary library objects. It must map the extracted data into a list of immutable `HarvesterPayloadDTO` objects (found in `core/dtos.py`). This isolates the Harvester Core from any changes in external APIs.
3. **Single Responsibility Principle:**
   Your connector's ONLY job is to fetch data and hydrate DTOs. Do not implement filtering logic, database calls, or file saving inside the connector.

### Example Connector Workflow:
1. Fetch data from `https://api.example.com`.
2. Iterate through the results.
3. Map each result to `HarvesterPayloadDTO(source_url, title, content, ...)`.
4. Return `List[HarvesterPayloadDTO]`.

## 🐛 Bug Reports & Fixes
Please ensure all tests (`pytest -v`) pass locally before submitting a patch.

---
**dammgo labs** - _Engineering Longevity. Signal over noise._
