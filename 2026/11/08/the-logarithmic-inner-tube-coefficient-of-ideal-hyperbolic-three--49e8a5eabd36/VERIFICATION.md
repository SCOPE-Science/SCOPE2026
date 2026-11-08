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

# Verification notes

The proof in `RESULT.md` is analytic. It reduces the hyperbolic cusp to a fixed Euclidean convex polygon in horospherical coordinates and integrates the exact initial inner-offset area polynomial. The claimed asymptotic remainder follows from the bounded tail integral and a finite compact polyhedral decomposition.

For a computational cross-check, run `python check_cusp_tube.py` with Python 3 and SciPy available. The program independently clips inward-shifted polygon half-spaces to compute eroded cross sections of equilateral triangular and square vertex figures. It compares those results with Euclidean tube coefficients and then numerically integrates the actual hyperbolic cusp formula at multiple positive distances. It additionally tests the tetrahedral angle and volume inequalities on a finite grid of admissible angle triples. Expected final marker: `IDEAL_HYPERBOLIC_POLYHEDRON_LOG_TUBE_OK`.

The finite tests neither exhaust all cusp polygons nor certify an asymptotic uniformly in degenerating polyhedron shape. The geometric proof handles the quantified fixed-polyhedron statement. Historical priority has not been independently validated. Koçak–Ratiu’s full arXiv text was examined in an accessible extraction, including its Euclidean planar inner-tube formula and statements explicitly limited to Euclidean polytopes.
