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

Run `python verify_ternary_symmetry.py` with Python 3.10 or later from the directory containing the attached file. No dependencies beyond the standard library, external datasets, or network access are needed.

The script generates all 5,950 simplices including the empty simplex directly from the 27-vertex forbidden-pair relation. It then matches 2,951 pairs and checks acyclicity by topological sorting the entire oriented face-poset Hasse graph with 27,216 incidences. Exactly one critical vertex and 46 critical three-simplices remain. This certifies a wedge of 46 three-spheres by discrete Morse theory.

The script independently calculates each of the 22 group-character values by two mechanisms: signed fixed simplex chains and signed independent-set evaluation of admissible vertex-orbit selections. It checks the complete group of 1,296 elements, the 22 class sizes, the character orthogonality matrix and multiplicity extraction. It confirms seven irreducibles with multiplicity one, dimensions 8, 12, 6, 1, 12, 6, 1, and no trivial constituent.

`verification_output.txt` records the actual successful run, including all 22 conjugacy class traces. This finite certificate does not claim results for arbitrary alphabet sizes or Hamming dimensions. The review is not an external or independent audit.
