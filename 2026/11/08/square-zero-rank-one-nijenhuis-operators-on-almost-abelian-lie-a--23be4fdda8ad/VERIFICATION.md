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

The original square-zero and Lie-Nijenhuis equations were tested directly on all basis pairs, for every nonzero ordered rank-one factorization, over seven finite-field configurations. The checker reconstructs the bracket from the specified action matrices, deduplicates operators by exact matrix entries, independently computes eigen-covectors by transposition, checks the nilpotent census and records the idempotent branch only as a regression comparison. The identity on arbitrary vectors follows from bilinearity and alternation, so basis-pair checking is exhaustive for each finite configuration. The checker works over prime fields and over the explicitly implemented nonprime field \(\mathbb F_4\).

Execute `python verify.py`. A successful run ends with `ALL_DIRECT_NIJENHUIS_AND_COUNT_CHECKS_OK`, and all seven expected lines are preserved in `verification_output.txt`. The program is a finite check. The infinite-field and arbitrary-dimension assertions rest on the separate proof in `RESULT.md`.

Scientific limitations: this does not independently certify the proof, establish priority over inaccessible or unidentified publications, enumerate higher-rank operators, or analyze unreduced schemes.
