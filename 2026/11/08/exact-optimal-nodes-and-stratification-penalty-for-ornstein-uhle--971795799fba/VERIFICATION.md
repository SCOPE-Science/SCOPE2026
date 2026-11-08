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

# Verification

The claimed stationary OU conditional integral covariance has two independent derivations: the local Gaussian Markov bridge/terminal decomposition in the proof, and the global Schur complement of the covariance matrix. The supplied script `verify_ou_quadrature.py` checks their agreement on deterministic optimized and randomized designs for multiple \(\lambda\), \(n\), and covariance scales. The symbolic checks verify the exact first derivatives, cubic Taylor coefficients, and the rational moments \(3/2\), \(16/7\), and \(-307/336\) needed for the Gaussian fluctuation variance \(11/864\). It passed 140 assertions with NumPy, SciPy and SymPy installed.

To reproduce, place the checker beside this document and run `python verify_ou_quadrature.py`. Its finite floating-point and symbolic checks are supplementary: strict convexity is proved analytically, and the limit law invokes the standard central limit theorem for bounded 1-dependent variables. Verification of specialist publication precedence remains incomplete because one closely related historical dissertation was accessible only through its abstract.
