---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite verification and proof limits

`python3 VERIFY.py` runs direct vertex-subset enumeration of rook graphs, testing induced acyclicity with union-find and testing every one-vertex extension for inclusion-maximality. It compares component-count distributions and degree-structure predicates for the eleven boards with \(2\le m\le n\), \(m\le4\), \(mn\le16\). It then compares an independent path-component recurrence with the closed formula for 1,375 integer parameter triples, and checks boundary connectedness assertions on further arithmetic inputs.

Recorded execution:

```
VERIFY_OK rook_board_cases=11 nonempty_subsets=190277 maximal_forests=2740 independent_path_recurrence_checks=1375 component_distributions_and_structures=PASS
```

The verifier is independent of the main combinatorial proof but checks finitely many graph orders and arithmetic instances. It is not an exhaustive verification for arbitrary m and n; the mathematical proof in RESULT.md establishes the universal statements. Run using Python 3.10 or later with no third-party dependencies.
