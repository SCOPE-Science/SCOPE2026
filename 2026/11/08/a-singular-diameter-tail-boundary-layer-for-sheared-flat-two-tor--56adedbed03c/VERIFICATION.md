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

# Computational and analytic verification

The primary argument is analytic: exact Voronoi inequalities, the cyclic-hexagon circumradius identity, circular-segment area subtraction, differentiation at the diameter, and a compact-uniform dominated-convergence argument. There is no discrete numerical certificate on which the general theorem depends.

Run `python3 check.py` using only Python 3 standard-library modules. The independent numerical implementation constructs Voronoi polygons as intersections of half-planes (rather than using the displayed vertex list), checks their unit area and vertex radii, and integrates the radial area in 32,000 independent angular bins for 20 combinations of five shears and four radii. It also compares analytic tail coefficients and tests twelve crossover approximations at several decreasing shears. The actual program returned `FLAT_TORUS_RADIAL_AREA_CYCLICITY_EXACT_TAIL_AND_CROSSOVER_OK 32`.

An additional 55-digit numerical evaluation checked the cancellation-sensitive crossover expression over six sample scales, with deviations consistent with an error of order of the shear. These tests do not prove the infinite limiting statements; the proof is in RESULT.md.

The main mathematical limitations are fixed positive shear for the quadratic tail, fixed crossover parameter for the zero-shear boundary layer, and two-dimensional Euclidean flat quotients of the explicitly specified lattice. A separate independent audit has not been performed.
