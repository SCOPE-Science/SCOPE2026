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

The stand-alone `verify_brightness.py` uses NumPy and SciPy. It builds all \(24\) signed-permutation vertices of \((1,t,0)\), projects those 3D vertices to independently constructed orthonormal 2D bases, evaluates convex-hull areas, and checks the analytic directional formula and both extremum bounds. The script tested \(3344\) directions across \(11\) parameter values, including the two algebraic thresholds, the equal-area member, and near-endpoint shapes. It explicitly checked predicted extreme rays and the published regular truncated-octahedron normalization, and reported `INDEPENDENT_PROJECTED_HULL_CHECKS_OK 3344`.

The proof's key exact identities, not inferred from the finite tests, are: six axial facet areas \(p=2t^2\); eight diagonal facet areas \(\sqrt3q\); the two-branch Cauchy projected-area expression; two Cauchy–Schwarz maximization certificates with squared difference \(4q(q-p)\); and the first-chamber normalized-minimum endpoint argument. The equal-weight \(3\)-design property is verified by direct degree-one, -two and -three moment identities. The full continuum and all equality conditions are therefore analytical statements, not an extrapolation of numerical enumeration.

No third-party proof checker or independent audit was used. The full text of one relevant broad-brightness manuscript was not accessible; this is an originality limitation rather than a numerical-verification defect.
