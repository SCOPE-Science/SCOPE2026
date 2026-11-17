---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

With iid renewal gaps 0<w_-<=W<=w_+ and iid independent defective hit delays U, Q(t)=E product_{S_i<=t}(1-G(t-S_i)). The sandwich g_(1-p)(t)<=Q(t)<=g_(1-G(K))(t-K) is correct since ignored births contribute factors <=1. With cE exp(theta W)=1, tilting on first overshooting gap gives g_c(t)=c^-1 E_tilde exp(-theta S_(N_t+1)), bounded between c^-1 exp[-theta(t+w_+)] and c^-1 exp(-theta t). Continuous theta_c squeeze as G(K) to p yields exact log rate. Strict convex-order monotonicity/Jensen yields fixed-mean constant-gap optimizer; Poisson survival exp[-b integral G] gives bp, and Pareto first waiting time gives zero exponent but a.s. reaction by infinitely many geometric successes. Independent computed roots for p=.1,.4,.8 in deterministic and two-point clocks and checked ordering; finite tests do not certify the asymptotic; single-particle Brownian p=exp(-L sqrt(d/D)) follows killed harmonic ODE. Scope excludes general unbounded light-tailed renewal law and finite-time survival ordering.

## originality

PASS

Best-of-knowledge PASS for bounded-renewal/delayed-success exponent plus strict fixed-mean clock ordering. Classical Bernoulli renewal thinning and Lundberg adjustment coefficient explain the zero-delay tilt, and Poisson-search literature covers bp, not the joint delayed-success statement with general bounded-renewal clock convex-order optimum. An inaccessible plausible November 2026 same-model article remains a priority risk, not a claim of exhaustive literature search.

## value

PASS

PASS: Renewal timing is a natural experimental control in mortal search and synthesis; the exact long-time reaction rate depends only on hit probability despite arbitrary success delays, while deterministic clock is unique robust optimal fixed-mean choice. Extends physical Poisson-birth analysis with a mathematically meaningful convex-variability comparison. Jensen/renewal tilting are classical tools, not themselves claimed novel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
