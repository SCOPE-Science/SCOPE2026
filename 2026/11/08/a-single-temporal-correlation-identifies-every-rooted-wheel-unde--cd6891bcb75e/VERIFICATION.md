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

## Reproducible checks

Run `python3 verify.py` with Python 3 and no external dependencies. The checker constructs every off-diagonal stationary pair-covariance equation directly from wheel neighbor lists, solves the rational linear system, and compares the resulting hub/rim covariance with the analytic spectral formula using high-precision Decimal arithmetic. It tests three noise-square values \(q\in\{1/4,4/9,9/16\}\), all \(n=3,\dots,10\), rational inequalities at finite sizes, and larger-index high-precision values through \(n=100\). Current run: `VERIFY_OK 339 exact pair/spectral and large-index assertions`.

The code checks finitely many examples, not the all-size strict monotonicity theorem. The latter follows from the explicit Green-function identity, the upper bound \(t<1/6\), and positivity of \(F'_q\), as proved in `RESULT.md`. It neither establishes historical priority nor constitutes an independent mathematical audit.
