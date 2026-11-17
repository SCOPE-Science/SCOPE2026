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

Run `python check_radial_simplex.py` with the required NumPy dependency. The checker constructs independent Euclidean simplex coordinates, solves linear equations for the circumcenter and barycentric coordinates, and compares them against the closed-form expressions. The numerical checks cover 10,500 independently generated radius tuples in dimensions 2–8, 70,000 additional fixed-ratio inequality tests, exact equality families, and one example realizing each permissible number of negative coordinates. Output marker: `RADIAL_SIMPLEX_PREFIX_SHARP_BOUND_OK`.

The mathematical proof is analytic and holds for all integer dimensions at least two and all positive radii. Finite calculations are sanity checks only; the exact positivity and sharpness conclusions rely on the inequalities in `RESULT.md`. Originality comparisons were conducted against the cited literature and mathematical records; no independent human audit or complete all-publisher historical search has been performed.
