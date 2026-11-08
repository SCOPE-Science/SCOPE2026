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

# Computational reproduction

The exact claim and the graph conventions are given in `RESULT.md`. Run `python3 verification/verify.py` from the package root using Python 3; only standard-library modules are imported. The verifier independently enumerates all independent faces (recursive bitmask construction versus a three-layer placement construction), constructs every matched pair from the fixed pivot list, and checks that reversing matched arrows in the complete oriented nonempty-face Hasse diagram creates no directed cycle. This finite exhaustive check establishes the discrete-Morse hypothesis; the homotopy conclusion then follows by the stated standard topological theorem.

The observed output in `verification/observed_output.txt` was produced by running this code. The code checks 11,776 faces (including the empty face), 5,868 ordinary pairs, 39 ordinary critical cells, 56,592 oriented covering relations, 11,775 vertices visited by topological sort, and an independent full-complex mod-two chain reduction. Mod-two homology checks alone would be insufficient to establish integral homotopy, so they serve only as corroboration.

# Boundaries

The calculation makes no assertion for other Hamming parameters, no graph-automorphism-equivariant claim, and no claim that this complex is simplicially homeomorphic to a wedge. Its novelty has been assessed against accessible literature, not independently certified.
