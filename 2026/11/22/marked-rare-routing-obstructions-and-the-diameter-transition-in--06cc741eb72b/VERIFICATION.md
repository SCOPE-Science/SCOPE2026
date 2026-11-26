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

Independently reconstructed the statement in RESULT.md, lines 5–34 and 42–63. The absence of a left-to-left 2-path is exactly row inclusion. One obstructed row pair has three equiprobable coordinate types 00, 01, 11; this gives the stated means, common variance 2/9 and covariance 1/9, so the conditional multivariate CLT has correlation 1/2. Two distinct obstructions on three rows give five allowed patterns out of eight for a fork and four for a chain; two reversed obstructions permit two of four patterns. Disjoint row pairs are independent. For a direct check of the marked argument, independently retain each obstruction with probability 1−exp(−f) at its mark. The conditional probability of retaining none is the Laplace functional. Scalar dependency-graph Poisson approximation applies to the retained indicators, with errors bounded by O(m³(3/4)^{2n} + m³(5/8)^n + m²(1/2)^n); the three terms vanish under the given scaling. The conditional CLT times the ordered location-grid limit gives the limiting retained mean. The conditional mark laws are tight and expected mass is bounded, giving weak convergence of finite point measures, not just local convergence. The overlap expectation also tends to zero. For the diameter reduction, condition on the row of a fixed left vertex and choose an available witness right neighbor different from the queried right vertex. Each of the other m−1 independent rows offers a 3-path with probability 1/4. A union bound with the missing-neighbor and failed right-to-right 2-path events gives exactly the stated three error terms. On the complement every left pair can route in at most four steps; bipartite parity makes an obstructed pair require four, while in the absence of obstructions the diameter is exactly three (one direction of each cross edge is absent). This also covers the allowed infinite-distance convention. VERIFICATION.md and check.py were inspected, not executed. The stated 79,561 assertions are source-reported finite checks, not independent reproduction or asymptotic evidence; the pass rests on the proof check.

## originality

PASS

The ordered inclusion-count Poisson limit is already covered by Stark. The supported distinct result is the Bernoulli row-degree and ordered location process jointly with the directed 3-versus-4 diameter reduction and its explicit finite error. The strongest distinct indexed overlap proves a closely related Gaussian-marked matching for continuous coordinatewise comparisons, with the same endpoint correlation, but it does not imply the Bernoulli theorem or the routing result. No priority order is inferred from the matching publication date.

## value

PASS

The graph diameter is a global maximum over directed routes. The explicit reduction to a sparse family of disjoint anomalous pairs and the joint degree law identify where the transition comes from, distinguish typical outdegrees from the troublesome one-third/two-thirds profiles, and quantify when other routing failures can be ignored. This is more than reusing a prior count threshold or rephrasing a covariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
