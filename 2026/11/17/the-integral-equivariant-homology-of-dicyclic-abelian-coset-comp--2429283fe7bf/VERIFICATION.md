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
# Verification and limits

The executable `verify.py` enumerates all elements of the dicyclic group, the maximal abelian cosets, every central-coset facet of the associated nerve, and all nerve faces for each \(2\le n\le7\). It compares the exact f-vector with the closed binomial count and checks Euler characteristic and the predicted homology rank. It then computes every left-translation action on the maximal-coset set, verifies all central and noncentral fixed-coset counts and the resulting signed trace formulas, and confirms the separate transitive orbits of small-coset types. All executed assertions succeeded (see `verify_output.txt`).

The uniform proof of the integral module uses a \(G\)-equivariant nerve equivalence and an explicit equivariant strong deformation retraction of the nerve, so it applies beyond the tested range. The checker does not independently prove the equivariant nerve lemma, the general collapse, or a complete literature novelty claim. The nonequivariant wedge rank is credited to the 2023 reference.
