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

The executable `verify.py` checks twelve independently constructed convex hulls (dimensions 2–5 at three values of the deformation parameter), every named facet rank through dimension five, and the symbolic three-dimensional surface-quotient derivative. The analytic facet description and the global uniqueness statement are proved in `RESULT.md`, not extrapolated from the finite tests. The checker requires Python with NumPy, SciPy and SymPy. No independent audit has been performed.
