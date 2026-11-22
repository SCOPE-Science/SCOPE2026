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

# Reproducible verification

The accompanying `check.py` was run successfully with Python 3, SymPy and NumPy, returning `PASS: 220 exact and independent numerical assertions`. It checks rational Legendre coefficient formulas, barycentric identities and facet intersections, plus independent 650-point Gauss–Legendre integration over four radii, five parameter pairs per radius and degrees zero through nine.

The universal positivity and strictness statements are proved analytically in `RESULT.md`. Numerical quadrature, finite matrix tests or finite symbolic substitutions alone cannot prove the full statement. Independent mathematical review and external certification have not been performed.
