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

# Verification

The proof is in `RESULT.md`. Its global assertions follow analytically from strict unimodality of the logistic-shrinker derivative, monotonicity of the objective-value gap and local Taylor expansion; finite computations cannot establish these claims for all parameters.

Run `python3 verify.py` using the Python 3 standard library. For hardness \(a=4\) and threshold \(\lambda=1\), it computes a unique maximum slope near 1.718092822612, critical multiplier near 2.392577628561, and positive quartic coefficient near 0.929930127555. It then solves the two fold equations and the equal-area equation at three small supercritical distances, and compares jump and fold-width ratios with their predicted leading constants. At criticality it tests the signed cubic-root response on both sides of the critical input. The checker reports `OK` when all assertions pass.

The numerical checks are cross-checks rather than proof certificates for the entire continuous domain. The exact uniqueness, fold count, asymptotic exponents, and matrix lifting are proved in the manuscript. No external independent audit has been performed.
