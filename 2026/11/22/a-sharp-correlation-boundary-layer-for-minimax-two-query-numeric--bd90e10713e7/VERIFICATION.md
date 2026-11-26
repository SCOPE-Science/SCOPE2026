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

The unbounded constant, linear and quadratic coefficients force exactness on degrees 0–2, hence the only finite-risk predetermined linear designs are central differences. The two signed cubics attain the Taylor bound Mh²/6; the error variance is exactly σ²(1−ρ exp(−2h/ℓ))/(2h²). In normalized variables, q=1−ρ(1+x)exp(−2x) is positive and its derivative ρ(1+2x)exp(−2x) is nonincreasing, so xq′≤q and q/x⁶ is strictly decreasing from infinity to zero, including at ρ=1. This gives uniqueness and strict decrease of both optimal spacing and risk with ρ. Expanding q uniformly as δ+ρx+O(x³), δ=1−ρ, gives x∼[κδ]^(1/6) at fixed δ>0 and x∼κ^(1/5) at δ=0. When δ/κ^(1/5)→α, the ρ=1 root is a lower bound and x⁶≤κ(δ+x) gives an upper bound of order κ^(1/5); the normalized equation has the unique limit z≥1 with z⁶=z+α. Substitution of δ+2x+o(κ^(1/5)) in the risk gives both constants and the stated risk profile. In the outer overlap δ≫κ^(1/5), scaling by (κδ)^(1/6) in the same inequality gives x/δ→0, hence the nugget law. Independent bisection at κ=10⁻⁵ gave 0.146779926762, 0.112272913733 and 0.099879220204 for ρ=0, 0.9 and 1 respectively. Inspected the supplied verification and source without running the uploaded program; the analytic proof, not the finite competitor grid, certifies the theorem. No nonlinear, randomized or adaptive minimax conclusion.

## originality

PASS

The independent-noise specialization is known and acknowledged. The closest two-query and correlation results inspected do not establish the stipulated OU-plus-nugget minimax problem or its joint positive-correlation boundary layer. This is a comparison against inspected evidence, not a publication-priority certificate.

## value

PASS

The useful conclusion is not rediscovery of central differences. Under an experimentally meaningful nugget plus spatially correlated noise model, removing the nugget changes the optimal radius and risk exponents. The sharp joint scaling and universal profile specify when the independent-noise rule ceases to be predictive and how to choose spacing through that transition. This is a motivated boundary effect within the stated fixed two-call class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
