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

Execute `python3 verify.py` with Python 3; it requires no external modules. It checks the event recurrence against direct string enumeration, the four- and five-day identities, and both parity derivative formulas at many exact rational parameters and horizons. All assertions use exact rational arithmetic. The global proof of the arbitrary-horizon formula is in RESULT.md; finite regression checks are not exhaustive proofs.

The empirical motivation comes from observed flow-related barrier passage, whereas the two-consecutive-wet-day requirement is an explicit modeling abstraction. No independent external validation was performed.
