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

# Reproduction and limits

With Python 3.9 or later execute `python3 icosa_forest_verify.py`. No external Python modules are required. The program reconstructs the labeled thirty-edge icosahedral graph, exhausts all \(4096\) possible vertex subsets, and checks two independent induced-forest predicates. It then constructs the deterministic staged-toggle discrete-Morse matching on all \(983\) nonempty faces and tests every one of the \(3972\) oriented Hasse incidences for directed cycles by a complete topological sort. The resulting forty critical four-cells and single critical vertex provide an integer homotopy certificate through Forman's theorem.

A separate mod-two simplicial boundary computation verifies the ordinary Betti vector \((1,0,0,0,40,0)\). Exhaustive adjacency-constrained graph automorphism backtracking yields a group of order \(120\). Two independent character calculations, one from signed oriented simplicial faces and one from automorphism-cycle unions, give identical traces for all group elements. The program verifies ten conjugacy classes, character average zero, inner product seventeen, and the projected \(A_5\) characters.

The script's complete standard output is embedded as `icosa_forest_verify.out`. Finite enumeration covers this particular graph and its full group only; neither the finite computations nor the review imply an infinite-family theorem, an integral irreducible module decomposition or external certification. Independent audit is not performed.
