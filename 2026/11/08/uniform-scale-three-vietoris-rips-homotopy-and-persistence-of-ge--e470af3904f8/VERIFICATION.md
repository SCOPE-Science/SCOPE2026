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

# Reproduction and evidence limits
Run `python verify.py` with the Python standard library. The test constructs projective points of symplectic 4-space over the prime fields of orders two and three, enumerates totally isotropic projective lines and their incidence graph, and exhaustively rebuilds all graph distances by breadth-first search. It verifies that all cross-colour pairs have distance one or three; all same-colour pairs have distance two or four. For each side of the scale-three join it enumerates every clique, confirms that maximal cliques coincide with line/pencil blocks, constructs root-star face pairs, topologically sorts the oriented face-poset Hasse diagram, and independently computes mod-two reduced homology. It repeats the matching/acyclicity/homology checks on the full scale-two complex.

For order two the program verifies 15 points and 15 lines, each join factor having 75 nonempty simplices and 135 covering incidences, 15 matched pairs and reduced degree-one rank 16; the scale-two complex has 315 simplices and 750 covering incidences and has reduced degree-one rank 16. For order three it verifies 40 points and 40 lines, each factor having 480 simplices and 1120 incidences, 160 matched pairs and reduced degree-one rank 81; the scale-two complex has 2000 simplices and 5680 incidences and degree-one rank 81. The proof then implies scale-three ranks 256 and 6561 respectively. See `verification_output.txt` for the exact executable transcript.

The proof's universal quantifier rests on the generalized-quadrangle axioms, the stated graph-power collapse theorem and exact simplicial collapses in both join factors. The finite computations do not establish the universal claim, do not directly enumerate the full radius-three complexes (especially at order three), do not certify originality, and do not constitute an independent audit. The submitted files include no third-party papers.
