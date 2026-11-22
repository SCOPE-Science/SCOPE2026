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

# Verification

The included standalone `verify.py` uses exact integer permutation enumeration and `fractions.Fraction` for each n from 3 through 8. It checks every feasible conditional circular-descent mean, every factorial mixed moment, and each parity-dependent unique maximizing fixed-point class. It reports `Exact enumeration assertions passed: 117`.

The general proof is a forced-fixed subset counting argument followed by finite inclusion-exclusion. Finite computations alone do not prove the all-n statement. No independent audit or publication-priority determination has been performed.
