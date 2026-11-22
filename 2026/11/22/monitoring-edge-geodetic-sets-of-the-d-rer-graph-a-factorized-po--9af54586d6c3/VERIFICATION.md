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

# Verification

Execute `python3 verify.py` using standard Python 3. The program builds the exact 12-vertex, 18-edge graph, calculates shortest-path distances before and after deletion of each edge, and derives all monitoring pairs independently of the statement of the theorem. It checks the three representative witness-pair tables, evaluates the monitoring predicate and the structural criterion on all \(2^{12}=4096\) subsets, and verifies the full polynomial and all inclusion-minimal configurations. It separately enumerates every optimal one-token jump and graph-edge slide and checks the bijection to two four-choice coordinates.

Observed output starts with `VERIFY_OK` and reports 16 minimal sets, coefficient sequence \(16,72,129,116,54,12,1\) for cardinalities six through twelve, and 24 exchange edges. The proof of the factorization and product graph is mathematical and self-contained in `RESULT.md`; the code is a finite replay, not a claim about other generalized Petersen graphs. Independent verification has not been performed.
