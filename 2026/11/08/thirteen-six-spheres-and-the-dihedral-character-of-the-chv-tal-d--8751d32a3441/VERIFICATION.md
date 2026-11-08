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

The exact finite statement is reproduced by `python verify_chvatal_dominance.py` with the standard Python library and no nonlocal data or modules. The output in `verification_output.txt` was recorded from this same supplied standalone program.

The two face predicates are compared on each of the \(2^{12}\) subsets. The code counts 3098 nonempty faces in dimensions zero through seven, constructs 1542 deterministic Morse pairs, confirms the critical dimensions \(0\) and \(6\) only, and fully topologically sorts the oriented 16,648 face-poset covering relations. The acyclic-matching theorem proves the **integral homotopy** result. Separate boundary elimination modulo two recovers reduced Betti number thirteen in dimension six, but does not purport to establish integral homotopy by itself.

The code also checks all candidate automorphism extensions through an exhaustive adjacency-and-nonadjacency backtracking tree, verifying that precisely eight automorphisms exist and that the explicit quarter-turn and reflection generate them. For each group element it computes the exact reduced signed fixed-face Lefschetz number, including the empty-face contribution, and confirms all four one-dimensional and one standard two-dimensional rational representation multiplicities.

The scope is **one specified finite graph**; verification does not imply an infinite family, a canonical integral irreducible decomposition, or an equivariant homotopy splitting. The arithmetic and discrete-Morse implementation have been replayed locally; an independent mathematical audit has not been performed.
