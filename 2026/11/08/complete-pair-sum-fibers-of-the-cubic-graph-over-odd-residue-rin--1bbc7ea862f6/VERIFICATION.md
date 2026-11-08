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

Run `python3 verify.py` from the directory containing the attached verifier. It uses the standard library only. It compares the exact local quadratic-root formula against direct pair enumeration at every target for 13 odd prime-power moduli, and checks five composite moduli through Chinese remaindering. It also checks the support count, energy and pair totals. Successful output ends with:

`VERIFY_OK local_cases=13 composite_cases=5 max_modulus=125`

The verifier checks only finite moduli; the unlimited claims rely on the algebraic proof in RESULT.md. No external audit or independent validation has occurred.
