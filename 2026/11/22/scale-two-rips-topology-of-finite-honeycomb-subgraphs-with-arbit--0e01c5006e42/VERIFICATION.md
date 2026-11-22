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

# Verification and reproducibility

Run `python3 verify_honeycomb.py` from the directory containing this file. It uses the Python standard library only and deterministically prints the exact content of `verification_output.txt` (apart from platform-specific line-ending conversion).

The verifier independently constructs finite patches of the bipartite honeycomb lattice, recomputes graph distances, enumerates all scale-two cliques, and checks the exact centered/hexagon exceptional-face classification. It tests 16 rectangular windows, 135 pseudorandom connected subgraphs obtained by bond and vertex deletion, and an internal shared-edge deletion with seven remaining hexagons and one persistent graph loop. It also checks full mod-two simplicial boundary ranks, not just Euler characteristic or facet totals.

The infinite-family proof is in `RESULT.md`. Its key noncomputational facts are uniqueness of midpoint for each distance-two pair, absence of four-cliques in either triangular color sublattice, the two CW attaching disks for each hexagon, and the collapsibility of a finite planar union of complete hexagonal faces to a graph. Mod-two finite checks cannot establish integral primitivity, homotopy equivalence or the theorem for all finite subgraphs; these are derived mathematically in the proof. No independent audit or validation is asserted.
