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

For positive sorted lengths, absence of nondegenerate triangles is equivalent to x_{i+2}≥x_i+x_{i+1}: the two largest smaller lengths maximize the pair sum for each possible largest length. Consecutive growth and x_{i+1}≥x_i imply x_{i+d}≥F_{d+1}x_i by induction. For m observations at or below t, anchor the negative-side constraint at x_m≤t and the positive-side constraint at x_{m+1}>t, omitting empty sides. In z_i=log(x_i/t) coordinates the required negative and positive distances from zero are at least log F_{j+1}, j=0,…,m−1 and 0,…,n−m−1 respectively when counted outward. Their sums are c m²/2−O(m), c(n−m)²/2−O(n−m), with c=log φ (Binet or the adjacent Fibonacci exponential bounds). For an alternative upper proof, integrate the two global exponential envelopes implied by the log-density limits with positive slopes α−ε, β−ε. For each assignment of the labelled observations to sorted positions, discard ordering but require the coordinate tail inequalities just obtained. Independence yields their product and the union over at most n! assignments only costs o(n²). This recovers the exponent upper bound uniformly including m=0,n. For the matching lower bound use separated interval boxes x_i∈[t q^{i−m−1}, t(1+h)q^{i−m−1}] with q>φ, 1+h<q and (1+h)(1+q)<q². These inequalities force strict separation and all consecutive inequalities and give the exact occupancy apart from the endpoint at t of probability zero. Each log interval has constant width and positivity and continuity on compacts extend the tail lower bounds with exponents α+ε and β+ε to the entire line. Thus the product of the interval probabilities has logarithm at least −(log q)/2[(β+ε)m²+(α+ε)(n−m)²]−O(n); shifting one coordinate a bounded amount changes cost by at most a constant. Taking n→∞ first at fixed q,h,ε and then ε↓0 and q↓φ gives the exact-count exponent for every convergent occupancy sequence. Empty sides and threshold translation are harmless throughout. The quadratic cost minimizes at α/(α+β) with value cαβ/[2(α+β)], and summing at most n+1 counts does not change its leading exponent. Subtracting this minimum from the pointwise rate and using compactness (take a convergent subsequence of maximizing lattice points for the closed-set bound, and approximate any open-set point by lattice points for the lower bound) gives precisely the conditional LDP, including both endpoints and convergence at each fixed threshold. These analytic checks are replayable from inequalities (5)–(15) or the independent upper-bound argument given here. I inspected but did not execute the frozen check_two_tail.py; finite rational box tests and separate floating-log diagnostics cannot establish the asymptotic result. No result was inferred for moving thresholds, tail-probability-only hypotheses, local fluctuation laws, or finite-size prefactors.

## originality

PASS

The surviving distinct claim is the evaluated joint large-deviation rate with two finite positive log-density slopes, and the resulting conditional occupancy LDP and optimized harmonic-mean exponent. The no-triangle recurrence, Fibonacci spacing, integral formula methodology, and one-sided quadratic rate are already present in earlier work and are not credited as new. The actual closest indexed and primary statements were compared; none supplies the two-sided split and optimization.

## value

PASS

The triangle-avoidance event is classical, and the existing one-sided Pareto and bounded-support answers give a specific reason to ask what changes when the sample can occupy both tails. The cost of using many extremely small sticks competes with the cost of using many extremely large ones, changing the leading constant rather than a lower-order correction. The exact conditional rank law predicts the macroscopic fraction on either side of any fixed physical threshold and quantifies all atypical splits, including occupying only one tail. This is more than a reapplication of a Fibonacci product or a new example distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
