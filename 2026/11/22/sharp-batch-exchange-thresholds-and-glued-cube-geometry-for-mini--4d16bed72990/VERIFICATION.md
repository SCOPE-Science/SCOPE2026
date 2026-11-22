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

The mathematical argument is in `RESULT.md`; reproduce computational corroboration with `python3 verify.py` in the package directory using Python 3 standard library only.

The checker enumerates all eligible sizes of edge-deletion sets on five small tripartite graphs, counts each exact labelled optimum family, and confirms the sharp lower bound. It separately solves the exact-one-per-triangle binary equations in the balanced case for \(n=2,3,4\), then constructs the predicted optima and verifies every batch-threshold adjacency and all-pairs distances in balanced orders \(n=2,\ldots,7\). Four unbalanced tied-largest instances are checked for cube degree and diameter.

Observed completion markers: `TOTAL_SMALL_SUBSETS_TESTED 405579`, `COMPLETE_BALANCED_EQUALITY 4 optima 45 AB_matrices 65536`, `BALANCED_EXCHANGE 7 vertices 381 edges 1344 diameter 10`, `VERIFY_OK`.

This finite computation supports the proofs but does not constitute an exhaustive proof for unbounded parameters. It is not an independent mathematical audit; no external validation is claimed. Historical originality remains subject to unindexed and inaccessible prior literature.
