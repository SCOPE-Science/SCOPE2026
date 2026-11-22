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

# Reproduction and limits

Run `python checker.py` with Python 3 and SymPy. The program checks exact symbolic polynomial identities, absorbing boundary values, the full third-moment recurrence, the sharp critical response factorization and sign examples, and an independent one-dimensional interval limit. It printed `PASS: 27 exact symbolic, boundary, independent interval, and rational sign assertions` when tested. No finite numeric or symbolic collection is a substitute for the wedge-tail proof in `RESULT.md`; the exact calculation depends on classical first-exit asymptotics. There is no independent audit and no claim about globally optimal positive reset rates.
