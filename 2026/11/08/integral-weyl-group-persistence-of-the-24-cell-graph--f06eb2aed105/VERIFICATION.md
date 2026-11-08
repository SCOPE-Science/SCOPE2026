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
# Reproducible checks

The exact computation is contained in `verify.py`, with its original `verification_output.txt`. Run `python3 verify.py` using Python 3.13.5, NetworkX 3.6.1, and SymPy 1.14.0. It enumerates all 276 pairs of 24 roots, the 96 edges and 96 triangles of the radius-one flag complex, all 24 octahedral facets and their incidences, the rank-73 triangle boundary over the field of two elements, the reflection-generated 1152-element symmetry group, and an independent full graph-automorphism enumeration. It computes and checks the complete degree-two and degree-eleven trace distributions and the average invariant multiplicities. Expected terminal marker: `TWENTYFOUR_CELL_EQUIVARIANT_RIPS_PASS`.

The topology and integral module proof relies on the geometric identification of the radius-one complex with the two-skeleton of the convex 24-cell boundary and on the integral cellular exact sequence, plus the antipodal cross-polytope decomposition at radius two. Mod-two matrix ranks alone would not certify an integral result. The degree-eleven orientation representation is separately checked on four Coxeter generators and all group elements. No independent audit has been conducted.
