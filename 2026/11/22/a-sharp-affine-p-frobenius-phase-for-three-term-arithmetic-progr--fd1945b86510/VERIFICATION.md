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

# Reproducible verification

`verify.py` is a standalone Python 3 script using only the standard library. It computes exact representation counts for each triple by the coefficient recurrence for three geometric generating functions and independently enumerates short two-variable base lists for a subset of parameters.

Command: `python3 verify.py`.

Observed checks: 977 coprime parameter pairs with \(5\le a\le90\) and \(2\le d\le\min(\lfloor a/2floor,28)\); 40,466 affine-phase levels; 977 first-successor levels; 20 independently generated base-order checks. All assertions passed in the recorded execution.

These tests have finite scope. Correctness for all admissible parameters rests on the row-count and order-statistic proof in `RESULT.md`. In particular the proof never treats an incomplete enumeration or a numerical timeout as a universal theorem. The originality assessment is contingent on the inspected literature, and an independent mathematical audit has not been performed.
