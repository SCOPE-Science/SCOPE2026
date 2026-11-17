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

# Reproducible verification

Execute `python verify.py` from the directory containing `requirements.txt` and the bundled source. Requires Python 3.10+ and SymPy 1.12+; the program uses exact integer and rational arithmetic. A successful run begins `K33_MULTIPATH_EQUIVARIANT_EXACT_PASS`. The stored `verification_output.txt` contains the actual stdout of a successful execution.

The program exhaustively checks the face predicate among all \(2^{18}\) arc sets and all face deletions. It computes the complete simplicial boundary ranks over \(\mathbb F_2\); builds \(336\) Morse pairs and checks that an acyclic directed graph contains all \(2376\) nonempty face incidences; carries out all integer unit-pivot Morse reductions; proves a unit maximal minor of the degree-three-to-two Morse matrix; and checks the other Morse differential vanishes. It independently constructs the original degree-four boundary matrix, computes a rational cycle basis using row reduction and derives its automorphism traces. It checks the action on every face for every group element, all class sizes, every signed Lefschetz trace, the entire irreducible character orthogonality table and both multiplicity decompositions.

The resulting character table, exact critical-cell masks, degree-three Morse matrix and group class data are recorded in the output. Those data and the standalone source are sufficient to reconstruct the proof of the fixed finite classification. As an exact finite proof it does not establish a general biclique family, any integral equivariant splitting, or the homotopy type of the quotient. Independent mathematical audit has not been performed.
