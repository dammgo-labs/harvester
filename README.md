# Harvester

> **Division:** Agentic Infrastructure
> **Status:** Alpha / Architectural Prototype

## 🌍 The Compute Obesity Problem

The current paradigm of Artificial Intelligence suffers from **compute obesity**. Sending LLM Agents to blindly crawl the open web wastes millions of tokens, computing cycles, dollars, and gallons of water in data centers, only for them to process SEO noise and marketing garbage.

At **dammgo labs**, we believe that true intelligence is knowing what *not* to read. 

## ⚙️ The Solution: Deterministic Pre-Processing

**Harvester** is a deterministic pre-processor designed for sustainable Agentic Workflows. It extracts, filters, and sterilizes text using strict mathematical and lexical contracts *before* passing any payload to the expensive cognitive layer (LLMs). 

By acting as a relentless gatekeeper, Harvester optimizes token expenditure by up to 90%, significantly reducing the ecological and economic footprint of our deep-tech research operations (such as *Coherence Infrastructure*).

## 🏗️ The Hybrid Pipeline Architecture

Harvester operates under a Hybrid Pipeline that separates cheap, deterministic extraction from expensive, non-deterministic cognition:

1. **Phase 1: The Harvester (Traditional Compute)**
   A lightweight, zero-token script running locally. It interfaces with primary sources (APIs, RSS feeds, specialized subreddits, academic hubs). It downloads raw text and immediately subjects it to a severe Regex/Lexical filter.
2. **Phase 2: The Filter (The Lens Contract)**
   Harvester reads a standardized JSON contract called `SCOUT_LENS.json`. If a scraped article contains any string defined in the `bullshit_filter` array (e.g., commercial buzzwords, pseudoscientific marketing), the article is instantly purged. 
3. **Phase 3: Cognitive Evaluation**
   Only the surgically filtered, highly technical raw text is dropped into a staging folder. A dedicated LLM Agent is then invoked to read only this pure payload, extracting the actual research gems without wasting a single token on noise.

## 📄 The `SCOUT_LENS.json` Standard

This repository champions the use of Lens Contracts as APIs for Agents. A standard Lens looks like this:

```json
{
  "project": "Research-Name",
  "deep_keywords": ["keyword A AND keyword B"],
  "bullshit_filter": ["marketing term", "seo trap", "clickbait"],
  "gem_criteria": ["Raw datasets", "Academic papers from 1990s"],
  "target_sources": {
    "rss": [
      "http://export.arxiv.org/rss/physics"
    ],
    "reddit": [
      "r/biohacking"
    ]
  }
}
```

## 🛡️ Core Engineering Pillars
Harvester strictly adheres to dammgo labs' internal architectural guidelines:
- **Sovereign DTOs (Anti-Corruption Wall):** Connectors (like RSS) never pass raw external API dictionaries into the core domain. They immediately hydrate an immutable `HarvesterPayloadDTO`. The core domain never speaks the language of external dependencies.
- **The Ledger (SQLite Memory):** To protect API rate limits and compute time, Harvester maintains a local SQLite database (`ledger.db`) of every URL ever processed. Known URLs are silently skipped before they even reach the Regex evaluation.
- **Implicit OR Bilingual Scanning:** The `deep_keywords` array evaluates as a massive `OR` block. This allows researchers to stack queries in multiple languages (e.g., English for arXiv, Spanish for niche forums) ensuring zero translation loss.

## 🔒 Configuration (OpSec)
Harvester relies on secure environment variables for API connectors. 
Copy the provided `.env.template` to `.env` and fill in your credentials. The `.env` file is strictly ignored by Git to protect institutional secrets.

## 🚀 Usage (CLI)

Because the `SCOUT_LENS.json` contract now embeds the `target_sources` natively, executing the orchestrator is remarkably clean:

```bash
python main.py --lens /path/to/SCOUT_LENS.json
```

## ⚖️ License

All code, pipelines, and architectural standards in this repository are published under the **Elastic License 2.0 (ELv2)**. 
You may not provide this software to third parties as a hosted or managed service without the express consent of dammgo labs.

---
**dammgo labs** - _Engineering Longevity. Signal over noise._
