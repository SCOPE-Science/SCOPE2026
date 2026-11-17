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

# Reproducibility and limits

Run `python3 verify_m7_rotation.py` using the Python standard library. The program reconstructs all simplices from the lexicographically ordered edges of the seven-vertex complete graph, computes their sevenfold orbits and orientation signs, and builds the quotient cellular boundaries. It checks the boundary composition, rational and modular ranks and a primitive spanning-tree minor. The triangle attaching-word list is independently preserved in `cell_presentation.txt`.

The program contracts the tree, solves twelve single-occurrence relators over the noncommutative free group, substitutes with free reduction, and prints the remaining relator powers. The certificate establishes cyclic order twenty-one, not merely its Smith-normal-form abelianization. All integer homology groups then follow by Hurewicz, the two-dimensional cellular chain complex, and Euler characteristic. The recorded execution is `verification_output.txt`.

Checks have finite, exhaustive domains: twenty-one graph edges, 231 nonempty simplices, and quotient cell counts 3, 15 and 15. The checker establishes the particular finite presentation and its exact equivalence by Tietze moves. It does not prove publication priority, classify integral cohomology operations, or calculate a complete homotopy decomposition. Independent mathematical validation has not been performed.
