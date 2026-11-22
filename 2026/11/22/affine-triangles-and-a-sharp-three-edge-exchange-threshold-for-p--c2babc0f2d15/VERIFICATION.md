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

# Verification record

Both standalone source programs `verify_affine.py` and `verify_lcf.py` were executed directly from the package directory with Python 3. The affine program used a first-free-vertex exhaustive recursion to enumerate all maximal matchings; its mathematical invariant is that leaving two adjacent vertices unmatched would prevent maximality. The independent LCF program enumerated uncovered independent pairs on the two shores and their complementary perfect matchings, using a graph constructed from an independent Hamiltonian cyclic representation. They agree on the minimum and full distance profile.

The full cardinality count is \(36z^6+567z^7+648z^8+42z^9\). The two lower exchange budgets leave 36 isolated configurations; the three-edge exchange graph has 36 vertices, 126 edges, degree seven, 108 triangles and identical distance shells \((1,7,12,12,4)\) from every state. The affine program also checks 108 line-class-preserving affine automorphisms and transitivity on all 36 optima. Both programs enumerate finite sets exhaustively; neither makes claims about all graph orders or uses numerical experimentation to infer an infinite assertion.

The verification programs need no third-party packages or network access. Included output files are references for reproduction, not replacements for code and the mathematical justification. No independent external evaluation has been undertaken.
