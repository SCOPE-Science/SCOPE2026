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

## Reproduction
Run `python verify_leaftrap.py` in a Python environment with NumPy. The script builds the full complex Liouvillian in column-major vectorization, includes the trap anticommutator with both site indices, inverts it on a localized nontrapped-leaf density matrix, and checks 90 combinations against the exact formula. The computations are finite and cannot independently prove statements for all graph sizes or the stated asymptotics; the analytic proof is in `RESULT.md`.

## Scientific limitations
The normalization is site offdiagonal decay rate \(\gamma\) and loss flux \(\kappa\rho_{tt}\). The exact formula requires strictly positive dephasing and trapping, real nonzero edge hopping, and a single initially occupied nontrapped leaf. No claim of independent scientific certification or experimental validation is made.
