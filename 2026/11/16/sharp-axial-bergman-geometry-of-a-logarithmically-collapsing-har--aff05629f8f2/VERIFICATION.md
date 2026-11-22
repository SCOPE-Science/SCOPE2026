---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Rotational orthogonality gives squared monomial norm π² μ(n), μ(n)=∫_0¹ s^n exp[-2(log(e/(1-s)))^α]ds; axis kernel K=π^-2 Σ r^(2n)/μ(n). Setting x=-log(r²), a(t)=-log μ(t), differentiation of log Z(x)=log Σ exp[a(n)-xn] verifies exact β²=Var_x(N)/r² (no lost π or factor two). For the continuous μ(t), q=1-s gives strictly concave H_t(q)=t log(1-q)-2log(e/q)^α; mode q_t solves tq/(1-q)=B_t=2α(log(e/q))^(α-1), q_t~B_t/t, B_t~2α(log t)^(α-1)→∞ since α>1. Gaussian Laplace curvature and controlled tails imply a’(t)~B_t/t and -a’’(t)~B_t/t², not merely pointwise local quadratic fit. Unique discrete saddle a’(t_x)=x gives t_x~2α x^-1(log 1/x)^(α-1), variance asymptotically 1/(-a’’(t_x))~2α x^-2(log 1/x)^(α-1) from discrete local CLT/tangent-tail concentration. Therefore β coefficient sqrt(2α); radial induced metric and dL/dr~2/(1-r²) give axis-distance coefficient sqrt(2α)/(α+1). Independent numerical quadrature of actual moments for α=1.5,2.0 and δ=.05,.02,.01 found finite variance/predicted ratios decreasing from ~1.39 to ~1.36 and ~1.30 to ~1.26 with negligible n-tail masses; slow convergence is not a proof. Direct differentiation of moment series and both saddle curvatures checked. The endpoint α=1 has a different exact Bergman coefficient, as correctly excluded; ambient geodesic distance is not identified.

## originality

PASS

Best-of-knowledge PASS for the sharp coefficient on exactly the Hartogs family introduced by Chen–Xiong. Their 2026 Theorem 1.4 and §7 Lemma 7.3, directly read in full-text HTML, prove only an ambient distance comparison and an axial metric UPPER bound with implicit constant, explicitly leaving optimal estimates open. Earlier exponentially weighted disk literature was found to prove comparability, not an exact coefficient in accessible abstracts/material; its inaccessible full text remains a concrete priority risk rather than an automatic failure.

## value

PASS

This computes a sharp previously unspecified geometric constant for a canonical logarithmically collapsed Hartogs family and its intrinsic-axis path length, refining a concrete contemporaneous one-sided estimate. The two nested Laplace/variance mechanism is substantive analytic content; it does not pretend to settle unrestricted ambient Bergman distance. Exact boundary growth geometry is a motivated natural invariant, not an arbitrary numeric slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
