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

Run `python3 verify.py` with Python 3 standard library. It computes exact integer Narayana entries, checks the bit formulas for all rows through 128, and checks the complete multiset and cumulative count for dyadic blocks through exponent seven. It prints `VERIFY_OK` on completion.

Finite tests do not establish the all-row claims. Those are proved using Lucas's theorem, parity-preserving symmetry, a finite block decomposition of binary subset indices, and the binomial theorem. The independent audit channel has not been performed.
