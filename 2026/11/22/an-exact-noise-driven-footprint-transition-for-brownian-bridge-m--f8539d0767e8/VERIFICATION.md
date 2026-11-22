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

# Verification of the fixed-width interval-sensing theorem

Execute `python verify.py` with Python 3, SymPy, NumPy, and SciPy installed. The script verifies symbolically that the posterior-risk derivative factors through the declared quadratic, the derivative's endpoint values and second derivative are correct, the integration of the Brownian-bridge cross-covariance gives the printed formula, and the target prior variance is exactly \(1/180\). It independently evaluates the bridge covariance double integrals using Gauss–Legendre quadrature and numerically checks optimality/phase selection over a range of widths and noise variances. The accompanying `verification_output.txt` captures the successful execution.

The package's analytic argument, not the finite computations, proves global placement and uniqueness for all admissible real parameters. The numerical computations check only specified finite grids; a floating-point maximum is not an exhaustive search and cannot prove a real-parameter uniqueness assertion. No theorem is claimed for unrestricted window widths, multiple observations, other kernels, or general noisy measurement operators.
