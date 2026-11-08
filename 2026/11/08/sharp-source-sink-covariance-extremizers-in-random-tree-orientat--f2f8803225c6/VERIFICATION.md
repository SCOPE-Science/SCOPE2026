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

Run `python verify.py` in the directory containing this file and the embedded `verify.py`. The script uses only the Python 3 standard library and exact `fractions.Fraction` arithmetic.

The script enumerates all Prüfer-coded labeled trees for orders 4, 5, 6, 7 and 8 (16, 125, 1296, 16807 and 262144 trees respectively). It tests both exact extremal bounds and uniqueness characterizations for each tree. It independently enumerates every orientation for every labeled tree of orders 4, 5 and 6 and checks sample covariance against the asserted degree-local identity. All these tests passed on the extracted code. The general proof is in `RESULT.md` and does not rely on extrapolation from finite checks.

The checker does not examine external publication priority or provide an independent proof audit. The finite exhaustive checks cover only the explicitly enumerated orders. The claimed all-order theorem rests on the displayed mathematical inequalities.
