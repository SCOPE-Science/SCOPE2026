---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

The governing analytic inputs are the sharp-constant reduction and the absolutely convergent hypergeometric series in Theorem 1.3 and Proposition 6.1 of arXiv:2611.10656v1. Both were inspected against the original paper with the Riesz-potential normalization recorded in its equation (1.1).

The proof independently verifies that the series remainder and its first two derivatives are bounded uniformly in every integer dimension at least three when the fractional order is at most one half. The Gamma-ratio normalization then gives two uniformly twice-differentiable factors that agree at zero. Their first-derivative difference is exactly the finite-gap coefficient. This is the analytic certificate for the all-dimensional result.

A supplementary finite numerical experiment evaluated partial hypergeometric sums for dimensions 3, 4, 5, 10 and orders 0.2, 0.08, 0.03. It was compared with the explicit comparison constant and the Laurent formula. The numerical output was consistent with the claimed asymptotics but is not a substitute for the proof; truncation error grows relevant as the order approaches zero. No machine-based infinite theorem certification or independent validation was performed.

The dimensionally uniform error constant is not given a numerical optimum. The proof does not extend the exact unrestricted sharp constant to dimension two. Bibliographic uniqueness is not formally certified.
