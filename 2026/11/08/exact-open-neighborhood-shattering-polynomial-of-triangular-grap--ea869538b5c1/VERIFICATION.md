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

# Verification of the triangular-graph census

The executable `verify.py` uses only Python 3 standard-library modules. Run `python3 verify.py` from the extracted package directory. It produces a sequence of `MOTIFS` and `DIRECT` records and terminates with `ALL_OPEN_TRIANGULAR_GRAPH_CHECKS_PASS 26 five-edge motifs, 2..12 motif counts, 2..10 labelled graphs`.

The graph-generation routine adds one edge and zero, one, or two new vertices to an existing no-isolates graph. Removing any edge and pruning newly isolated endpoints proves this generates every isomorphism type; the asserted type counts by edge number are \(1,2,5,11,26\). The degree-constrained isomorphism routine tests all adjacency-preserving assignments. For each type, the certificate computes the exact set of two-vertex cuts with zero, one, and two available external vertices. By the proof's two-fresh-vertex lemma, this checks *all possible ambient orders*. It finds no shattered five-edge graph and exactly the ten listed types of smaller size.

The code independently enumerates the labelled concept family in \(J(n,2)\) and checks every support of size at most four for \(2\le n\le10\). It also checks the automorphism-weighted motif count for \(2\le n\le12\). The tests agree with the explicit formula, including the exceptional small orders.

No proof extends from arbitrary finite sample testing: the universal scope is justified by the cut identity, exhaustive type recursion through five edges, and hereditary nonshattering. Exhaustive software execution is reproducible but does not constitute an independent audit; possible software faults or overlooked earlier literature are residual risks.
