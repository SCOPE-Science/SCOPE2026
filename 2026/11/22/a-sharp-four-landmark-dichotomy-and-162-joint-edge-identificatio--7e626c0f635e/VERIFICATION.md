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

# Exact finite verification

The claim concerns the ten-vertex Petersen graph, so all vertex subsets can be enumerated without a numerical approximation. Two different graph constructions are independently implemented.

## Kneser-coordinate verifier

Run `python3 census_symbolic.py`. It constructs all ten unordered two-subsets of five ground labels, all fifteen disjoint-pair graph edges and exact edge distances in \(\{0,1,2\}\). It checks the pairwise uniqueness of fifteen edge-signature vectors and checks coverage for all \(1024\) landmark subsets. It independently constructs the \(120\) ground-label permutations and exhausts six orbits of four-sets and six orbits of five-sets. The output matches `symbolic_output.txt` and ends in `PET_X5_SYMBOLIC_OK`. The four-set orbit sizes add to \(210\); the five-set sizes add to \(252\), with exactly four qualifying five-set types.

## Independent Petersen/BFS verifier

Run `g++ -std=c++17 -O2 census_bfs.cpp -o census_bfs && ./census_bfs`. The second implementation builds the outer pentagon, spokes and inner pentagram of \(GP(5,2)\) rather than using the two-subset distance formula. It computes every vertex distance by breadth-first search and asserts the exact coefficient array of each of the three counting polynomials over all \(1024\) subsets. Its output matches `bfs_output.txt` and ends in `PET_X5_BFS_OK`.

## Exact expected totals

The edge-resolving cardinality counts at sizes four through ten are \(15,162,195,120,45,10,1\). Vertex–edge dominating counts at sizes three through ten are \(60,195,252,210,120,45,10,1\). Joint feasible counts at sizes five through ten are \(162,195,120,45,10,1\). Both implementations completed these tests successfully.

## Limits

The computations are exhaustive for the Petersen graph but say nothing automatically about arbitrary orders of generalized Petersen graphs. The two programs are independent finite implementations, not independent external audits. External publication priority remains provisional.
