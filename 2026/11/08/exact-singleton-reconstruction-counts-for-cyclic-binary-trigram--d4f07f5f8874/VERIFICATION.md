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

The source word is an indexed binary vector of length \(n\), and each trigram uses cyclic indices. Execute `python3 verify_direct.py` and `python3 verify_runs.py` with Python 3 standard library, from this directory. These scripts do not call outside services.

`verify_direct.py` enumerates all binary indexed words for lengths 1–18 and independently reconstructs each profile's rotation-class fiber. It prints `DIRECT_OK` on success. `verify_runs.py` examines run-composition transitivity in a separate enumerator, tests paired simultaneous rotations and matches the first 120 coefficients to the exact rational recurrence. It prints `RUN_TRANSITIVITY_OK`, `PAIRED_TRANSITIVITY_OK`, and `RATIONAL_SERIES_OK` on success.

## Limits

Finite enumeration only checks finite cases. The theorem for arbitrary lengths follows from the binomial-count transitivity argument and the geometric generating-series proof in `RESULT.md`. No independent external proof audit is asserted.
