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

The proof is analytic: an exact Haar measure-preserving sum/difference transformation, independent arcsine-type variables, a normalized conditional integral, two elliptic-integral substitutions, a standard complete-elliptic-integral asymptotic, and finite-moment algebra.

Run `python3 verify_ellipse_chords.py` from this directory, using Python 3 and its standard library. The checker verifies the density-integral normalization and moments for \((a,b)=(3,2),(2,0.5),(1.01,1)\), direct trigonometric factorizations, reconstruction, and the logarithmic singular coefficient from both sides. Seeded Monte Carlo of 220,000 endpoint pairs is a secondary check. Expected success string: `ELLIPSE_END_POINT_CHORD_DENSITY_CHECKS_OK`.

Numerical integration is approximate, and the finite tests alone do not establish the statement for all ellipses; the written proof carries the quantifiers. No independent audit or external certification is asserted. This distribution uses independently uniform eccentric-anomaly endpoints, not arclength-uniform or invariant-line chords.
