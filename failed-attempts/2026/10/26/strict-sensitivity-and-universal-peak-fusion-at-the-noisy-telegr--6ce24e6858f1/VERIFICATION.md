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

For q=rho/h in (0,1), the beta–Gaussian law gives the central-curvature equation H(q,z)=2z E[T]-1=0 at z=1/(2 delta). The stated Kummer ODE gives a strictly negative second derivative of G at every stationary point; small-z and differentiated large-z signs establish existence and uniqueness. Using G'/G=-H/(2z) there gives z H_z=1-q, so the boxed denominator is exactly 1-q. The q derivative is 2z Cov(T,log(1-T)), strictly negative for the nondegenerate tilted law. Implicit differentiation and delta=1/(2z) give the boxed quotient. At fixed interior q, the quartic derivative at criticality is strictly negative; heat flow converts it to twice the derivative of curvature in thermal variance. The expansion of p'(y)/y in delta-delta_c and y² then yields y²=3(delta_c-delta)+O((delta_c-delta)^2) and a local maximum on the positive side, identified as the off-center mode by the two-mode classification. This is in normalized coordinates and is not uniform in q. The supplied quadrature code was inspected, not run; no floating point check is needed for the analytic assertions.

## originality

FAIL

A distinct indexed same-day record gives the identical central-curvature equation, its exact nonzero crossing derivative, the heat equation, quartic criticality, and global mode classification for the same normalized family. Its explicit identities yield both the covariance sensitivity and the peak coefficient by direct differentiation and expansion. This is statement-level coverage by implication, not a claim about the order of publication within the day. The November peak-opening record confirms overlap but is not earlier evidence.

## value

FAIL

The geometry of an exactly characterized mode transition is worthwhile, but the model-specific work claimed here is already supplied by the matching global-mode and simple-crossing result. The remaining exact identities reduce to implicit differentiation and the leading symmetric heat-flow Taylor balance; neither is an independent invariant requiring another model-specific argument. No distinct valuable remainder is established in the frozen scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
