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

Run `python3 check.py` using Python 3 with its standard library. The checker performs 52 explicit root, Gaussian-profile, independent Fourier-sum and finite-time optimization assertions; it prints the computed unique root and squared-norm coefficient. For the direct Fourier sum, the elementary tail bound \(\sum_{n>N}n^{-2}\le 1/N\) controls truncation, while the accelerated identity has a Gaussian tail. These computations test normalization and reproduce stated decimal values; they cannot verify global maximization or a claim over all \(BV\) functions on their own.

The all-time sharp inequality and equality cases rest on the derivative-measure coupling and strict-convexity proof. The limiting profile and unique microscopic jump separation rest on a uniform periodization estimate and strict monotonicity of the complementary-error-function ratio, as shown in RESULT.md. No independent audit or external validation has been performed.
