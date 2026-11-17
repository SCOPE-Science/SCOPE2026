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

Run `python3 check_weighted_huber.py` with Python 3 standard library. The reproducible checker reports exact rational weighted-Huber minimizer roots, explicit sharp two-input witnesses, finite random rational inequalities, equal-weight parity, and near-equal-weight transitions. Exact finite tests cover dimensions through twelve; the all-dimensional and all-weight proof is supplied in RESULT.md.

# Limits

No independent mathematical audit has occurred. The program is a finite corroborating test, not a completeness proof for arbitrary real weights, and historical priority remains provisional owing to full-text access restrictions.
