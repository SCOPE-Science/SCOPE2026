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

# Verification of the affine-projection face-skeleton theorem

To reproduce the exact rational checks, execute `python3 checker.py` from a directory containing the standalone checker. The checker has no external dependencies. It reports:

```
EXACT_ALTERNATE_BETA_POLYNOMIAL_INTEGRALS_OK 594
EXACT_FACE_SKELETON_COVARIANCES_OK 594
EXACT_FACE_LEVEL_AND_SOLID_MONOTONICITY_SAMPLES_OK 33
UNIFORM_FIRST_ORDER_REMAINDER_CERTIFICATE_SAMPLES_OK
DIRECT_DISCRETE_VERTEX_KERNEL_NORMS_OK 38
EXACT_VOLUME_RADIAL_MOMENTS_OK 38
ALL_CROSSPOLYTOPE_SKELETON_PROJECTION_CHECKS_OK
```

The alternate Beta-integral computation expands \((1-u)^{s-2}\) and integrates every monomial from the moving kernel sign threshold to one using rational arithmetic. The theoretical covariance is checked by a separate calculation via coordinate inclusion probabilities and Dirichlet moments. The first skeleton is also verified by direct enumeration of all signed coordinate vertices. The volume kernel covariance is checked against the exact radial law.

These computations are finite checks. The mathematical claim for all \(d\ge2\) and all \(1\le s\le d\), the strict vertex-only norming property, the complete monotonic hierarchy and the asymptotic limit are derived analytically in RESULT.md. No independent verification or scientific audit has been performed.
