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

For fixed 1/2<p<=1 the invariant dyadic density gives J_m=E[X0 D^m(X0)]=mu/2+2^(-m)/12+B*c^m (checked independently by rational geometric sums at p=3/5,4/5,9/10 for m<=7). A random walk in doubling/halving decisions has exact identity X_n=2^(S_n-M_n)D^(M_n)X0; the reflected-height recurrence yields its generating resolvent Phi. Combining three modes and subtracting mu^2/(1-z) yields the stationary correlation generating function. Positive- and negative-edge square-root expansions and the t=1/2 physical-sheet pole determine the p<4/5, p=4/5 and p>4/5 fixed-parameter asymptotics. Independently enumerated exact walk probabilities and dyadic moments through lag 5 for three p; original packaged rational finite-lag verifier supplies further checks. No critical p=1/2 or uniform crossover theorem asserted.

## originality

PASS

Yan et al (2024) give invariant density and exact first small stationary lags, while their full-lag treatment uses approximation. Monthus (2024/2025) gives exact reflected walk and correlations for uniform rather than invariant initial law and observes the crossover scale. Neither inspected primary statement explicitly gives the new stationary three-mode algebraic transform and precise three-regime amplitudes; general machinery is a residual derivability risk.

## value

PASS

Exact stationary correlations govern mixing and fluctuations in a well-studied noncommuting random map. Recovering all lags and exact p=4/5 singular transition amplitudes resolves a specific physically motivated quantitative gap left by low-lag/approximate treatments. No CLT or near-critical uniformity is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
