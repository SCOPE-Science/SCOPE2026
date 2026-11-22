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

Run `python3 verify.py` from the same extracted directory. The program directly reconstructs the eight-by-five carry table, checks all rational zero-tail fixed points, tests the exact first nonzero digit branches and strictness structure, compares direct Franel sums with the forbidden-digit criterion, and tests the one-third maximum and equality cases for many shifts.

The proof's all-step claim is not inferred from finite tests: it follows from the full 40-case table, the verified zero-tail boundary, backward superharmonic induction and the positive-branch strictness argument. Historical uniqueness is not independently certified.
