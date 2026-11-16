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
# Reproducibility and exact checks

Run `python su2_cone_verify.py` with SymPy installed. It computes the contribution of tensor fusion to each character coefficient for degrees zero through thirty, compares it with the all-degree symbolic formula, solves three pairs of affine constraints, and checks the constant-kernel factorization and sample positivity signs at three exact rational radii.

The infinite theorem is based on the algebraic character-product identities, compact-group Bochner positivity, and the all-degree formula in `RESULT.md`. Neither numerical sampling nor finite coefficient verification establishes positivity for arbitrary degree. The checked code is supplementary. The sign claims on the two feasible vertices hold analytically for every \(0<r<1\) because their displayed numerators are \(1-r^2\); the third intersection is excluded by numerator \(r^2-1\). No external independent audit was performed.
