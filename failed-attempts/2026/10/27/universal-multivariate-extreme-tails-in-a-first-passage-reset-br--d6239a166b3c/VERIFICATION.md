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

For N≥3 the regenerative cycle has finite mean (L²/D)J_N, since its survival is erf(L/√(4Dt))^N. Integrating the reflected kernel below −b leaves the positive Gaussian integral from b to b+2L. Both this integral and single-walker survival are (πs)^−1/2 times Gaussian averages at s=Dt/L²: respectively over a uniform point on [b/L,b/L+2] and on [0,1]. Tonelli and the gamma integral give the joint probability exactly as C_N E[(Σ Z_i²)^(1−N/2)], with independent uniform points of these types for the constrained and free walkers. For b_j=a_jR this proves the limit by scaling the sum by (R/L)²; it is bounded below after scaling by Σ a_j²>0 and converges uniformly in the averaging points. In particular the coefficient and cancellation of D are correct. Dividing by the one-label tail gives the equal-threshold conditional limit, and layer cake with the bounded positive part gives the moment boundary and logarithmic coefficient (equivalently with log(R/L)). The finite quadrature checks in VERIFICATION.md and verify_first_passage_tail.py are consistent with this proof but do not certify the limit; the bundled script was inspected, not run.

## originality

FAIL

The distinct indexed Resultary finding on multivariate Pareto excursions gives the same joint limit and equal-threshold conditional coefficient under identical assumptions, the same moment criterion, and additionally a Gamma age limit. K_N there equals C_N L^(N−2) after substituting Z_N=(L²/D)J_N. Neither exchangeability to arbitrary labels nor the boundary logarithm from layer cake leaves a substantively distinct claim. This is verified duplicate scientific coverage in the reviewed corpus, not a determination of who obtained the result first; the path dates do not establish priority.

## value

PASS

Judged apart from duplicate coverage, the result identifies a useful exact heavy-tail dependence law of the stationary Brownian gas: observing one extreme leaves a nonzero probability of any fixed number of joint extremes, with a sharp direction-dependent constant and a corresponding moment boundary. The same exponent for all k is not a consequence of the between-reset independence alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
