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

Run `python3 verify.py` using a Python 3 standard-library installation. The program performs 256 deterministic assertions and reports the four-vertex witness's area, boundary, and Steiner centroids together with its numerical unique positive radius.

The program verifies (1) exact rational enclosures of the strict witness inequalities using classical rational bounds on \(\pi\) and the alternating arctangent series; (2) independent shoelace, edge-midpoint, and exterior-turning-angle center computations; (3) direct first-moment reconstruction for outer-parallel polygons by disjoint edge strips and circular corner sectors, not only reuse of the centroid polynomial; (4) existence, sign change, and root stability for multiple unequal-base trapezoids; and (5) the predicted linear onset slope for six unrelated base ratios and three decreasing height gaps each.

The infinite-domain statements depend on the detailed algebraic and analytic proof in `RESULT.md`: positivity and strict monotonicity of the coefficient ratio, sine-graph triangle rigidity, the strict \(\arcsin z/z\) inequality, and a first-order expansion at the critical height. Floating-point tests do **not** establish infinity-wide uniqueness, historical originality, or priority. The results apply to Euclidean outer parallels in the plane only. Independent audit is not performed.
