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

The stationary angular Fourier modes are explicit eigenfunctions of the centered generator. The proof uses their resolvent to calculate the third tensor and then optimizes its directional cubic polynomial globally.

To reproduce the checks: install Python 3 with `sympy` and `mpmath`, then run `python CHECK.py` in this directory. On the original embedded files, the program printed `PASS 25 checks; critical ratio 1.94554336387280`. Checks include symbolic factorization, a unique positive threshold root, 15 independent high-precision eigenvalue finite differences, and angular objective comparisons.

The Fourier eigenvalue evaluations are finite numerical validations, not proofs for arbitrary rates or observation directions. Those quantifiers are established by the symbolic Poisson-resolvent identities, strict positivity of the factored amplitudes, and Descartes' sign rule. Initial angular transients do not affect the time-normalized cumulant limits.
