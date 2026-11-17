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

Run `python3 verify_dodecahedral_symmetry.py` in this package, using only Python 3 standard library. The program builds the explicit \(GP(10,2)\) graph, enumerates all independent sets, computes the full augmented mod-two chain ranks, and exhaustively determines the graph automorphisms by backtracking constrained by both adjacency and nonadjacency. It constructs all five independent eight-sets, the action on them, their central antipode, the derived subgroup, the ten conjugacy classes, and the signed simplicial traces. Independently, it evaluates the independent-set polynomial at \(-1\) on the graph of admissible vertex orbits for every automorphism. The two trace computations must agree for all group elements. It also checks irreducible-character norms and rational invariant dimensions for five subgroups.

The actual executable output is embedded as `verification_output.txt`. Its final success marker is `DODECAHEDRAL_CUBE_AUGMENTATION_CHARACTER_PASS`. The proof of rational homology concentration uses the mod-two upper bounds plus the integral Euler characteristic, rather than incorrectly promoting finite-field rank equality to an integral Smith normal form. The ordinary-quotient cohomology step uses exactness of rational invariants after barycentric subdivision. Neither the verifier nor the proof classifies integral quotient torsion, provides an equivariant homotopy equivalence, or constitutes independent mathematical auditing.
