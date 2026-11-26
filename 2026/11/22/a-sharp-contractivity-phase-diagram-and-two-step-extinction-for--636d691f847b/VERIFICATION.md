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

For d=1+θh, drift inversion gives M=rI+(u+σΔW/d)N with r=(1−(1−θ)h)/d and u=γh/d². For v=σ²h/d² the Gram matrix has entries G₁₁=r², G₁₂=ru, G₂₂=r²+u²+v. Writing α=1−r²=hc/d², det(I−G)=α²−αv−u², because α+r²=1. If c>0, positivity is equivalent to the determinant test and hence c≥c*. If c<0 it is impossible, and if c=0 it requires γ=σ=0 (both the off-diagonal entry and v must vanish). Solving the affine inequality in h gives all three stated step sets. The continuous energy matrix is [−2,γ;γ,−2+σ²], so derivative at zero proves necessity and integrating the Itô energy identity proves sufficiency of γ²+2σ²≤4. In the discrete product any term with two N factors vanishes. For r≠0 its second moment is bounded by the stated geometric factor times a quadratic in n; testing e₁ gives necessity of |r|<1. When r=0 every product of two updates is zero for every realization. At the displayed explicit-Euler example E[(10+4ΔW)²]=116. These establish the claimed distinctions without any sampled tests.

## originality

PASS

The exact Gram and covariance form, scalar test equation and energy identity are standard. The assessment is for the joint resolved phase diagram in the fixed Euclidean norm, including the large-step-only nonexpansion regime where the continuous dynamics initially expand, and its contrast with a pathwise zero product at the resonant step. The strongest inspected indexed comparison changes the noise operator and concerns asymptotic stability. No equivalent or dominating resolved diagram for the common nilpotent drift and noise was identified in the bounded material inspected.

## value

PASS

The common nilpotent shear isolates one-step Euclidean amplification from modal asymptotic stability. Its precise comparison distinguishes regimes where larger steps actually restore weak nonexpansion despite initial expansion in continuous time, and identifies an exact resonant step with arbitrarily large transient amplification and guaranteed annihilation in two steps. These are informative diagnostics for interpreting results on stochastic time integrators; the value is not the elementary scalar stability test alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
