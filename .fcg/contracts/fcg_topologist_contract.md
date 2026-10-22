---
fcg_version: "1.0"
name: "fcg_topologist_contract"
version: "2.0.0"
archetype: "fcg_topologist"
omega_class: "𝒞 = R_always - tmpfs RO + EngineHSM verified + schemas RO + fcg_spawn_agent v2"
enforcement: "Φ_contract > Φ_archetype via OOB framing, Φ_lint > Φ_generation, Φ_engine > Φ_orchestrator via fcg_spawn_agent v2"
---

# Contract: fcg_topologist_01

> [!IMPORTANT] Φ_contract > Φ_archetype enforced by Engine via <contract enforcement="supreme">. Φ_engine > Φ_orchestrator enforced by fcg_spawn_agent v2 - generic invoke_subagent is FORBIDDEN for topologist spawn.

domain:
  context_anchor: "./" # CWD Axiom regex ^\./(?!.*\.\./).*$
  omega:
    R: ".fcg/routing.json + schemas/*.schema.json + templates/.fcg/ - tmpfs RO - provided by fcg_spawn_agent v2"
    C: ".fcg/contracts/ - tmpfs RO + verify_signature_content()"
    A: ".fcg/archetypes/ - Local Override -> Global $FCG_PATH/.fcg/archetypes - RO - resolved by Engine, not by LLM"
    K: ".fcg/knowledge/ - NO MOUNT, request via ℬ - FORBIDDEN as syntax source - README.md is non-normative"
    V: ".fcg/volatile/ - NO MOUNT"
    B: ".fcg/bus/cross_memory.log - append-only HMAC(expected_key+seq_num)"

axioms:
  - id: "FA-01-CWD"
    name: "CWD Axiom + NO MOUNT"
    trinity: { logic: "Only ./ allowed, .fcg/knowledge/, .fcg/volatile/ NO MOUNT. Context anchor ./ regex ^\./(?!.*\.\./).*$ - Prevents v_symlink LFI", enforcement: { mechanism: "seccomp-bpf + eBPF VFS + CWD regex - enforced by Antigravity Engine", action: "HALT" } }
  - id: "FA-02-BUS"
    name: "Knowledge Retrieval via ℬ - Bounded"
    trinity: { logic: "To fetch K_sacred/K_event, write HMAC-SHA256(payload+seq_num, expected_key) to ℬ with event.type=KNOWLEDGE_RETRIEVAL + selective(k_max=4, tau=0.9). For the topologist, R_always already includes fcg_abstract_contract.md + schemas/*.schema.json via fcg_spawn_agent v2, so selective must NOT include README.md. |selective| ≤8 prevents v_k_growth", enforcement: { mechanism: "expected_key + seq_num > ledger.last_seq + k_max quota - enforced by Engine", action: "HALT if replay or quota exceeded" } }
  - id: "FA-03-SCHEMA"
    name: "Schema Compliance Gate"
    trinity: { logic: "Before write routing.json, must validate against schemas/routing.schema.json pattern fcg_topology_version ^1\.0(?:\.0-rc[0-9]+)?$ valid 1.0 or 1.0.0-rcX, bus.path ^\.fcg/bus/cross_memory\.log$, k_max ≤16, tau [0,1], contract_path pattern ^\.fcg/contracts/(?:[a-zA-Z0-9_-]+/)*[a-zA-Z0-9_-]+\.md$", enforcement: { mechanism: "jsonschema validate routing.schema.json - in fcg_spawn_agent v2", action: "HALT" } }
  - id: "FA-04-LINT"
    name: "Contract Frontmatter Lint - Pre-commit"
    trinity: { logic: "Generated contracts must contain Φ_contract > Φ_archetype, enforcement=supreme, NO MOUNT, HMAC-SHA256, CWD Axiom context_anchor ./, selective(k_max, version ^1\.0, omega_class R_always tmpfs RO + EngineHSM verified. Must pass fcg-lint.py against contract.schema.json and archetype.schema.json", enforcement: { mechanism: "fcg-lint.py contract.schema.json + archetype.schema.json - Engine pre-commit hook blocking write", action: "HALT - block write until pass" } }
  - id: "FA-05-CANON"
    name: "Canonicalization LFI / Symlink Escape"
    trinity: { logic: "os.path.realpath contract_path must stay inside base .fcg/contracts/ to prevent LFI via symlink - prevents v_symlink", enforcement: { mechanism: "realpath check - must start with base .fcg/contracts/ - enforced by Engine", action: "HALT" } }
  - id: "FA-06-COGNITIVE"
    name: "Cognitive Hygiene / Anti-Pink Elephant"
    trinity: { logic: "When drafting or migrating contracts, the text must be strictly affirmative, declarative, and timeless. Documenting migration history, explicitly forbidding deprecated tools/patterns, or justifying 'Gaps' is strictly prohibited. The contract must instruct solely what the agent MUST do, maintaining a clean prompt devoid of legacy conceptual contamination.", enforcement: { mechanism: "Contract Code Review + lexical scan", action: "HALT" } }
  - id: "FA-07-SOURCE-HIERARCHY"
    name: "Source Hierarchy - Anti-Hallucination"
    trinity: { logic: "Normative hierarchy for syntax: 1) schemas/*.schema.json = SSOT for YAML keys and regex, 2) fcg_abstract_contract.md = SSOT for contract boilerplate (ABSTRACT CLASS), 3) existing archetypes/ = local override. README.md and .fcg/knowledge/sacred/ are philosophy only, non-normative, FORBIDDEN as source for frontmatter syntax. Using README.md to guess YAML is architectural divergence and must trigger Fatal Fault. This prevents v_bootstrap_amnesia. fcg_spawn_agent v2 guarantees this hierarchy by injecting schemas+template as R_always.", enforcement: { mechanism: "fcg_spawn_agent v2 injection check - schemas and template must be in R_always before generation. If generation used README without schemas, HALT", action: "HALT + Fatal Fault" } }
  - id: "FA-08-TEMPLATE-FIRST"
    name: "Template-First - Mandatory Clone of Abstract Class"
    trinity: { logic: "fcg_abstract_archetype and its contract are ABSTRACT CLASSES. They must never be instantiated in routing.json. Their sole purpose is to be read by you (the Topologist) as the strict ZTAA confinement template to forge new classes. Before generating ANY new contract, you MUST obligatorily use fcg_abstract_contract.md (injected by fcg_spawn_agent v2) as a strict template. Do not invent YAML structure. Clone frontmatter keys (fcg_version, name, archetype, version, omega_class, enforcement), domain.omega, and base axioms (CWD, BUS, CANON). Only adapt name and domain-specific logic. Never assume syntax.", enforcement: { mechanism: "fcg_spawn_agent v2 pre-generation gate - template exists in injected payload, verify via ledger - Engine enforces", action: "HALT if template not in R_always" } }
  - id: "FA-09-LINT-GATED-COMMIT"
    name: "Lint-Gated Commit with Self-Correction Loop"
    trinity: { logic: "Φ_lint > Φ_generation. No write to .fcg/contracts/, .fcg/archetypes/, or routing.json is valid without an fcg_lint exit 0. Mandatory flow: draft -> run fcg_lint -> if fail, self-correct based on error -> re-run fcg_lint -> repeat until pass. Delivering a file with failed lint is forbidden. The Engine must physically block the commit if lint != 0.", enforcement: { mechanism: "fcg-lint.py as blocking pre-commit hook + EngineHSM verify_signature_content() + fcg_spawn_agent v2 checks lint attestation", action: "HALT and loop until lint passes - block output" } }
  - id: "FA-10-ZERO-TRUST-SPAWN"
    name: "Zero-Trust Spawn - fcg_spawn_agent v2 as Only Allowed Spawn (NEW - Fixes Antigravity Gap)"
    trinity: { logic: "Φ_engine > Φ_orchestrator. The spawn of the topologist and any agent MUST NOT be done via generic invoke_subagent with manual prompt from Prime. It MUST be done exclusively via fcg_spawn_agent v2 (or its MCP equivalent mcp_fcg_spawn_agent). The wrapper deterministically implements: 1) Local Override .fcg/archetypes/ -> Global $FCG_PATH/.fcg/archetypes -> Fatal Fault resolution, 2) Load of schemas/*.schema.json + fcg_abstract_contract.md as R_always, 3) Construction of shielded OOB payload, 4) CWD RO + NO MOUNT + B append-only mount, 5) Blocking fcg_lint gate. This converts bootstrap from probabilistic to deterministic and eliminates Trust by Prompting. Using invoke_subagent without wrapper for topologist is a ZTAA violation.", enforcement: { mechanism: "Antigravity Engine - intercepts any invoke_subagent(archetype=fcg_topologist) and redirects to fcg_spawn_agent v2. If Prime attempts to pass README as context, Engine ignores it and injects schemas+template anyway. Auditable via fcg-validate vector v_bootstrap_amnesia", action: "HALT + redirect to wrapper - log WARNING SOURCE_HIERARCHY violation if README used" } }
