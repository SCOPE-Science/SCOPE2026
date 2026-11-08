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

## Checkable finite proof

The twenty reversal classes of five-bit binary words give the universal length cutoff \(k\le20\). The graph-first `verify_graph.py` enumerates all closed directed walks on four-bit states without repeated reversal-class edge labels, canonicalizes rotations, checks all pairwise observation-mask intersections and asserts the complete twenty-word census. It returned `GRAPH_COMPLETE_OK expanded=3242 necklaces=20`.

A structurally separate `verify_direct.cpp` tests every indexed binary word for lengths \(5\) through \(20\), reconstructs windows directly using cyclic indices, canonicalizes by rotation, and verifies pairwise conflicts for each length. It returned `DIRECT_COMPLETE_OK total=20`. The outputs matched the canonical representatives in `CENSUS.txt`. Both programs were compiled or executed and checked against files extracted from the final package.

This proves exhaustiveness only because the twenty-class pigeonhole bound removes all larger lengths and the recursion or direct loop covers each word in the finite remainder. No randomized sample, partial enumeration, or timeout is used as a proof. Later alphabet sizes or window lengths are not addressed. Scientific historical-priority review remains same-model only; external independent review has not been performed.
