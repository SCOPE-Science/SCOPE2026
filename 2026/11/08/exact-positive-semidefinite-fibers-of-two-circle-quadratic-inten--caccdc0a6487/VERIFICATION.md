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

# Verification of the two-circle PSD fiber formula

The proof is self-contained in `RESULT.md`. `CHECK.py` (NumPy dependency) directly evaluates the original Hermitian quadratic forms and constructs the corresponding ten-by-nine real measurement matrix. Its computed eight-dimensional row space and one-dimensional nullspace, followed by rank nine with an additional off-circle sample, agree with the analytical theorem. Sixteen input combinations test PSD feasibility at the endpoint, in the interior and outside the interval. The trace-one counterexample is evaluated at nine independent angles on each radius. A separate 100-node Gaussian-Hermite quadrature verifies the Gaussian STFT identity against its closed form.

Run: `python CHECK.py`. Expected output: `TWO_CIRCLE_PSD_FIBER_CHECKS_PASSED 16_SETS_AND_GAUSSIAN_STFT`.

Numerical checks do not certify universally quantified statements; those are established by five-point Fourier coefficient recovery, a negative-subspace argument, a Schur complement and a factored radial polynomial. Independent audit has not been performed. No noisy-data stability or higher-degree result is asserted.
