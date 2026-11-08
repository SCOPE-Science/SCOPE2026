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

# Verification record

The standalone `checker.py` was executed using the Python standard library. It passed 49 assertions: complete exact-rational parent-vector enumerations through seven vertices for three negative integer exponents, comparisons with the exact martingale variance formula, and decimal high-precision checks of the leading and second-order asymptotics at four increasingly negative exponents.

The theorem's infinitely many indices and parameter limit were verified analytically by summable uniform upper bounds. The checker does not certify those infinite statements. Reproduction command: `python3 checker.py`.

The centered global path-length limit for each fixed exponent is established in Gałązka--Wdowicka (2026); its supporting innovation representation and the new asymptotic steps are reproduced in `RESULT.md`.
