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

# Reproduction and limits

Run `python verify.py` with Python 3, SymPy and SciPy installed. The self-contained file implements and checks the exact rational factorization, the strictly feasible unique threshold, a rational three-horizon example and independent adaptive quadrature comparisons. The analytic argument in `RESULT.md`, not a numerical sampling certificate, proves the universal assertion. The documented tests passed when run from this package.

The model is a scalar impulsive exponential store with an illustrative saturating response. It is not physically calibrated, does not identify water uptake with a reservoir sink, and does not prove any statement for full spatial Richards equations, field crop outputs or any uninspected formulation. Independent audit status: not performed.
