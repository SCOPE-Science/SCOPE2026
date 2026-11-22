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

# Reproducibility and limits

Run `python verify.py` with Python 3, SymPy and SciPy to reproduce the symbolic derivative identity, exact-optimum comparison grid, and quadrature cross-checks. The bundled source is standalone; there are no datasets, network calls, or other package dependencies.

The checker reports 36,369 assertions and dimensionless sample values. Its finite grid and numerical quadrature are supplemental checks only. The full-domain uniqueness claim follows from the derivative sign argument in RESULT.md. The midpoint crossing follows from a single exact inequality evaluated at the geometric midpoint; the asymptotic offset and monotone schedule sensitivity follow from the closed root formula.

This analysis neither certifies biological yield nor independently validates historical novelty. Independent audit has not been performed.
