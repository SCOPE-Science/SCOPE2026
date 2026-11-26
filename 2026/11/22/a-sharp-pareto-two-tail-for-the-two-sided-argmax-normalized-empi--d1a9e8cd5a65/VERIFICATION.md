---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For iid observations under a specified continuous null, the probability integral transform gives uniform order statistics. On each affine piece of the deviations, an equality between competing ranks lies on a null hyperplane. The numerator is bounded by one, so any exceedance forces the winning order statistic within 2/t² of an endpoint. Unless it is the first rank at zero or the last rank at one, there must be two observations in that endpoint interval, an O_n(t^-4) event. For a first-rank winner at u<1/(2n), competing ranks each occupy one of the disjoint intervals ((i-1)/n+u,i/n-u). The squared exceedance condition is (1+t²)u²-(t²+2/n)u+1/n²>0; its small root is 1/(n²t²)+O_n(t^-4). The simplex density n! gives n! times the integral of (1/n-2u)^(n-1) up to that root. Reflection doubles its leading coefficient to 2(n-1)!/n^n. Tail integration then gives precisely the q<2 moment range for q>0 and the stated logarithmic truncated second moment. This checks fixed n≥2 only, not a joint n,t limit. Inspected RESULT.md §§1–4, VERIFICATION.md and checker.py; the finite checker was not run and is not part of the proof.

## originality

PASS

Pass is for the explicit factorial far-tail coefficient with the O_n(t^-4) error, not for the statistic, a full CDF, or historical priority. Ferger's one-sided exact CDF and two-sided weak limit do not furnish this finite-n expansion. A separate same-day exact-CDF record genuinely covers the same distribution, but its verified statement is a general piecewise algebraic calculation, not an explicit inverse-square expansion; the endpoint-volume and noncorner estimates do additional work. That record mentions an earlier coefficient without identifying an independent source; it could refer to the reviewed finding. No distinct source for the explicit expansion was established.

## value

PASS

This is an explicit tail invariant of a published goodness-of-fit statistic. It identifies divergence of the finite-sample variance despite an exponentially small far-tail coefficient as sample size grows, and gives an inexpensive severe-tail asymptotic without evaluating an exact piecewise algebraic CDF. No ordinary test-level accuracy or uniform threshold regime follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
