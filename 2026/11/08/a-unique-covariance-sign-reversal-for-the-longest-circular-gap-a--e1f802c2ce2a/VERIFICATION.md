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

The included `verify.py` contains two independent computational paths for the exact mixed covariance: (i) the proposed finite expression and (ii) a direct layer-cake integral of joint simplex-tail probabilities. It checks 2,635 cases using exact rational arithmetic for \(2\le n\le18\), including the endpoints \(t=0,1\). It additionally performs 48 comparisons with a numerically evaluated conditional-maximal-gap regression and reports sample unique zero locations.

Invoke `python verify.py`; SciPy is needed for the numerical quadrature, while the exact Fraction comparisons use the standard library. Computational checks do not establish the all-size theorem, which follows analytically from convexity, the endpoint signs and the conditional tail identity in `RESULT.md`. A numerical root-finder does not certify a root's uniqueness; uniqueness is proved separately.
