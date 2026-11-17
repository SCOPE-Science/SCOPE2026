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

The stationary second-moment identities were proved by a unitary Fourier decomposition and complex Itô moment equations for the linear stochastic ring. Independently, run `python3 checks/check_stationary.py` from the package root. It uses only Python's standard library, constructs the real centered drift for three vehicles, and solves 25 continuous-Lyapunov equations in exact rational arithmetic in each of ten parameter cases. It checks the sharp energy-sign alternatives, a nontrivial exact increasing-energy witness, and both headway and speed variances.

The exact checker was executed from the actual package path and printed `PASS: 10 exact-rational 25-equation Lyapunov covariance tests, sharp-sign checks, rational witness`. These are finite exact checks, not a replacement for the stated analytic proof. The conclusions are limited to the stable centered Gaussian model with zero velocity alignment. No independent mathematical audit has been performed.
