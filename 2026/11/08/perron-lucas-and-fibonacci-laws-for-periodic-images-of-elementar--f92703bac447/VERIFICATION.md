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

Run `python3 verify.py` from the same directory using Python 3 and its standard library. It generates exactly 45 reachable Boolean relations, verifies the entire vector support and two-step annihilation, checks the 13 numerator coefficients, enumerates every periodic input for lengths 1 through 12, and independently checks 80 transfer/recurrence terms. The all-length proof uses the vector identity, not the finite tests. The rule is a one-step indexed cyclic map; no independent audit has been performed.
