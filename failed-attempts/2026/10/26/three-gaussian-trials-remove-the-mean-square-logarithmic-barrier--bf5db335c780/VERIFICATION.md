---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For a rotation through α the joint squared loss is 2(sin²(2α)+ε²cos²(2α)), with optimum 2ε². In the random eigenbasis the conjugation uses the direction of (g1,εg2); isotropy of (g1,g2) gives the stated one-trial law, whose survival is powered by L. Independently, writing t for the distance of the best folded angle to π/2 yields density L(2/π)^L t^(L−1) and normalized squared loss (sin²t+ε²cos²t)^−1. For L=1 the tangent substitution gives 1/ε. For L=2, the squared-moment integral near t=0 differs from the integral of t/(t²+ε²) by a uniformly bounded amount, giving the 8/π² normalized log coefficient. The integrable limits for L≥3 follow from sin t≥2t/π. At L=3 integration by parts gives ∫ t² csc²t dt=π log 2 over [0,π/2]; at L=2 the first-moment integral uses ∫ t csc t dt=2 Catalan over the same interval. L=1's first moment is the complete elliptic integral; subtracting the regularizing integrand 1/sqrt(t²+ε²) gives the log(4/ε) asymptotic. Thus the constants refer to rates at fixed L, not failure of finite-noise moment existence. Read verify_rjd.py without executing it. `python3 /workspace/branches/independent_checks.py` (section 2; mpmath and SymPy) corroborates the normalized constants by angle-density integration; the proof uses integrable domination and the explicit endpoint comparison, not numerical extrapolation.

## originality

FAIL

The distinct published 2026/10/18 record SCOPE-exact-restart-moment-frontier-for-two-by-two-randomized-joint-di--0b473a2a4655 directly covers the matrix pair, random experiment, full best-of-L law, all headline mean-square asymptotics and the sharp three-trial criterion. Its angular-minimum law and this record's arcsine survival are the same distribution. The elliptic and Catalan expressions for the first moment are not explicit in the earlier Finding, but here they are direct integrations of that same known law and do not establish a distinct headline theorem. This is demonstrated coverage, not an inference from failed retrieval.

## value

FAIL

The known benchmark is scientifically useful as a demonstration that a high-probability perturbation bound can hide a mean-square penalty. The frozen work repeats that exact benchmark and frontier; the remaining first-moment expressions are direct evaluations under the previous law, with no further structural threshold beyond the integrability of the elementary angle density or distinct need for those constants established. No substantive surviving repair is delivered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
