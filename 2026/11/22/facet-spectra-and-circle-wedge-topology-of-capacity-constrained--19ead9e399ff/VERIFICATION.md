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

Run `python verify_supertoken.py` using Python 3 with NetworkX installed. The checker constructs all valid labelled placements, generates the single-coordinate transition graph, enumerates maximal cliques, independently counts partial assignments, evaluates the factorial-coefficient formulas exactly using rational numbers, checks graph connectivity, the clique-polynomial Euler characteristic, and the facet-purity threshold. The completed execution returned `TESTED_INSTANCES 45 VERIFY_OK`. It includes three-site two-capacity examples with 54 vertices and facet sizes two and three, and with 90 vertices and only edge facets. The full-capacity boundary is verified as a collection of isolated vertices where small enough.

These finite checks are not infinite proofs, nor do they compute an independent homology certificate. The topological conclusion follows from the proof that all maximal simplices intersect in at most one vertex, enabling a simplicial deformation retraction to the connected incidence graph. All mathematical statements are restricted to the parameter domain in `RESULT.md`.
