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

# Reproducibility and claim-to-evidence

Run `python3 verify_prism_bits.py` and `python3 verify_truncated_graph.py` using the two complete standalone scripts supplied beside this document; both require only the Python 3 standard library.

`verify_prism_bits.py` enumerated all \(2^{n+1}\) binary-word states for each \(3\le n\le11\), built every transition from the exact permitted face rules, checked reciprocal moves, exhaustively traversed all components, matched their complete memberships to the proposed fixed-core decomposition, checked every predicted independent-set component cardinality, and compared the recurrence, largest-sector order, and frozen formula. All assertions passed.

`verify_truncated_graph.py` independently constructed the actual \(6n\)-vertex, \(9n\)-edge truncated graphs for \(3\le n\le7\). It enumerated every graph-theoretic perfect matching by backtracking, expanded every geometrical polygonal face into its \(2k\)-cycle of new vertices, verified alternating matches, built all physical face-flip transitions, checked their reversibility, and traversed all resulting sectors. Each result agreed with the theorem. In particular, the truncated cube has exactly 32 matchings, 12 face-flip edges, 23 components, largest component size 10 and 22 frozen matchings.

The all-circumference proof is symbolic: the odd-subgraph correspondence, explicit edge-parity coordinates, exact flip criterion, invariant-core connectivity, transfer-matrix recurrence and Laplacian quadratic form are proved in `RESULT.md`. Exhaustive tests only cover the explicitly stated finite ranges. A finite numerical run is not evidence of an arbitrary-size or infinite-system theorem; no arbitrary-size claim depends on such extrapolation.

No external independent audit has been performed; no data were supplied for external verification channels. Historical priority is based on the explicitly documented literature and record comparisons, not a guarantee that no other equivalent formulation exists.
