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

# Reproducibility

Use Python 3 with NumPy and SciPy installed, then run \(\texttt{python verify.py}\). The checker evaluates killed-diffusion resolvent integrals separately from the limiting ODE formula, and verifies the exact drift-free one-cycle identity, large-rate success constants, marked finite-rate transforms, limiting elementary identities, and positivity/covariance derivatives.

Analytical validity comes from the exact renewal transform, the \(r^{-1/2}\) boundary-layer expansion, a compensated Poisson martingale and differentiation of the OU boundary problem. Finite numerical cases do not verify all real parameter values or prove asymptotic convergence. The program does not assert independent scientific review or external certification.
