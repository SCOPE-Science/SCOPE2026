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

The standalone `verify_fcc_sections.py` runs using Python 3's standard library only. On the package's own code, execution produced

`VERIFY_OK vertices=14 facets=12 edges=24 exact_symmetry_cases=96 spherical_regions=32 hexagon_regions=8 octagon_regions=24 sampled_normals=240000 observed_hexagon=0.351720833 formula_hexagon=0.350959312 error=0.000761521`

The verifier exhaustively enumerates feasible intersections of triples of the twelve supporting planes, confirming the complete fourteen-vertex list; then reconstructs the twelve facets by exact integral inequalities on doubled-integer vertices and derives all twenty-four edges by facet-pair intersections; verifies ninety-six sign/crossing cases spanning the signed-permutation symmetry types; and checks the spherical areas and normalization analytically using standard trigonometric functions. The final random sample of 240,000 directions tests implementation consistency only. Its tolerance does not establish the theorem. The written proof covers every generic direction by signed coordinate permutations, continuity on ordering-equality walls that are not sign walls, a four-region partition of every octant, and Girard's spherical excess. No claims are made for noncentral or nonuniform-offset sections. Independent audit: not performed.
