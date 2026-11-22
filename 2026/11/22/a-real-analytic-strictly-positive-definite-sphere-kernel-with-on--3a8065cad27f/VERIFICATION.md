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

# Verification of the single-mode spherical kernel construction

The proof is analytic. Each selected feature is a homogeneous harmonic polynomial, proved by direct ambient differentiation. The positive Gram sum is strict exactly when its feature moments separate finite atomic measures. The critical separation lemma uses a long consecutive exponent block and an ordinary nonzero-node Vandermonde determinant; it is not inferred from sampling. Four arbitrarily long degree-block families independently recover real/imaginary projection and height-weighted projection sums; degrees zero and one resolve the zero projection. All remaining site coefficients are then determined by a one-point or two-point fibre linear system.

For finite reproducibility, run `python check.py` with NumPy and SymPy installed. The test contains 34 exact harmonicity/homogeneity assertions, 990 exact block rule assertions, and ten finite Gram checks (1034 total). A successful run reports the smallest observed Gram eigenvalue near `1.9248516e-11`. Numerical testing does not prove strict positivity for all finite sizes or all positions, and no numerical bound on the worst possible Gram eigenvalue is asserted.

For the spectral statement, verify orthogonality of distinct spherical-harmonic degrees and the nonzeroness of every selected feature. All positive coefficients use the explicit geometric weights given in the result. To check the distributional witness, use orthogonality of the degree-one harmonic `x1` to `x3` and to every other selected degree, with normalized sphere measure. External independent auditing has not been performed.
