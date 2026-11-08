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

# Verification record

The theorem's infinite-domain statements have an analytic proof in `RESULT.md`: (1) inward offsets of Euclidean unit-normal halfspaces describe all admissible ball centers; (2) the Hausdorff error of a convex opening is determined by vertices; (3) the local tangent-cone quadratic program controls those vertex distances globally below and exactly for sufficiently small radius; (4) an inset planar angle contributes \(\csc(\theta/2)-1\); (5) angle sum gives the sharp side-count bound, attained at every radius by a regular polygon; and (6) elementary inversion and angle summation give the global angular stability estimate. No finite experiment is used to infer an infinite quantifier.

To reproduce supplementary numerical checks, run `python3 opening_verify.py` with Python 3, NumPy and SciPy. The program uses exact geometric definitions and floating-point clipping, segment-distance, and linear-programming routines. Its completed run printed:

`OPENING_GEOMETRY_NUMERIC_OK 220 random convex polygons x 2 radii; 112 regular-polygon radii; 16 rectangle radii`

The checks probe 440 radius choices on randomly generated convex polygons, 112 choices on regular polygons of 3–18 sides, and 16 on four rectangles. Floating-point tolerances are specified in the code; these checks are not formal mathematical certificates and do not establish completeness for any infinite family.

Limits: the local equality threshold is polygon-dependent; for arbitrary nonregular polygons the global bound can be strict at larger radii. Historical priority is provisional. No independent mathematical review has been carried out.
