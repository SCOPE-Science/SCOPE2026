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

# Reproducibility and actual verification

Run `python check.py` under Python 3 with SymPy. The script constructs every convex hull directly in Cartesian coordinates for \(4\le n\le12\) and compares its signed shoelace area and chordal perimeter against the cyclic-gap identities. It also verifies the area–perimeter inequality numerically in every proper subset. As symbolic checks, the script derives geometric-moment formulas, fifth-order cancellation identities, covariance reductions, and a finite uniform-composition marginal identity.

Actual output:

```
DIRECT_GEOMETRY_SUBSETS 7813 NONTRIVIAL 7804 MAX_ERROR 1.7763568394002505e-15
MOMENT_SYMBOLIC_CHECKS_PASSED 11 covariances positive definite at 19 fractions
CUBIC_CANCELLATION_AND_FIFTH_GAP_PASSED
FINITE_COMPOSITION_MOMENTS_PASSED
```

Finite checks are corroboration, not proof of all-dimensional monotonicity or a full conditional central limit theorem. The paper's analytic Fourier argument and strict-concavity proof supply those conclusions. No external independent audit has occurred.
