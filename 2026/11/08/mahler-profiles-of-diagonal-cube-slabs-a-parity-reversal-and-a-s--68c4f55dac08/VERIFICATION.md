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
The formula for clipped-cube volume follows from an exact Irwin--Hall inclusion--exclusion identity. The formula for the polar follows from the outward pyramids over visible cross-polytope facets, together with an explicit argument that the two antipodal pyramidal enlargements meet only in the original cross-polytope. A recurrence proves strict central unimodality of cube-sum densities, giving the odd-dimensional monotonicity; differentiability and exact facet counts give the even-dimensional right derivative. Polynomial differentiation and a positive Bernstein expansion settle the complete three-dimensional extremum pattern.

Running `python checker.py` with NumPy, SciPy and SymPy tests the independent hull-volumes against exact formulas for 15 configurations in dimensions 2--5. It also checks exact symbolic identities and finite binomial/polar formulas through dimension 10. The checker does not certify any unbounded quantifier by computation, and no independent audit has occurred. The singular zero-width limiting section does not itself have an ambient-dimensional Mahler product.
