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

The ratio (1-z)/(1+s z), s=theta-1, has derivative -theta/(1+s z)^2, giving T'=alpha theta f with f=(1-z)^(alpha-1)(1+s z)^(-alpha-1). The logarithmic derivative yields (1-z)(1+s z)f'=(A+2s z)f, A=2-(1+alpha)theta. In the extension strip 0<s<1 and A≥0, coefficient matching gives (n+1)a_(n+1)=[A+(1-s)n]a_n+s(n+1)a_(n-1); induction includes A=0. When theta≤1 the two factors are individually nonnegative binomial series for alpha≤1, including alpha=1. In both cases |s|<1, so integration gives w_k=alpha theta a_(k-1)/k inside the unit disc and monotone convergence at z=1 yields sum w_k=1. The resulting positive-integer Laplace mixture gives the canonical all-dimensional copula and the conditional exponential sampler, with uniform margins. For alpha>1 the ratio at t=0 is (t/theta) times an analytic function equal to one at zero, so psi'' is negative to leading order. Otherwise above the theta frontier, e^t psi tends to positive w_1 and would force a positive Laplace measure to avoid [0,1) and have an atom w_1 at 1. The residual measure would be nonnegative, contradicting w_2 e^(-2t)+O(e^(-3t)) with w_2<0. This excludes any mixing measure, not just integer ones. The all-dimensional complete monotonicity criterion has the required strict endpoint and monotonicity hypotheses.

## originality

PASS

The inspected sources establish the bivariate distortion, the general criterion and known one-parameter slices. They do not give the exact family-wide all-dimensional frontier and the associated positive-integer frailty weights, especially the mixed strip 1<theta≤2/(1+alpha).

## value

PASS

This is an exact dimension-free classification for a previously proposed bivariate distortion, including an extra strip beyond the known rectangle and the full upper boundary. The explicit frailty law gives a constructive interpretation and exact joint sampler rather than just an existence test. It does not identify the maximal finite dimension outside that frontier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
