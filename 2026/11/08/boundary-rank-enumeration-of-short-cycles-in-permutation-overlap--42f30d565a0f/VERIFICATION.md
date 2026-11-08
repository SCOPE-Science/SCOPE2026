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

# Reproduction of the exact short-cycle census

The algorithm's all-order, fixed-length claim is established by the boundary-rank reconstruction proof in `RESULT.md`. This verification additionally checks its finite specialization at walk length \(3\).

Run `python3 verify_counts.py` from the folder holding all embedded files, with Python 3 and `g++` supporting C++17. It compiles `count_three_cycles.cpp`, enumerates every ordered first-three rank tuple and possible final-three rank set for all \(6\le n\le24\), and tests the complete triple rank-insertion walk space for every valid vertex. The integer results must match the 19 rows of `three_cycle_census.csv` exactly. Each row is also checked against the proved conversion between rooted closed three-walks and directed three-cycles.

The separate `direct_graph_check.py` directly constructs every permutation vertex and every labeled edge of the unrestricted graph for all \(3\le n\le8\), then evaluates the exact weighted adjacency-matrix trace of degree three. This independent method checks all six smaller orders, including the three orders common with the boundary census. A successful complete replay prints `BOUNDARY_RANK_CHECK_OK`, `DIRECT_GRAPH_CHECK_OK` and `VERIFY_OK`.

Scope of verification: finite integer enumeration, source-program replay, a mathematical proof of candidate completeness and exact edge accounting. The checks do not establish a closed formula for arbitrary order or certify priority in the historical literature. Independent scientific audit has not been performed.
