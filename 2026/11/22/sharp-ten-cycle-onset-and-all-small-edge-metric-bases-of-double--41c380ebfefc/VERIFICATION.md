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

# Finite verification

The included C++17 code and Python 3 code explicitly define all \(4n\) vertices and \(6n\) edges for every \(n=3,\ldots,12\). For each such graph, they test *all* unordered vertex subsets of sizes 2, 3 and 4, comparing the distance-signature of each edge. The C++ program computes shortest paths with BFS and tests edge-pair collisions; the Python program uses Floyd–Warshall and tests complete-signature uniqueness. Both emit the exact same TSV: `bfs_output.tsv` and `floyd_output.tsv`. These are independently implemented finite certificates, not random samples.

A further Python program, `verify_independent.py`, lists an explicit first witness at each order and verifies its counts against `verify_py.out`. The third Python program repeats the \(n=10\) graph construction, obtains precisely 160 resolving triples and partitions them into six generated-automorphism orbits of sizes 20, 20, 20, 20, 40, 40. `orbit_output.txt` records the exact representatives.

To reproduce: compile `check_bfs.cpp` with `g++ -std=c++17 -O2 check_bfs.cpp -o check_bfs`; run `./check_bfs`, `python3 check_floyd.py`, `python3 check_orbits.py`, and compare their stdout to the three bundled files. Python requires the standard library only. The excluded case \(n=6\), the first three-resolver case \(n=10\), and each four-set count are checked explicitly.

The published theorem for \(n\ge13\) is cited rather than independently regenerated; finite checks are not extrapolated to arbitrarily large graphs. No independent external mathematical audit has occurred.
