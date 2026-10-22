---
fcg_version: "1.0"
name: "fcg_abstract_contract"
version: "2.0.0"
archetype: "fcg_abstract_archetype"
omega_class: "𝒞 = R_always - tmpfs RO + EngineHSM verified"
enforcement: "Φ_contract > Φ_archetype via OOB framing enforcement=supreme priority=1"
---

# Contract: fcg_abstract_contract_template

> [!IMPORTANT] Φ_contract > Φ_archetype enforced by Engine via <contract enforcement="supreme">

domain:
  context_anchor: "./" # CWD Axiom regex ^\./(?!.*\.\./).*$
  omega:
    R: ".fcg/routing.json - tmpfs RO"
    C: ".fcg/contracts/ - tmpfs RO + verify_signature_content()"
    K: ".fcg/knowledge/ - NO MOUNT, request via ℬ"
    V: ".fcg/volatile/ - NO MOUNT"
    B: ".fcg/bus/cross_memory.log - append-only HMAC(expected_key+seq_num)"

axioms:
  - id: "C-00"
    name: "Business Precedence Supremacy"
    trinity: { spirit: "The domain contract represents invariant operational law overriding archetype defaults.", logic: "Φ_contract > Φ_archetype via OOB framing enforcement=supreme priority=1.", enforcement: { mechanism: "Engine HSM Contract Gate", action: "HALT" } }
  - id: "DB-01-CWD"
    name: "CWD Axiom Strict Confinement"
    trinity: { spirit: "Strict Zero-Trust workspace containment preventing directory traversal or unauthorized mount access.", logic: "Only ./ allowed, .fcg/knowledge/, .fcg/volatile/ NO MOUNT", enforcement: { mechanism: "eBPF VFS + Landlock LSM + seccomp-bpf CWD regex ^\./(?!.*\.\./).*$", action: "HALT" } }
  - id: "DB-02-BUS"
    name: "Knowledge Retrieval via ℬ"
    trinity: { spirit: "Knowledge access strictly via HMAC-authenticated event bus to preserve minimal context footprint.", logic: "To fetch K_sacred/K_event, write HMAC-SHA256(payload+seq_num, expected_key) to ℬ with event.type=KNOWLEDGE_RETRIEVAL + selective(k_max=4, tau=0.72)", enforcement: { mechanism: "expected_key + seq_num > ledger.last_seq", action: "HALT" } }
