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

The frozen variance expression has denominator N-1 although N=2n-k=1 is permitted when n=k=1. The original formula is undefined there. The complete corrected repairs/4/RESULT.md restricts the expression to N>=2 and proves the deterministic zero variance at N=1. For N>=2 total variance yields a^2 Var(M)+a(1-a) E[M(N-M)]/(N-1), which equals the displayed harmonic expression. The event that a retained point is maximal twice is exactly maximality in the combined union. With the retained indices fixed, all union positions are exchangeable conditional on the number M of maxima, giving the hypergeometric law; independent ranked planar record indicators and independent selection of the rank marks give the coefficient PGF. The product-uniform orthant integral gives the alternating sum by binomial expansion. For refreshed labels, if the shared side is large, the joint upper bound is E exp(-m max(A(X),A(Y))); the CDF of the maximum is F_d^2 and the change of variable u=s/m in its Laplace integral gives O((1+log m)^(2d-2)/m^2). If instead the refreshed side is large, the two independent one-sample maxima probabilities give the same order. Consequently P and I can differ only with uniformly o(1) probability. Bai et al. (2)–(4) give the growth and concentration of M, uniformly over N in [n,2n]. Coupling marks by drawing M slots with replacement and handling a repeated slot at cost at most M(M-1)/(2N) gives the independent thinning limit, and binomial concentration supplies the factor q/(2-q) and rare mean theta/[2(d-1)!]. In dimension two the independently marked record count has Bernoulli probabilities a/j; the Poisson–Stein bound is at most a sum(1/j^2)/H_N <= C/H_N. The change in the Poisson parameter under K fluctuation is O(log n / sqrt(n)), uniformly in q, using a(k) Lipschitz with constant 2/n and harmonic increments at most 1/n there. At a=0 the approximation is exact for the thinned count. The supplied code was inspected rather than rerun; its variance helper already treats N=1 separately. No other files need correction.

## originality

PASS

The distinct content supported by the comparison is the persistence law for two partially shared samples under whole-vector refresh, especially the uniform negligible refreshed-label term and the resulting uniform planar Poisson approximation. The exact hypergeometric step is generic marking/exchangeability, and classical one-sample skyline and record identities are inputs, not independent claims of novelty. The one-point variance correction does not alter the literature comparison or any asymptotic claim.

## value

PASS

The robustness of a Pareto skyline to retention and refresh is a motivated two-sample problem. The union-normalized q/(2-q) survival fraction, the dimension-dependent rare-retention calibration, and a bound uniform from no retention to full retention in the plane together quantify it. The fresh-label control and uniform error make this more than the routine exact law for marking a fixed set; the finite boundary correction preserves that contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
