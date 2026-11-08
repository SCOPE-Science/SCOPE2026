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

The analytic proof establishes global optimality for all real parameters in the stated domain and all bulk multiplicities, using exact block eigenvalues and a strict scalar optimization. It establishes the two-iteration criterion from minimal-polynomial degree, not from numerical convergence tolerances.

Run `python check_preconditioner.py` with Python 3 and NumPy. A deterministic run gave `PASS 44183 checks`. The checks include exact rational crossing identities, random SPD inputs with varied bulk sizes, sampled global-scale comparisons, and explicit CG iterates. These tests are finite validation only, not a replacement for the continuous proof. No independent audit or independent validation has been performed.
