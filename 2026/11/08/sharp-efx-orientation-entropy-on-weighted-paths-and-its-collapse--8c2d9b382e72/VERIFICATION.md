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

# Verification of the path fairness census

Run `python verify.py` using Python 3 without nonstandard packages. The executable constructs every path orientation under selected positive weight vectors, checks the literal all-pairs/all-goods-removal EFX inequalities, and independently checks the derived sink conditions. It also checks the exact combinatorial counting formula, the extremal bounds, and the recurrence.

Observed output: `VERIFY_OK`; 3,343 weighted configurations; 397,362 orientation states; uniform/increasing exact comparisons for 1 through 13 edges; recurrence for 5 through 200 edges. The all-removals direct checker does not use the local criterion for its decision. Finite checks are evidence against small counterexamples, not a proof for all edge counts or real weights. The full argument appears in `RESULT.md`.
