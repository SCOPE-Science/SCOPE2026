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

# Reproduction of finite calculations

Run `python3 check_multipartite_inball.py` using Python 3.10 or newer, with no third-party packages. The expected success line is:

`MULTIPARTITE_SYMMETRIC_EDGE_INBALL_CHECKS_PASSED 67 cases`

The checker exhaustively iterates vertex labels in the set `{0,1,2}` for all qualifying integer partitions of graph orders 3 through 9. It tests the edge-difference bound, connectedness of the unit-difference subgraph, and exact rational squared norms, then compares the maximal norm and the number of maximizing facets with the theorem. It additionally verifies explicit higher-order predictions, including 78 tangent facets for the graph with four classes of size two and 924 for four classes of size three.

These are bounded finite tests. The claim for all numbers of vertices and all positive class sizes follows from the analytical facet-potential proof, not from finite experiments. Historical priority and the generalization to other graph families have not been independently verified.
