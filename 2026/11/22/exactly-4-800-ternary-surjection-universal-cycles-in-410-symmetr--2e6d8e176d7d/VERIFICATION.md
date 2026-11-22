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

# Verification performed

`python3 verify.py` was executed from the same standalone package with the output:

```
VERIFY_OK windows=36 contract_vertices=6 trees=75 cycles=4800 symmetry_classes=410 orbits_6=20 orbits_12=390
```

The program constructs all thirty-six eligible windows from first principles, confirms the complete graph degree profile and exact cofactor, enumerates every 15,552 possible rooted rotor assignment, checks all 4,800 complete Euler tours by their cyclic windows, then exhaustively checks all twelve symmetry operations and their orbits. No probabilistic testing, float arithmetic, internet access or third-party module is required.

This finite certificate supports the complete orbit counts. The paper proof independently establishes the total labeled cycle count by the matrix-tree and BEST theorems. Novelty comparisons are limited by accessible literature; no independent validation is claimed.
