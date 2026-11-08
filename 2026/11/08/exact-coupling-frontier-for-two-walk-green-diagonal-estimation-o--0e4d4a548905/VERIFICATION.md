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

The theorem is proved analytically in `RESULT.md`. It uses a normalized two-state Neumann resolvent, the layer-cake expansion for a pair of nonnegative integer counts, an attained Fréchet intersection bound, exact joint-survival probabilities for the half-shift stagewise stopping coupling, and dominated convergence for the long-walk asymptotic. None of these arguments relies on a finite parameter sweep.

`verify.py` is a standalone Python 3 standard-library script. `VERIFY_OUTPUT.txt` records the run and its 1,296 assertions, including rational stopping parameters, exact discrete quantile integration, probability inequalities and numerical checks of the limiting constant. The script is supplementary; it does not certify all real stopping probabilities, the abstract optimal-coupling argument, or asymptotic convergence. No independent scientific audit has been performed.
