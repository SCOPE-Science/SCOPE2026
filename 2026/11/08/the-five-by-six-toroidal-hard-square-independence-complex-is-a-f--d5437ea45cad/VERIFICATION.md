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

# Finite verification of the five-by-six toroidal independence complex

Run `python3 verify.py` with a standard Python 3 interpreter. The source has no dependencies beyond the Python standard library. Its stdout must match `verification_output.txt` exactly.

The program checks symmetric degree-four periodic Cartesian grid adjacency; compares independent full face enumeration by vertex extension with a structurally independent five-cyclic-row pattern enumeration; checks every distinct discrete-Morse matching pair; constructs all 1,347,900 Hasse cover relations and verifies that reversing the matched cover directions yields an acyclic digraph by exhaustive sorting of all 199,821 faces. The empty simplex is included and matched. The sole unmatched simplex mask and dimensions appear in recorded output. The finite verification is specific to one graph, not a general theorem about toroidal grids.

The inference to the claimed CW type is by augmented discrete-Morse theory: matching the empty face and leaving one critical five-simplex yields a pointed CW complex with a basepoint and one five-cell, necessarily a five-sphere.

Independent mathematical audit was not performed. The uninspected full text of a directly relevant 2010 paper remains an originality limitation, not an unverified correctness assumption.
