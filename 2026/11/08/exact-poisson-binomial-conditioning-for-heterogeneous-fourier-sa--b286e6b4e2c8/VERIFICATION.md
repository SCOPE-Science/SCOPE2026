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

# Verification scope

The self-contained checker `artifacts/verify.py` constructs twelve actual complex Fourier restrictions for heterogeneous finite cyclic factors and nontrivial marked coordinate values. It computes their Hermitian Gram eigenvalues and independently computes the predicted Poisson-binomial spectral list. On replay it reports `HETEROGENEOUS_PUNCTURE_SPECTRUM_PASS cases=12 max_error=3.66e-15` (rounding may vary with NumPy). The examples include unequal product alphabets and several interaction degrees. Numerical equality checks are corroborative only.

# Proof verification

The mathematical argument in `RESULT.md` verifies the coordinate orthogonal decomposition, rank-one tensor action, band-compressed eigenvalues and multiplicities, strict top-eigenvalue ordering on the unobserved rectangle, and the explicit extremizer. The result holds for all finite abelian groups by product-character orthogonality; experiments cover cyclic factors only. No external or independent audit has been performed.
