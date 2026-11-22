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

# Verification

The attached `verify.py` uses the standard Python 3 library and re-creates all finite certificate objects without importing external data. It uses lexicographic cube triangles/tetrahedra, checks a signed boundary matrix of size 56 by 38, finds exact rank 35 and a specified 35 by 35 minor with determinant -1, and checks all translated free-triangle/tetrahedron pairs in the *currently remaining* complex for each cycle length 6 through 13. All 36 cyclic template stages are included directly in that file, with no hidden data dependencies. The script also checks that no removed triangle belongs to a surviving cube block. `verification_output.txt` contains the actual completed execution trace ending in `TOROIDAL_FOUR_CUT_VERIFIED`.

The all-integer homotopy conclusion relies additionally on the written locality lemma, common-neighbor bound, relative homology and Whitehead argument in RESULT.md. The finite execution is not itself an infinite proof. No integral homotopy type of the original four-cut complex or equivariant splitting is asserted. No independent audit is represented as completed.
