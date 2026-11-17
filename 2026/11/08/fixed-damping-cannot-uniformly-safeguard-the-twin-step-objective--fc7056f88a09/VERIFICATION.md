---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For any fixed kappa>1 and 0<eta<=1, both normalized gradient descent rays intersect at the explicit feasible positive parameters t=(epsilon*kappa+epsilon+kappa-1)/(2 epsilon kappa), s=(epsilon+kappa-1)/(epsilon kappa). With common damping the pair distance contracts by 1-eta; epsilon times the common intersection tends to (-(kappa-1)/kappa,-(kappa-1)), so both objectives scale as eta^2(kappa-1)^2(kappa+kappa^-2)/(2epsilon^2) from bounded initial points. For kappa=2, eta=c epsilon gives limiting best-objective minimum of two exact quadratics and unique upper safe threshold (20+2sqrt(19))/9; determinant identity gives 1-cos(theta)~2epsilon^2/25. Direct independent symbolic/rational check confirmed intersection, positivity, two limit quadratics, angle scaling and c*. This is one raw step, not behavior of safeguarded full method.

## originality

PASS

Original fixed-curvature bounded-input simultaneous objective divergence is distinct from the primary near-parallel large-step discussion and from the previously published orthogonal-gradient example, whose unbalanced second starting energy grows with the amplification parameter. The angular-safe c* coefficient is not stated in either inspected work. Best-of-knowledge; earlier general optimization counterexamples may exist.

## value

PASS

The example proves that a common fixed damping cannot enforce even one-step objective safety on a strictly convex two-dimensional quadratic of fixed condition number and quantifies the necessary square-root angular-gap scale. This directly exposes a nontrivial stability limitation of the distance-based step, not a generic steepest-descent observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
