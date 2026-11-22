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

# Verification and reproducibility

Execute `python verify_franklin_fourcut.py` using a standard Python 3 interpreter. No third-party packages, downloaded data or precomputed lookup tables are required. The script reconstructs the Franklin graph from the LCF recipe, enumerates all 495 quadruples and all 4096 vertex subsets, verifies both Alexander-dual descriptions and face vectors, and performs a deterministic sequence of 75 free-triangle/tetrahedron collapses. Each collapse is checked against every current face of the complex rather than just counting tetrahedral cofaces.

It separately enumerates all graph automorphisms from adjacency-preserving permutations, checks there are 48, computes oriented simplex chain traces on both the original complex and its Alexander dual, verifies their orientation-twisted correspondence, and independently groups the automorphisms into ten conjugacy classes. The weighted trace sum 144 gives an invariant rank of three. The last output line is `ALL EXACT TESTS PASSED`; the retained complete run transcript is `verification_output.txt`.

The finite program proves the exact face, collapse and character certificates for this single twelve-vertex graph. Homotopy conclusions also use the stated mathematical theorems: simple connectivity of the complete two-skeleton, elementary-collapse homotopy invariance, Hurewicz and Whitehead, and integral combinatorial Alexander duality. It does not sample an infinite graph family or prove a uniform classification, and it does not certify an equivariant homotopy splitting or integral representation decomposition.
