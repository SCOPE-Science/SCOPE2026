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

# Verification of the exact finite claims

The graph vertices are exactly the 27 ternary triples, adjacent if and only if their Hamming distance equals one. A connected dominating configuration is a selected set whose closed-neighborhood union is the full 27-vertex set and whose induced graph is connected.

`verify_fast.cpp` completely enumerates subsets of cardinality four through eight, constructs all permitted moves, performs breadth-first search from each optimal state in the jump graph and from each vertex in each slide component, and asserts every claimed metric including all nine unordered-pair frequencies. The degree-six observation excludes cardinalities one through three. Its executable source, not merely `fast_output.txt`, is the exact certificate.

`verify_independent.py` regenerates the graph using a different coordinate order, independently enumerates the same 11,340 minima and both transition graphs, builds automorphisms from coordinate/symbol swaps and proves through actual orbit traversal that the 11,340 states occupy eleven orbits and the 504 slide components occupy four orbits. BFS on orbit representatives establishes jump eccentricity nine and the listed slide component diameters. Its executable source, not merely `independent_output.txt`, is an independent-implementation computational cross-check (not an independent external audit).

Run the two programs as documented under *Verification* in `RESULT.md`. Both were executed from their actual source paths and passed. An exact finite exhaustive search proves this specific labelled graph statement; no larger-family extrapolation, external code certificate, or independent external audit is claimed. The remaining risks concern unindexed priority and generalization, not incomplete state enumeration.
