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

# Computational and analytic verification

The claim is for the standard characteristic-vector embedding of a total-matching polytope. The accompanying `check.py` uses only exact rational arithmetic (`fractions.Fraction`) and the Python standard library.

- Executed `python3 check.py` successfully, obtaining `TOTAL_MATCHING_OUTER_SPHERE_EXACT_PASS state_grids=1680_plus ties=3 centroid_injections_checked`.
- Evaluated every feasible edge count and remaining-vertex support size for each parameter pair in a finite grid of sizes up to 40 on the smaller side, also including values on either side of each exact screening boundary.
- Independently enumerated all injections for small parameters to confirm the contact-orbit coordinate barycenter and orbit cardinality.
- Verified equality cases `(8,12), (9,12), (9,15)` and the predicted strict integer window on that grid.

The infinite-dimensional-family conclusion is **not** inferred from numerical tests. Its proof is the exact orbit variance identity and the explicit monotonicity of two affine functions of matching size. Computational tests do not establish historical priority, and independent mathematical review has not been performed.
