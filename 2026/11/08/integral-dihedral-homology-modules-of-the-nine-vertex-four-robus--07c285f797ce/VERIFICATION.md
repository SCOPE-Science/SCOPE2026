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

Use the standard Python interpreter, version 3.8 or later, to run `python3 verify.py`. The script has no nonstandard dependencies. It regenerates the grid graph from Manhattan adjacency, enumerates all independent four-sets and all simplicial faces, independently checks every face using bipartite maximum matchings, builds an explicit 192-pair discrete-Morse matching, verifies 1544 oriented Hasse incidences and absence of directed cycles, and prints every critical face.

For all eight dihedral symmetries it computes signed simplicial-chain traces and the induced rational homology character, then compares with the determinant twist of the unit-square permutation character. It also independently reconstructs the Alexander dual, checks its full face vector and mod-two Betti ranks, and computes its eight first-homology traces directly. All comparisons are complete finite calculations on masks of nine vertices.

A successful replay ends with `ALL_VERIFY_OK` and reproduces `verify_output.txt`. The homotopy equivalence relies on the acyclic-matching theorem; the integral representation equivalence relies on the explicit unimodular basis and equivariant Alexander duality; the rational characters are extra checks. These standard structural deductions are written explicitly in `RESULT.md` and are not claimed to be the output of an independent audit. The prior numerical homology rank was already published; checking it here is a consistency test only.
