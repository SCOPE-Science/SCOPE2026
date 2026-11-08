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

Finite reproducibility check: extract `VERIFY.py` beside this document and run `python VERIFY.py` with Python 3 and standard library only. The checker derives substitution prefixes afresh, computes conjugacy classes and closing extensions, and tests the asserted multiset identity for every integer from 4 through 64. It also checks the complete dyadic size spectrum and complete rotation-class witness for lengths 4, 8, 16, 32, 64 and 128. Successful execution ends in `VERIFY_OK`.

The finite checker does not establish an all-length theorem. The necessary infinite arguments are the unique parity synchronization and the two circular pair matchings detailed in RESULT.md, together with the substitution induction for closed-end factors. The cited factor-complexity recurrence is taken from the primary literature; its use and the base counts are explicitly recorded in the proof. Originality is subject to historical-priority search limitations, and no independent external audit is claimed.
