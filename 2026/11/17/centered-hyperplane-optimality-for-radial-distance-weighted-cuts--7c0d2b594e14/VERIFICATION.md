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
# Verification and reproducibility

The analysis proves the centered-cut statement for all compactly supported rotation-invariant hyperplane-null laws and all continuous nonnegative nondecreasing distance kernels by an antipodal/transverse-reflection comparison of the moving-boundary variation. The exact circle profile is an evaluation of two complete chord integrals; the high-dimensional terms follow by Laplace expansion with controlled remainders.

Run `python checker.py` in the same directory with installed NumPy and SciPy. Actual execution returned: `PASS: sphere d=2,3 exact; eight dimension quadratures; three high-d remainders; seven independent circle cut profiles`. The verifier computes circular cuts from independently discretized chord pairs using an FFT convolution, not by substituting the claimed profile. It also checks spherical integral values by adaptive quadrature. Finite grids and numeric quadratures cannot prove infinite-dimensional or all-measure assertions and do not replace the analytical steps.

No external independent mathematical audit has been performed. Literature priority remains provisional.
