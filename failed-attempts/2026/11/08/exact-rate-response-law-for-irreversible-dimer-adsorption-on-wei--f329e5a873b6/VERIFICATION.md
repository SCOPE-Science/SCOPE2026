---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Conditioning on the first accepted edge among (2m-1) path edges and 2m rate-λ spokes forces the Catalan convolution with denominator βm-1, β=2(1+λ)>2. The Riccati β zQ′=Q-1+zQ² and substitution Q=-βu′/u yield a positive-coefficient entire denominator u, whose unique minimal-modulus simple positive zero ρ gives q_m=βρ^{-m-1}+smaller exponential error. Positivity of u coefficients and implicit function theorem give strict parameter monotonicity and analyticity, so Taylor expansion yields the fixed s/m response. Direct rational-arithmetic recurrence checks for λ=1/2,1,2 reproduce all finite q_m values through m=7. The expansion ρ=β-1/2+O(1/β) follows from the first two entire-series coefficients, not from finite samples. Valid only λ>0; λ=0 is discontinuous.

## originality

FAIL

FAIL: the October 25, 2026 published weighted-WHEEL result explicitly defines the hub-avoiding PATH probability q_m for 2m path vertices and an arbitrary positive spoke rate λ. Its recurrence is precisely (2(1+λ)m-1)q_m=sum_j q_jq_{m-1-j}; its complete generating function is exactly the same Q=-βu′/u with u={}_0F_1(; -1/β;z/β²), and it proves the identical dominant zero ρ(λ), simple-pole amplitude β, and strict monotonicity. The fan survival event is exactly that already analyzed path subproblem of the wheel after the first rim adsorption. The new 1/m rate-window and large-rate -1/2 expansion are standard Taylor/first-coefficient consequences of the prior explicit analytic function, rather than an independently new rate law.

## value

FAIL

FAIL: the physically natural weighted-fan survival statistic is valid and interpretable, but it is explicitly the path q_m already solved as a central lemma of the preceding all-rate wheel result. The new local perturbation limit is automatic after differentiability of the previously proved ρ(λ) and the large-λ term follows by two-term asymptotics from its hypergeometric equation. Neither offers a substantive new structural boundary, unknown invariant or non-implied result beyond that prior stronger treatment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
