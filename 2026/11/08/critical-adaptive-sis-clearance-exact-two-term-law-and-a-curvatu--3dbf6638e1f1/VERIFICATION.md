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

# Mathematical and computational checks

The proof independently verifies forward invariance, global comparison at the critical threshold, stable link-response convolution through order two, and integrability of the renormalized inverse-prevalence derivative. The exact functional coefficients are \(K=1-\tau h_1\) and \(B=\tau(h_1-h_2)/K\), with response coefficients defined in the main result.

The standalone `verify.py` is self-contained apart from Python, SymPy, SciPy and NumPy (SciPy supplies the ODE integrator). It checks the first three Taylor coefficients of the invariant-graph defect symbolically, verifies \(h_2=-\kappa/4-1/16\), and asserts \(B=\kappa/3-1/4\), including the critical \(\kappa=3/4\) and the two opposite signs. Numerical integration of the original, not truncated, ODE at \(\kappa=0,1\) confirms that the corrected inverse-prevalence residual is approximately constant on widely separated late times. Execute `python verify.py` to reproduce the diagnostics.

The finite computations do not prove the asymptotic limit; the stable-convolution and integrable-remainder arguments do. The sign classification is exact only under the stated analytic model assumptions. An independent external scientific audit has not been performed.
