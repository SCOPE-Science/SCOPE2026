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

Write D=n−1+a+b. With k ones, the up and down transitions share factor (1−ℓ)(2r−1)/(nD), multiplying (n−k)(k+a+t) and k(n−k+b+t) respectively, with t=(1−r)D/(2r−1). Detailed balance gives the stated beta-binomial law. Positive committed weights ensure irreducibility of the labeled chain, so permutation invariance identifies the full exchangeable Bernoulli mixture, even for nonanonymous F. Folding P about 1/2 gives a strictly decreasing likelihood ratio in z when t increases. The sign odds conditional on z do not depend on t: the tilt (1/4−z²)^t cancels. For the Bernoulli response g, a pivotal edge has positive probability under the shared-uniform coupling at any two distinct interior probabilities, so g is strictly increasing; self-duality makes g(1/2+z)−1/2 positive and antisymmetric under reflection. The conditional signed response is therefore strictly increasing in z for a>b, strictly decreasing for a<b, and zero for equality. The order reverses when changing from t to r, including t=0 at r=1; beta concentration as t→∞ gives the fair endpoint. In the illustration the Beta(c+1,c) density is 2p times Beta(c,c); integration by parts using the stated binomial-tail derivative verifies the formula for all m≥0. The weighted-majority example is read within the explicit monotonicity hypothesis: with positive voting weights any self-dual tie resolution is monotone; if zero weights are allowed, monotonicity of the tie resolution must still be imposed. Frozen finite rational tests were inspected as evidence, not executed or relied on for the infinite quantifiers.

## originality

PASS

The supported distinct claim is the strict finite-electorate cross-conformity order simultaneously for all coordinatewise monotone self-dual binary rules. The beta-binomial equilibrium and previously known majority comparisons are not novelty claims. A general prior folded-beta likelihood-ratio criterion may cover the folded-magnitude lemma but the available evidence does not give the signed aggregation order.

## value

PASS

This answers a fixed-electorate parameter question not settled by the stationary law, a majority comparison, or a population limit. One strict sign applies to every neutral monotone binary rule, including nonanonymous ones, and identifies the precise role of the exogenous bias. The sign/magnitude decomposition supplies an explanation for that uniformity, with no empirical or finite-time claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
