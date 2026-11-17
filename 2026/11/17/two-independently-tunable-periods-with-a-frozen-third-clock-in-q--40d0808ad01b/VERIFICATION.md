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

The result is proved by exact angular reduction, differentiated positive-period integrals, an explicit nonzero Jacobian limit, and a monotonicity argument valid over every geometric branch. The hyperbolic limit-cycle criterion is Theorem B and Proposition 4.3 of the cited Cao–Llibre source.

`check.py` was run with Python 3, mpmath and sympy. It compared exact third-period and first-two-period quadratures, verified the determinant for a rational geometry and reproduced the limiting determinant coefficient in four separated circle configurations. The tests are numerical checks, not exhaustive proofs. The inverse-function theorem establishes only local period control. No independent mathematical audit has been performed.
