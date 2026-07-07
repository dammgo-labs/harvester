# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.0.0] - 2026-07-07
### Added
- **Core Orchestrator (`main.py`)**: Hybrid deterministic CLI pipeline.
- **Bouncer (`core/bouncer.py`)**: High-performance Regex filtering engine with implicit `OR` bilingual support and `bullshit` keyword destruction.
- **Ledger (`core/ledger.py`)**: SQLite-based memory system to track and skip duplicate URLs automatically.
- **Sovereign DTOs (`core/dtos.py`)**: Immutable dataclasses establishing an anti-corruption layer between external APIs and the core domain.
- **Lens Parser (`core/lens_parser.py`)**: JSON parser for dynamic loading of OSINT rules (`SCOUT_LENS.json`) and data sources.
- **RSS Connector (`connectors/rss_pull.py`)**: TDD-compliant module for extracting XML/RSS feeds into Sovereign DTOs.
- **OpSec Protocol**: Built-in `python-dotenv` support with `.env.template` for secure API credential management.
- Comprehensive architectural documentation (`docs/architecture.md`) and authoring guides (`docs/lens_authoring.md`).

---
**dammgo labs** - _Engineering Longevity. Signal over noise._
