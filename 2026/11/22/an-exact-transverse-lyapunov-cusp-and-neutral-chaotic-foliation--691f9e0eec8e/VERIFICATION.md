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

# Verification and limits

The standalone `verify.py`, extracted from this package and run with `python3 verify.py`, reported `PASS 764 finite recurrence/Jacobian/quadrature/cusp/ray checks`. It uses only Python's standard library, computes the exact invariant-diagonal recurrence and two spectral multiplier formulas, compares each closed-form logarithmic exponent with independent deterministic Chebyshev quadrature over the logistic arcsine coordinate, checks the two one-sided cusp constants, and tests neutral-ray conservation.

The limiting expressions and no-physical-measure theorem are **not** consequences of the finite checker. Their mathematical certificates are the direct polynomial reduction, fixed invariant subspaces, cosine-log integral, logistic ergodicity, and a Fubini/first-moment injectivity argument in `RESULT.md`. These steps cover all real positive symmetric competition parameters, not a numerical parameter grid. The exact critical point is included; the zero-derivative preimage null sets are excluded from almost-everywhere quantification. No independently performed audit is asserted.
