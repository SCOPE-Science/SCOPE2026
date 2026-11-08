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

# Reproducibility and scope

Run `python3 verify.py` without third-party Python packages. The program recomputes the entire face poset (746 nonempty faces) from two mathematically equivalent descriptions, the full deterministic 370-pair matching, all 2580 directed Hasse covering relations, and a complete topological sorting certifying no directed cycle. The six critical face masks are exactly `1,5664,10784,19488,28736,29184` (one zero-cell and five three-cells). The program separately computes mod-two boundary ranks `14,91,169,81,15` and reduced Betti vector `0,0,0,5,0,0`.

The integral homotopy conclusion uses the fully checked acyclic matching and Forman's theorem; it is not inferred from a field-valued homology computation. The computation is exhaustive for exactly fifteen labeled graph vertices. It is not an infinite-family proof and does not establish a simplicial homeomorphism, equivariant decomposition or independent certification.
