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

# Reproducibility and exact verification

Graph: the \(24\) vertices \((j,r)\) of \(C_3\square C_8\) have ID \(3j+r\); each vertex has two triangle-neighbors and two cycle-neighbors.

Execute the supplied programs directly:

```sh
c++ -std=c++17 -O2 verify_torus_bfs.cpp -o torus_bfs
./torus_bfs
python3 verify_torus_geodesic.py
```

The C++ output must be byte-for-byte the supplied `bfs_results.txt`, and Python output must equal `geodesic_results.txt`. Their common coefficient table is:

```text
size feasible maximal
0 1 0
1 24 0
2 276 0
3 1952 0
4 8808 0
5 24720 0
6 40256 0
7 33000 4608
8 9960 4656
9 928 928
total_feasible 119925
total_maximal 10192
```

The Python program prints three additional explicit examples, one each of cardinalities seven, eight, and nine. In particular the seven-set with IDs `[0, 1, 2, 3, 12, 13, 14]` is feasible and has no feasible one-vertex extension.

**Why exhaustive:** The recursively generated search only prunes when a set is no longer mutually visible, a hereditary property. Every feasible set is uniquely reached by its increasing vertex order. The predicate checks every selected pair against *all* its shortest paths, and maximality checks every possible one-vertex addition. The Python route generates all geodesics by cycle-arc interleavings; the C++ route generates them independently by graph-distance descent. These are two distinct implementations of one fully specified finite theorem. No timeout, probabilistic search, approximate arithmetic, or assumed cutoff enters the claim.

**Limits:** The verification proves a finite graph statement, not a formula for larger even circumferences. The agreement of programs is not an independent external audit. The maximal cardinality nine was already available in the primary literature and is credited in RESULT.md.
