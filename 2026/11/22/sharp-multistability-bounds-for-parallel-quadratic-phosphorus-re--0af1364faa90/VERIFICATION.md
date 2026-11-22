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

Run `python3 verify.py` with Python 3 (standard library only). The script checks 58 assertions with exact rational arithmetic, including the six signed two-channel witnesses, denominator-cleared degree-five numerator, and the constructive alternating-sign induction up to four positive recycling channels.

These finite checks do not prove the unbounded claim. The complete proof is the induction and polynomial-degree argument in `RESULT.md`: the degree bound applies to all positive real parameters and each inductive step permits an arbitrarily large finite saturation scale. Re-execution need not access a network. No independent mathematical audit has been performed.
