---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The exponential race on vacant edges gives the stated recursion, including R(1,1)=1 and the zero-coefficient boundary terms. Conditional on bridge use, each clique is greedily matched with one fewer vertex, which proves the full vacancy law. Coupling the first attempt as E/beta with a common unit exponential E reduces success to the survival of two independent tags in bridge-deleted cliques. Each survival is E[J(t)] divided by clique size; its derivative is strictly negative at each finite time because the initial state has positive holding probability. This gives strict monotonicity and the weak-rate parity discontinuity. At u=mt the vacancy fraction has drift -x^2+x/m and quadratic-variation rate at most 2/m, giving uniform convergence on compact u-intervals to (1+u)^(-1). The rescaled Laplace law and the early-attempt/late-survival bounds give the three rate regimes. For fixed beta, Jensen's logistic bound dominates the rescaled product by a constant times (1+u)^(-2) up to u=m; above m the O(m^(-2)) product times the exponential kernel has O(m^(-1)) contribution to mP. This justifies the distinct fixed-rate coefficient, including rho=1. Independent exact recursion arithmetic reproduced 1/3, 3/10, 2/7 and 5/26 at unit rate; it did not independently reproduce the full graph or scaling law. The frozen checker was inspected, not run.

## originality

FAIL

An independently indexed record covers the same single-bridge process, finite recursion, Laplace identity, weak-rate discontinuity, coverage distribution, fixed-rate logarithmic coefficient and proportional-rate integral. The target's additional phrasing for variable rates and strict monotonicity follows directly from those results and the tag laws; it does not separate a substantive claim. This is verified equivalent coverage, not a finding of historical priority: the comparison record has a later catalogue path. The frozen mathematics is not shown false.

## value

PASS

As a mathematical result this explains a genuine finite-size effect: a faster bridge changes the number of matched vertices in opposite directions for the two same-parity cases. The exact crossover and the distinct weak-rate and fixed-rate limits quantify when the effect matters. Scientific usefulness does not undo the verified duplicate coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
