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

Differentiation gives f'=2ρ+log(1−ρ) and (1−ρ)f''=1−2ρ, so H DF is symmetric and q=m(1−ρ)f' satisfies ∇q=(DF)^T∇h. The diffusion chain rule and m source yield exactly −f''|ρ_x|²−|m_x|²−2m² after periodic integration, with no activity coefficient. Conservation of the density mean and α_R≤f''≤1 bound the relative entropy above by half the sum of the two squared L² distances. Poincaré for the density fluctuation and the polarization reaction give the claimed minimum rate. For a steady or translated profile confined to ρ≤1/2, the entropy integral is constant; then m=0 and ρ_x=0 where ρ<1/2. At ρ=1/2 differentiability at a global maximum gives ρ_x=0 as well. At an unpolarized physical state the off-diagonal symmetry equation is (1−ρ_*)H_11=(1−2ρ_*)H_22, impossible for a positive-definite Hessian when 1/2≤ρ_*<1. This also verifies the obstruction at the degenerate threshold without relying on the rate bound there.

## originality

PASS

The PDE and linear spinodal are known, and the Hessian obstruction is a direct flux-Jacobian calculation, not credited in isolation. The supported contribution is the exact nonlinear periodic entropy balance with an explicit h and the resulting exclusion of all smooth stationary and traveling profiles confined pointwise to half filling or below, with a conditional quantitative decay estimate. The strongest inspected primary antecedent concerns a linear instability threshold and a particular stationary-interface construction, not this claim.

## value

PASS

The exact entropy turns a linear homogeneous threshold into a genuinely nonlinear statement for smooth finite-amplitude periodic profiles, at any activity. The endpoint argument at half filling handles loss of coercivity rather than treating it as a uniform decay estimate. It separates low pointwise density from low mean and gives a quantitative diagnostic when the stricter cap is known. These conclusions, not the familiar entropy framework or eigenvalue test in isolation, justify the result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
