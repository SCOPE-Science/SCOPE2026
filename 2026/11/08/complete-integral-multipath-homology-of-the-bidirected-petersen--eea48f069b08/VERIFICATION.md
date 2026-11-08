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

# Computational verification

Run `python3 verify_petersen_multipath.py`. No third-party packages or external data are required. All graph vertices, arcs, simplicial faces, matching pairs and integral matrices are reconstructed from the graph definition rather than loaded from a precomputed output. The script ends with the marker `PETERSEN_BIDIRECTED_MULTIPATH_INTEGRAL_HOMOLOGY_PASS` only after all assertions pass.

The verification includes two independent complete face enumerators; full Hasse-graph acyclicity tests in two opposed coordinate orders; signed integral Morse boundary construction from local incidence projections; verification of every consecutive boundary composition; and exact integer row/column elimination using only unimodular operations and unit pivots. The resulting zero residual matrices prove that each boundary has Smith invariant factors only zero and one. An unreduced mod-two boundary computation supplies an independent cross-check of the Betti vector, and the face vector independently determines the Euler characteristic.

The calculations verify the precise finite statement for the bidirected Petersen graph. Mod-two agreement alone is not used to infer integral torsion-freeness; that follows from the integral unit-pivot reductions. The script does not compute the full homotopy type and makes no statement about arbitrary digraphs.
