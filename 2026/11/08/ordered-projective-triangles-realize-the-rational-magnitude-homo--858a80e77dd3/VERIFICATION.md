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

# Reproducibility and verification

Execute the two included standard-library Python programs in this order, in the same directory:

`python verify_ternary_pg_mh.py`

`python pg_mh_symmetry.py`

`CHECK_OUTPUT.txt` includes the actual output from this run. The integral program checks 26 equal-endpoint and 312 distance-two endpoint blocks, each signed boundary and all successive boundary compositions; integer row/column operations find only unit pivots. The character program enumerates 5616 normalized invertible projective matrices, determines their graph automorphisms, and compares their homology Euler–Poincaré trace to the separately enumerated ordered-projective-triangle permutation trace. It checks 117 involutions, six fixed-point profiles and the invariant multiplicity. The swapped point-line coset is handled by a structural zero-trace argument and is not explicitly iterated as 5616 additional permutations.

The computation establishes the rational representation isomorphism for PG(2,3), using the published girth-six diagonal magnitude rank. It does not give an integral equivariant basis, extrapolate to arbitrary field orders, or constitute an independent external audit.
