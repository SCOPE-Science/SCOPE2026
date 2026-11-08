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
# Reproducibility

`verify.py` is a complete, standalone standard-library Python 3 program, included alongside this document. Run `python3 verify.py` without input files. The program computes root-subtree generating polynomials and tests them against direct brute-force geodesic-triple enumeration on every labeled tree with three, four, or five vertices, plus five additional larger trees. It additionally tests a distinct graph-corona root-projection formula on four non-tree graphs, and compares the degree-maximum coefficient against simplicial-vertex counts. Its observed output is:

`VERIFY_OK graph_cases=153 enumerated_vertex_subsets=293568 tree_corona_recurrence=PASS root_projection=PASS top_simplicial=PASS`

These tests examine finite instances only, not all trees or all graphs. The unrestricted assertions are supported by the explicit structural proof in RESULT.md. All calculated coefficients use exact integer arithmetic. Self-review passed; no independent mathematical audit or independent certification has occurred.
