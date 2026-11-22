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

# Reproduction and limits
Run `python verify.py` with Python 3 and NumPy installed. It checks exact rational Gram factor identities, strict principal-angle improvement over interior random instances, 210 higher-dimensional nondegenerate examples, orthogonal boundaries and leading local cubic coefficients. It passed **15,310 assertions** when run against the included source.

The proof in `RESULT.md` is the evidence for the universal convergence claim. Numerical experiments do not certify infinitely many starts or unobserved regimes. The target is rank one, the observations are full and noiseless, and the tangent and SVD steps are exact. A zero tangent projection at the doubly orthogonal start does not define a rank-one update. Independent external mathematical audit has not been performed.
