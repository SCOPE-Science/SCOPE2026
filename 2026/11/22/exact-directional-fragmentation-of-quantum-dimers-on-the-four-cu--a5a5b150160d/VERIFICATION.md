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

# Verification

Run `python3 verify_directional_plaquettes.py` (standard-library Python 3). The exact output begins `VERIFY_OK matchings=272 faces=24 labeled_repertoires=64 symmetry_types=11 all_full_6_only=TRUE`. The verifier independently enumerates every 272-state perfect-matching configuration in two orders and representations, checks all 24 coordinate squares, and independently computes the 64 component multisets by adjacency BFS and explicit-edge-set DSU. It asserts every eleven-class component spectrum and class multiplicity, the fully isotropic 264-plus-eight decomposition, and the 198-plus-32-plus-32-plus-ten-singletons fragmentation under each one-orientation deletion.

The ground-space statement needs no numeric spectral diagonalization: the RK Hamiltonian is a nonnegative weighted flip-graph Laplacian, so its kernel dimension equals the number of connected components for strictly positive enabled weights. The finite algorithm covers *all* states and all 64 move policies. It does not validate analogous phenomena in higher dimensions, non-square transitions, nonzero spectral gaps, or an independent scientific review.
