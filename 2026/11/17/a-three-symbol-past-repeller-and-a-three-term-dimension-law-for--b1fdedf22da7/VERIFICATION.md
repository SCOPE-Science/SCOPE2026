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

The included checker `verify_implicit_cubic.py` tests branch residuals and derivative enclosures on seven step sizes and seven targets on each of three branches; it also checks the exact polynomial identity for 109 integer inputs and compares positive roots numerically. The full proof is given in RESULT.md. Finite numerical sampling cannot certify the all-real-parameter inequalities or the IFS dimension theorem. The exact algebraic bounds in RESULT.md provide those arguments.
