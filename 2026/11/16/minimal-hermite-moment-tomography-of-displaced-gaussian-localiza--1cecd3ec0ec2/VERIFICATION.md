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

The calculation is based on the normalized Bargmann-Fock measure \(\pi^{-d}e^{-|z|^2}dV\) and the polynomial indicator \(\mathbf1_{\{t+u\cdot z-|z|^2>0\}}\). The proof verifies sign separation, convex-gradient recovery, boundary transport, covariance positivity, and optimality by invariance of domain.

Run `python check_gaussian_ball_tomography.py` with `mpmath` installed. Expected markers: `GAUSSIAN_BALL_MOMENT_TOMOGRAPHY_CHECK_PASS` and `dimension_two_cases=4 inverse_recoveries=3 centered_dimensions=2,4,6`. The checker spot-checks numerical calculations; it does not exhaust parameters or prove the universal theorem. The verification does not replace an independent audit.
