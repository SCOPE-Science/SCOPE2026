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

# Reproducibility and verification

Execute `python verify.py` in a directory containing that single standalone file, with Python 3, NumPy, SciPy, and SymPy installed. It checks exact characteristic-polynomial algebra under \(s^2=c^2-1\), the derivative identity for the hyperbolic threshold function, and the neutral Perron eigenvalue. At \((\beta,\gamma)=(1,4/5)\), it evaluates the right and left positive eigenvectors, compares the explicit coefficient \(q\) against high-order Gaussian quadrature, and integrates 1500 periods of the nonlinear vector field to check the finite-time approach toward \(n p(nT)\to v/q\).

The exact symbolic identities are reproducible computational checks. Numerical quadrature and finite-time integration only corroborate, rather than certify, the theorem's \(t\to\infty\) quantifiers. Those follow from the positive adjoint Lyapunov argument and a one-dimensional neutral-mode reduction described in `RESULT.md`. No external independent audit has been performed.
