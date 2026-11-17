---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Using last Poisson reset time A_t=min(E,t), X_t=2Λ∫_{t−A_t}^t B_s dW_s. Itô isometry gives E X_t²=4Λ² J_1(t), Wick integration yields E X_t⁴/t²→288Λ⁴/r² and Var(X_t²)/t²→272Λ⁴/r². Exact Markov conditional squared-moment closure with the unreset Ω_t gives the cross moment, so Corr(X_t²,X_{ct}²)→2/(17c) for fixed c>1; ordinary covariance has the factor e^(−r(c−1)t). For finitely many distinct positive macroscopic times, replacing Brownian B_s within each O(1) age window by B_{s_jT} has O(1/T) mean-square error after normalization, and disjoint Poisson windows give independent limiting ages/driving Gaussian factors. Laplace mixing yields product normal×Laplace and the density boundaries. Independent symbolic integration of the Wick polynomial confirmed the moment coefficients. Limit c=1 intentionally excluded.

## originality

PASS

Santra–Basu–Sabhapandit study the very same Brownian-square diffusivity but reset both particle and diffusivity; their conclusion identifies position-only resetting as distinct unstudied protocol. Bodrova–Chechkin–Sokolov study nonrenewal position resetting with deterministic time-dependent diffusivity, lacking correlated Brownian stochastic environment. Existing stationary two-clock diffusing-diffusivity results apply positive environment reset rate, not this nonstationary limit. The explicit shared-Brownian joint law and persistent 2/(17c) correlation survive those comparisons, with historical residual risk.

## value

PASS

Aging without stationary distribution and persistent nonlinear memory despite vanishing linear memory give a motivated sharp distinction between partial and full resetting. The exact finite-dimensional law, logarithmic central singularity, stretched tail and two-time coefficient are natural quantitative observables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
