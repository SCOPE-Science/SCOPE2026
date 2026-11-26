---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

In the bound model the speed is constant during each traversal; even for bounded Borel f the primitive F_f is absolutely continuous and vanishes at both boundaries. Its derivative along a descent divided by speed is f(X)-bar f almost everywhere, and the primitive agrees as zero on both sides of a reset. Durations a/V are Gamma(n-1, rate v0/a), so the finite-mean equilibrium renewal law length-biases the shape to n and samples the fractional phase uniformly and independently of duration. Every (n-1)st event of a Poisson process realizes the Erlang renewal; the remainder stage mixes exponentially to uniform for n>2 and is trivial for n=2. Truncate the endpoint determination to windows of radius R around each observation: whenever both enclosing resets are inside the window the local increments and starting stage determine the endpoint, and the missing-event probability tends to zero as R grows. Between disjoint windows, the stage approaches a uniform label independently of the first window. For a fresh start the same finite-state convergence gives one equilibrium endpoint. Extend the underlying fresh Poisson process independently to negative times to bound the fresh containing duration: its age and residual are each no greater than the distance to the (n-1)st event in their respective direction (age stops at zero if necessary). The sum of these two Erlang distances has all moments uniformly in the observation time. Together with stationary Gamma length bias and |F_f(X)/V| <= ||F_f||_infty T/a, this justifies convergence of first and second moments, including mixed products. The fresh initial primitive vanishes, so one obtains one endpoint, not the difference of two. For position, F_x=x(a-x)/2 and direct integration gives E[U(1-U)]=1/6, E[U^2(1-U)^2]=1/30, E Z_x=a^2 n/(12v0) and Var Z_x=a^4 n(n+6)/(720v0^2); the stationary factor doubles this. At n=3, a=v0=1, the values are 3/40 (stationary) and 3/80 (fresh). Conditional Gamma variance is strictly positive when f is not a.e. constant. Position has a nondegenerate nonnegative fresh limit and a symmetric stationary difference whose positive tail is bounded below by an exponential, excluding Gaussianity for both.

## originality

FAIL

The two distinct indexed ballistic results give equivalent and strictly broader coverage of the stationary coboundary, all-observable independent endpoint law, and limiting variance. The same-day date does not decide priority, but the implication is exact. In particular, the closest stationary source already invokes convergence from a newly started cycle as the step proving its two-endpoint law; the exact boundary term anchored at a reset leaves that one limiting endpoint. The stated Gamma fresh covariance and bias follow by length bias and the same immediate Gamma/beta moments. The fresh-start statement is explicitly scoped differently, but does not establish a distinct non-mechanically-implied contribution as submitted.

## value

FAIL

The all-observable absence of extensive variance is a worthwhile phenomenon, but the checked broader ballistic results already establish it with exact duration-moment constants. The remaining comparison between fresh and stationary preparations is useful as an illustration: one versus two independent boundary terms and elementary Gamma moments give precisely the submitted factor of two, bias and position numbers. No separate non-routine result or motivated invariant beyond this mechanically available specialization is established by the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
