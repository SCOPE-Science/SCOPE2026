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

# Verification scope

Run `python verify.py` with Python 3, SymPy and mpmath. It checks the exact logistic-addition identity and the two critical derivatives, the Taylor/rational five-root witness, and representative numerical phase and stability signs at high precision. The final theorem's global classification follows analytically in `RESULT.md`. It is not established by enumerated numerical cases; no experimental calibration, full-text verification of an inaccessible motivating source, or independent external validation is asserted.
