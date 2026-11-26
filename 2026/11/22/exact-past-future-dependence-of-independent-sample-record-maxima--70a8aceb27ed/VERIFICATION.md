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

For 1<=n<m, let r=n/m. The continuous CDF transformation is lossless almost surely even with flat intervals: the generalized inverse of F applied to F(X_i) is at most X_i almost surely and has the same law, so it equals X_i almost surely. The uniform endpoints U=F(M_n)^n and V=F(M_m)^m have copula min(u v^(1-r),v). Exchangeability and the absence of ties give mass r on u=v^r. Off that curve the mixed derivative is (1-r)v^(-r) for u<v^r and zero on the other side; the density integrates to 1-r. The product law is Lebesgue on the square, so their overlap is the integral of min(v^r,1-r). Splitting at a=(1-r)^(1/r) gives 1-r-r(1-r)a/(1+r), and its complement is exactly the claimed TV under the sup-event normalization. The optimal positive event is the singular curve together with the density-greater-than-one region. To pass from endpoints to fields, future observations after n are independent of the earlier history, so given M_n, the kernel for the earlier history is unaffected by M_m. Given M_m the later path uses independent observations after m. These two kernels attach the histories to either the true or the independent endpoint law. Thus contraction gives an upper bound by endpoint TV and projection gives equality. Threshold events M_n>t imply M_m>t, whose probability can be arbitrarily small positive, giving phi=1. Equality of endpoint maxima has positive joint and zero independent probability, so the full joint law is not absolutely continuous with respect to the product and its KL divergence is infinite. The limits as r goes to 0 or 1 give the claimed relative-age coefficient and fixed-lag supremum. The supplied checker and verification notes were inspected but the executable was not run; the direct overlap computation, not finite checks, establishes the formula.

## originality

PASS

The exact copula is demonstrably prior and not credited as new; the singular support and the monotone threshold consequences are structural ingredients, not separate priority claims. The distinct substantiated result is the explicitly optimized absolute-regularity coefficient for the complete nonstationary past and future and its sharp relative-age scale. The closest inspected statements do not give this optimum, nor a broader formula that specializes to it. This is a bounded assessment, not a claim of unique priority.

## value

PASS

Record maxima are a canonical nonstationary process; dependence at fixed lag and at lag large relative to age are different questions. The formula provides the complete-history absolute-regularity value and the sharp constant 1+e^(-1) when n/m is small. Measuring this quantitative decay despite maximal conditional dependence and infinite information divergence is a use for the exact coefficient, not just a restatement of the endpoint copula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
