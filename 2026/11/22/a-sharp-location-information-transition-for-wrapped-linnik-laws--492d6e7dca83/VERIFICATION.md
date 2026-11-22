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

Install the declared optional checker dependency with `python -m pip install -r requirements.txt` and run `python verify.py` with Python 3. It checks 106 stated numerical/algebraic relations for four shape values, two scales, near-origin density and derivative behavior, integral finiteness and 24 exponential-mixture coefficients. The analytic proof of the three asymptotic regimes and the Fisher-information boundary is in `RESULT.md`; numerical tests cannot establish those assertions for all admissible parameters. All output file bytes can be hashed with standard SHA-256 tools. No independent external mathematical audit has been carried out.
