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

# Reproducibility

Run `python3 check_600cell.py` in a standard Python 3 interpreter. No network, external packages, floating-point comparisons, or third-party data files are required. All vertex coordinates and symmetry operators are generated from the explicit coordinate definition in the code. The checker enumerates all 120 vertices, a 14400-element symmetry group, all eight nonzero distance shells about a vertex, all 280840 unordered triples, all 56 symmetry orbits and distinct intrinsic Gram signatures, and the induced versus intrinsic automorphism groups of each orbit representative.

Expected terminal line:

`600_CELL_TRIPLES_PASS vertices=120 group=14400 two_point_shells=8 triangles=280840 orbits=56 distance_signatures=56 exceptional_orthogonal_orbit=2400 induced_C3=1`

`triangle_orbit_catalogue.csv` gives the 56 orbit representatives, with sorted inner-product signatures as pairs of integers representing elements of \(\mathbb Z[\varphi]\) for doubled coordinates. It also records orbit sizes, intrinsic isometry-group sizes, induced isometry-group sizes, and pointwise stabilizer sizes.

Finite exhaustive enumeration is valid for this fixed 120-point configuration. It makes no assertion about all regular polytopes, other dimensions, or perturbations. Independent mathematical auditing has not been performed.
