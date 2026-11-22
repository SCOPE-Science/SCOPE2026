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

# Reproducibility notes

Run `python checker.py` using Python 3 and SymPy. The script reconstructs the inverse mass matrix, the two slope-influence kernels, their exact absolute integrals, an explicit sharp Lipschitz tent input, all quadratic influence inner products, and the trace, determinant and discriminant that yield the exact \(H^1\) norm. Five exact-rational knot positions are used for supplementary numerical consistency checks. The scalar sign changes, Sobolev duality, extremizer attainment, minimizer uniqueness and all-parameter asymptotics are justified analytically in `RESULT.md`; the finite set of rational cases does not establish an infinite claim by itself.

The results are exact algebraic consequences of the specified projector, not measurements of computed discrete projections. No independent external audit has been performed.
