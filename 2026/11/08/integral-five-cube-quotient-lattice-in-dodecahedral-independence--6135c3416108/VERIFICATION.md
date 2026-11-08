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
# Exact reproducibility checks

The included `verify_dodecahedral_lattice.py` must be run with Python 3, NetworkX 3.x, and SymPy 1.x. The recorded output was obtained by running that file on the actual package path. It uses only exact integral/combinatorial operations and modular Gaussian elimination.

The script reconstructs the twenty-vertex thirty-edge graph; enumerates 5828 independent subsets and 27640 Hasse covers; certifies a directed acyclic matching and its five nonempty critical simplices; constructs four genuine integral fifth-homology cycles from those unmatched faces; checks integer projections, integral images of all 120 automorphisms, all 14400 multiplication identities, and independent fixed-simplex Lefschetz traces; verifies the five-maximum-octet action, its order-12 rotational stabilizer, the primitive invariant class, the five-column integral orbit matrix and its determinant minus one; confirms central inversion acts as negative identity; and tests distinct mod-five rotation coinvariants for the quotient and root lattices.

The computations cover this finite complex exhaustively; they do **not** prove a result for arbitrary cubic or generalized Petersen graphs. No external mathematical audit or expert certification has been conducted. Publication-priority assessment remains subject to the completeness of the literature search.
