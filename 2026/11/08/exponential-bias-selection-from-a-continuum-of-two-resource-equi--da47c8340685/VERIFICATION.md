---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

In the uniform nonatomic two-resource affinity game C1-C2=2(x-q)+δ, the positive-noise logit fixed-point derivative F'(q)=p(0)-p(1) belongs strictly to (0,1), giving existence and unique q. Integrating the logistic response and eliminating z=e^(2q/σ) gives az²+(e^(δ/σ)-1)z-e^(δ/σ)=0, a unique positive root and the stated exact asinh formula. At σ=δ=0 every threshold allocation [0,s] has mass s and is a pure equilibrium; conversely all PNE are such thresholds. For δσ→0 and α=-σlog|δσ|, asymptotic asinh gives q→min(α,1)/2 for positive offset and its reflection for negative; zero bias always q=1/2. For α=1 the σlogσ correction is still valid. These formulae hold on δ∈(-1,1) and all positive σ. Independently evaluated closed-form fixed-point residuals on 15 separate (σ,δ) configurations and checked asymptotic scaling analytically; finite tests alone do not prove limits.

## originality

PASS

The primary 2026 Dupont–Petit–Séguret study already gives the *same unperturbed continuum* in Remark 2.3 and a general Gumbel-logit fixed point, but its nondecreasing-interaction uniqueness theorem does not apply to negative popularity costs, and its inspected theorem does not determine the positive-noise asinh branch or the joint exponentially small bias selection diagram. Semantically compared equivalent equilibrium-selection formulations and the closely related 2026 noisy two-resource findings; no inspected result entails the exact joint (σ,δ) selection. Acceptance is best-of-knowledge only.

## value

PASS

This computes how entropy/Gumbel regularization selects one of an entire interval of Nash equilibrium masses, and how arbitrarily tiny deterministic preferences can select *every* point. The exactly characterized exponential scale of bias is a natural, noncommuting-noise robustness boundary for the motivating model, not just a numerical fixed point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
