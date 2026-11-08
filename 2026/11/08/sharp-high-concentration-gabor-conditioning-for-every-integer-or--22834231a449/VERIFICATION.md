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

# Reproducibility and limits

Run `python3 CHECK.py` with the Python 3 standard library. The script checks coefficient arithmetic, monotonicity, and finite Zak-grid values for a range of fixed integer orders and concentration parameters. Its successful output is `MATERN_GABOR_ASYMPTOTICS_CHECKS_PASSED 17300`. The mathematical justification of the limits is the exact Zak symbol and uniform asymptotic proof in `RESULT.md`, not finite tests or curve fitting. No independent audit has been carried out.
