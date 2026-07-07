# 🔬 Lens Authoring Guide

A `SCOUT_LENS.json` is the "Mission Contract" for Harvester and the downstream AI agents. This guide explains how to write an effective Lens to maximize signal and obliterate noise.

## 1. The Anatomy of a Lens

```json
{
  "project": "Project-Name",
  "thesis": "The guiding philosophical principle for the AI.",
  "deep_keywords": [
    "\"Keyword A\" AND \"Keyword B\"",
    "\"Translation A\" AND \"Translation B\""
  ],
  "bullshit_filter": [
    "scam", "buy now"
  ],
  "gem_criteria": [
    "What makes a text a 'Gem' for the AI"
  ],
  "target_sources": {
    "rss": ["http://feed.com"],
    "reddit": ["r/niche"]
  }
}
```

## 2. The "Implicit OR" Trick (Bilingual Scanning)

The Harvester's Regex engine (`Bouncer`) evaluates the `deep_keywords` array as a massive **OR** block. This means you do not need to write complex boolean logic strings.

If you are researching "Quantum Collapse" but your sources are both English and Spanish, write your keywords on separate lines:

```json
  "deep_keywords": [
    "\"Heart Rate Variability\" AND \"quantum collapse\"",
    "\"Variabilidad de la Frecuencia Cardíaca\" AND \"colapso cuántico\""
  ]
```
*Rule of thumb:* If ANY line in the array matches the text, the document passes the filter.

## 3. The `bullshit_filter`
This is an absolute **Negative Filter**. If any word in this array is found anywhere in the text, the document is instantly destroyed. Use this to filter out commercial spam, SEO traps, and clickbait. Ensure you include translations here as well (e.g., `"buy now"`, `"compra ahora"`).

## 4. `thesis` and `gem_criteria` (For the AI)
These fields are ignored by Harvester's code. They are embedded into the final Markdown file so that the downstream LLM (`atlas-scout`) understands the philosophical context of what it is reading. You can write these entirely in your native language (e.g., Spanish) as the LLM is natively multilingual.

---
**dammgo labs** - _Engineering Longevity. Signal over noise._
