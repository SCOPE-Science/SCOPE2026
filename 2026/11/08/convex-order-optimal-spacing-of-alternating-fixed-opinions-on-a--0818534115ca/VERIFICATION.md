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

Run `python3 checker.py` from the directory containing the supplied `checker.py`, with Python 3 and SymPy available. The checked execution printed `PASS 39942 exact assertions`.

The independent full-state generator construction verifies the claimed finite stationary laws for all tested alternating arrangements with two or four fixed agents on cycles of 4 through 7 vertices. Other exact-fraction assertions test every stated elementary balancing move with total lengths 4 through 27, relevant convex call functions, small multi-interval compositions, and the explicitly reported 12-vertex example. The tests are finite. The universal conclusion is proved analytically by domain-wall recurrence, the one-sign-change distribution comparison, and integer majorization; the computations are supplementary rather than exhaustive for all cycle sizes.

This document reports computational and proof-level checks only. Independent assessment has not been performed.
