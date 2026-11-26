---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Integrating the stationary covariance gives a=Cov(J,X(x)) and a'=b=Cov(J,X'(x)); the observation block is diagonal with entries 1+1/p and λ²+1/q because the same-site cross covariance and noise cross covariance vanish. This gives the two-term reduction, including omitted channels by continuity. On the left half, b>0 away from the midpoint, b'<0, and a+b'/λ²=2(2−K(x,0)−K(x,1))/λ>0, so noiseless a²+b²/λ² increases strictly. To justify finite-budget uniqueness rather than just a limit, set h=a_c²−a². With y=1/2−x and d=λ²e^(−λ/2), b∼dy and h∼a_c d y². Thus b²/(λ²h) extends to the midpoint with value d/(λ²a_c)<1, and its maximum ρ on the half interval is less than 1. The off-center gain is at most a²P/(1+P)+b²/λ², strictly below midpoint value-only gain when P>ρ/(1−ρ). For λ=8 at small P, the normalized objective in (x,p/P) converges uniformly to a convex combination of a² and b²; b(0)>a_c gives a unique maximizing corner on the left half. Both inward partials there are strictly negative and stay negative in a small rectangle, so compactness confines every maximizer to that rectangle and the corner is attained exactly. At P=1/20 the global pure maxima are a_c²/21 and b(0)²/84 from monotonicity. Independent rational arithmetic verifies the lower bounds 5507441/3688388100096 for mixed witness minus best gradient and 491/1835008 for best gradient minus best value. Strictness and continuity preserve the witness in an open parameter neighborhood. Reflection and compactness supply all quantifiers in the statement.

## originality

PASS

The closest co-located absolute-budget result changes the process to integrated Brownian motion, and the closest Matérn transition changes the observations to two values at symmetric sites with equal noise. Published derivative-enhanced Gaussian quadrature provides the conditioning framework but not this regime theorem. No statement-level coverage was found among the inspected sources.

## value

PASS

Even for a single predetermined common site, the global design needs different kinds of measurements at different budgets: derivative only, strictly mixed, and eventually value only. The mixed witness eliminates a pure-channel rule over all locations and holds on an open set, rather than winning at one handpicked site against a weak baseline. The eventual uniqueness proof addresses finite budgets, not merely noiseless convergence. These are useful sharp qualitative tests of budgeted derivative-enhanced design under the stated channel cost model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
