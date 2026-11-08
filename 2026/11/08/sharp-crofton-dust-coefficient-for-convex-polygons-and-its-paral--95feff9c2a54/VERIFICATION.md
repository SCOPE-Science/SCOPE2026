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

Run the accompanying standalone `verify_crofton.py` with Python, NumPy, and SciPy. The script evaluates the corner integral both numerically and against the Beta-function special case for a square. It directly clips convex polygons by halfplanes and integrates over line normals to obtain the **finite-\(\varepsilon\)** smaller-cap probability, independently of the local asymptotic corner calculation. The tested polygons include a square, a skew rhombus, an equilateral triangle, and a regular octagon; it checks the coefficient as \(\varepsilon\) decreases. It also evaluates regular orders 20, 50, 100, 400 and 1600 and a sequence of thinning rhombi.

The proof itself is contained in `RESULT.md`, including the uniform-dominating disk argument, the exact normalization, the AM-GM strict inequality, and the sharpness sequence. Computation confirms finite cases and limiting trends; it cannot certify the all-polygon limit or rule out unknown prior publications. Historical comparison includes full accessible text of arXiv:1404.6106 and arXiv:1204.2707. The 2011 predecessor arXiv:1109.2006 was identified bibliographically but not inspected in full.
