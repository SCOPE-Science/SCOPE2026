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

# Reproduction and boundaries

Run `python3 evidence/verify.py` from the extracted package. Standard Python 3 alone suffices. A successful output ends with `ALL_FINITE_CHECKS_PASS; infinite n uses the induction of RESULT.md`.

The checker constructs the proposed core from all whole-row, two-row/three-column and three-row/two-column simplices and adds every distinct-column three-cell transversal. For columns \(n=3,4,5,6\), it reconstructs the entire dual independently from the connectivity of **every** four-vertex induced subgraph, testing all \(2^{3n}\) subsets by a hereditary recurrence. For \(n=3,\ldots,8\), it applies all specified pivot matchings and compares the surviving face sets, not just their counts, against closed-form predictions. For \(n=3,\ldots,7\), it orients every nonempty-face Hasse cover and checks the entire directed graph is acyclic. For \(n=3,\ldots,6\), it independently computes all mod-two simplicial boundary ranks. A supplementary rectangular-core critical-pattern check at \(n=9,10,12\) also agrees with the formula.

The exhaustive finite checks do not prove the theorem at untested lengths. The general result depends on the explicit rectangular facet classification and the column-extension induction for the acyclic matching in `RESULT.md`. Neither external independent audit nor unindexed-literature priority review is claimed.
