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

# Reproducible verification

Run `python checker.py` with `sympy` and `numpy`. The checker performs the exact fourth-order bivariate Fourier-eigenfunction computation and a separate fourth-order univariate construction in three directions. The polarization identity recovers the same mixed coefficient. It performs 26 assertions, including root signs, two limiting coefficients, first and second displacement cumulant normalizations, and finite-matrix tilted-eigenvalue Cauchy-integral diagnostics for five positive reset ratios. All 26 assertions passed for this package.

The complete mathematical proof is in RESULT.md. The exact finite Fourier perturbation recursion establishes the fourth coefficient analytically; the finite-matrix numerical tests do not certify the infinite operator or determine the number of roots. The single positive root follows from a one-sign-change polynomial and two exact rational bracket signs. The general characteristic function and physical model are prior published work; publication priority has not been independently established.
