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

# Reproducibility and proof boundary

Use Python 3 with only the standard library. Execute `python check_direct.py` and `python check_structure.py` from the folder containing these files. Their expected stdout records are included as `check_direct.out` and `check_structure.out`. Each script contains assertion checks, and should finish with `DIRECT_CHECK_PASS` or `STRUCTURAL_CHECK_PASS` respectively.

The direct checker creates the complete triangular graph on all two-element subsets of \([n]\), computes full distance matrices by breadth-first search, and computes all shortest-path interval sets from the distances. It then exhausts every candidate below the proposed optimum cardinality, plus every candidate at that cardinality, for \(3\le n\le8\). For each optimum-sized subset, it independently compares the actual geodetic predicate with the min-degree/no-common-leaf predicate and checks exact counts.

The structure checker generates perfect matchings and both odd-order component types without using geodetic distances. It checks all generated configurations, classification-type and count formulas up to \(n=9\). It enumerates all one-token jumps and slides, degrees, edges and connected components for \(3\le n\le7\), and tests the predicted formulas.

Finite exhaustion is not an infinite-order certificate. The proof for all \(n\ge3\) uses the shortest-path criterion, connected-component excess analysis, counting, and an explicit three-slide transposition. Shortest-path computations are independent of the structural generator, while classification of all types for arbitrary \(n\) follows from the written proof.
