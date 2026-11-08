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

The proof verifies a positive Schur complement for all positive edge masses and hub mass; the exact inverse yields the evaluation kernels. Their signed zero locations and absolute integrals give the claimed uniform operator norm and norming locations. The phase threshold is an algebraic rearrangement with a positive denominator, while the small-arm jump follows from a one-sided parameter limit.

The accompanying standard-library script `verify_atom_star_projection.py` was run successfully and printed:

```text
INDEPENDENT_EXACT_MASS_MATRIX_AND_KERNEL_NORMS_OK 1440
EXACT_PHASE_SIGN_IDENTITY_OK 25
EXACT_COLLAPSING_BRANCH_JUMP_IDENTITY_OK 3
ALL_ATOMIC_STAR_LINEAR_SPLINE_CHECKS_OK
```

The 1,440 cases use exact rational Gram inversion and independent absolute-affine integration rather than merely evaluating the closed formula. These computations cannot establish universal inequalities on their own; the proof supplies those algebraic arguments. All claims require positive hub mass and constant positive densities on finitely many edges. Full-text comparison with Boman (2006) was unavailable; only its abstract was examined. Independent verification has not been performed.
