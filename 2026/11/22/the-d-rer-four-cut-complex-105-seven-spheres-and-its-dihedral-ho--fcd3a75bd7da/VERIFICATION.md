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

# Finite certificate and exact replay

`verify_durer.py` and `collapse_pairs.json` reconstruct the graph from the edge families, enumerate every subset, identify the disconnected quadruples, verify the closure and face-vector of the Alexander dual, and confirm that each listed pair is a genuine elementary collapse **at the instant it is removed**. There are 66 pairs and no remaining face above dimension two. No external Python packages are needed.

The verifier also enumerates signed, fixed simplices for twelve graph automorphisms. It verifies the six rotation traces and six reflection traces, each permutation's evenness, the resulting invariant rank eight, and the absence of six-vertex Alexander-dual faces. Its successful actual output is embedded as `verification_output.txt`.

The homotopy deductions are not delegated to software: the two-skeleton of the dual is simply connected, and the verified collapses preserve that property; the final two-complex has reduced Euler characteristic 105. Integral Hurewicz and Whitehead supply the dual sphere wedge, while integral combinatorial Alexander duality, the original complex's complete five-skeleton, and its seven-dimensional bound supply the original sphere wedge. Standard equivariant Alexander duality and the ambient even permutations transport the character.

The finite test covers the entire specified graph, but it does not validate similar formulas for other generalized Petersen graphs. Independent scientific validation has not been performed.
