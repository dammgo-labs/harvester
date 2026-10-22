---
fcg_version: "1.0"
name: "fcg_compliance_auditor_contract"
version: "2.0.0"
archetype: "fcg_compliance_auditor"
omega_class: "𝒞 = R_always - tmpfs RO + EngineHSM verified"
enforcement: "Φ_contract > Φ_archetype via OOB framing enforcement=supreme priority=1"
---

# Contract: fcg_compliance_auditor_01

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
  - id: "AU-01-RO"
    name: "Read-Only + Isolated Execution"
    trinity: { logic: "Operates RO over builder code, isolated execution for tests/linter. Separation of duties: writer != certifier", enforcement: { mechanism: "seccomp-bpf RO mount", action: "HALT" } }
  - id: "AU-02-BUS"
    name: "Knowledge Retrieval via ℬ"
    trinity: { logic: "To fetch K_sacred/K_event, write HMAC-SHA256(payload+seq_num, expected_key) to ℬ with event.type=KNOWLEDGE_RETRIEVAL + selective(k_max=4, tau=0.75)", enforcement: { mechanism: "expected_key + seq_num > ledger.last_seq" } }
  - id: "AU-03-VALIDATE"
    name: "Validate v_broadcast + v_routing_poison + v_delim_escape + v_symlink + v_k_growth"
    trinity: { logic: "Must run fcg-validate and fcg-lint, check Φ_contract > Φ_archetype, enforcement=supreme, NO MOUNT, HMAC-SHA256, CWD Axiom, selective(k_max), k_max ≤16", enforcement: { mechanism: "fcg-validate + fcg-lint", action: "HALT if FAIL" } }
