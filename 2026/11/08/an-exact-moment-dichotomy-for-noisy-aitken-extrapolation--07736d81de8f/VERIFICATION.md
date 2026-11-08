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

# Verification record

The standalone `verify.py` uses exact symbolic covariance arithmetic and high-precision Gaussian tail integration. Its completed execution reported 93 passed assertions; see `verification_output.txt`. Reproduce in a fresh Python environment by installing the dependencies in `requirements.txt` and running `python verify.py`.

The checks independently confirm the deterministic geometric Aitken identity; the exchangeable covariance contractions; the special fully shared-noise and curvature-free noise cases; the aligned geometric perturbation case; the exact rank-one Gaussian example; and high-precision finite-threshold tail approximations. The exact rational checks also cover positive-definite diagonal covariance examples. The asymptotic theorem for all admissible Gaussian covariances follows from the written Gaussian regression and pole-tail argument, not the finite numerical sample. The verifier uses finite \(t\) values only to detect algebraic mistakes, and it does not constitute an independent audit or external certification.

Scientific scope: one unmodified scalar \(\Delta^2\) extrapolation, three observations, jointly Gaussian additive noise with an arbitrary positive-semidefinite covariance. Non-Gaussian, nonlinear-history and regularized-extrapolator claims remain unproved.
