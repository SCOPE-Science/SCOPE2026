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

# Verification and limits
The complete integer checker `artifacts/verify.py` uses only Python standard-library rational arithmetic. Run `python3 artifacts/verify.py` alongside `RESULT.md` to reproduce the exact finite cyclic cross-sums, digit moment products, recursive coefficients, closed lag-one formula, polynomial comparison identities, and sample all-lag extremizers. It reports `CHECK_OK 10456 exact assertions`.

All finite checks are corroborative, not a proof for unbounded primes, shifts or digit lengths. The all-quantifier statement rests on the recurrence, strong induction and exact algebra in `RESULT.md`. Independent audit is not yet performed.
