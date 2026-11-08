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

Run `python3 verify.py` with Python 3 using only its standard library. A successful execution prints `ELLIPSE_ACUTE_CHECK_OK formulas=5 direct_samples=800000` after comparisons for five semiaxis choices. The script checks (1) the dilogarithm series; (2) a separately evaluated conditional probability integral over angle gaps; (3) direct quadrature of the arcsine-squared integral; (4) independent sampling of 800,000 triples and direct Euclidean dot-product tests, and (5) four exact sine-power integral identities numerically.

The numerical results are supportive checks; they do not prove the probability law. The exact proof is given in RESULT.md, using conditional integration and a convergent power series. The perimeter-uniform ellipse acute probability is outside scope. No independent mathematical validation was performed.
