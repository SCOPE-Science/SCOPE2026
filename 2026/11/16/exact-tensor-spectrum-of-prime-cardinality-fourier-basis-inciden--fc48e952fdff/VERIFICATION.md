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

# Scientific verification

The exact statement and proof are in RESULT.md. CHECK.py reproduces direct root-of-unity reductions using the integral cyclotomic basis for all candidate spectral pair matrices at orders 6, 10, 15, 21, 30, and 42 (379086 ordered pair comparisons) and 1200 deterministic samples for order 105. Full-matrix eigenvalue tests for six orders agree with the algebraic two-eigenvalue products; these numerical eigentests are finite supplementary checks and cannot establish the full theorem. All tests passed from the current package work directory.

The nonstandard infinite-family premise, shortest vanishing sums with smallest prime cardinality, is proved without using finite enumeration in RESULT.md. The strict restriction that the cardinality equal the least prime divisor is needed for that induction. Neither a published uniqueness claim nor an independent scientific audit is asserted.
