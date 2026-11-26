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

With x_s=√(a/b), s=at and h=A/(ax_s), the post-reset flow is y′=h+y−y³ and the age has exponential rate ρ=r/a; the chance of no reset in time s is e^{−ρs}, so the age mixture is stationary and unique. For h>0 the positive path increases to the stable root 1+O(h). The tail identity is m=∫₀^{y_+}e^{−ρτ_h(y)}dy. Subtracting log(1+y/h) from the hitting time leaves R_h≥0, with R_h(y)≤y²/[2(1−y²)] for y<1 and fixed-y limit −(1/2)log(1−y²), by domination of the positive remainder integrand. For ρ<1, y^{−ρ} dominates the rescaled integrand, and the interval above 1 contributes O(h)=o(h^ρ); substituting y² in the limiting integral gives the asserted beta coefficient. For ρ>1, y=hv makes (1+v)^{−ρ} an integrable majorant, and R_h(hv)→0, giving 1/(ρ−1). Independently, for λ in a fixed compact set and ρ=1+λ/L, the integral differs from ∫₀¹(1+y/h)^{−ρ}dy by O(h) uniformly: on [0,1/2] the integrand difference is bounded by C y²(1+y/h)^{−ρ}; on the rest each integral has O(h^ρ)=O(h) mass. With t=log(1+y/h)/L the comparison integral divided by hL is ∫₀^{log(1+1/h)/L}e^{−λt}dt, giving local uniformity and the log law at λ=0. Reflection gives oddness, and the susceptibility uses the difference quotient m/h, not differentiation through a divergent integral. This proof replays directly from the scalar hitting-time identity and the stated bounds. The supplied SciPy checks are finite corroboration only and were inspected, not run.

## originality

PASS

The same deterministic reset system with periodic forcing and its exponential-age renewal relation are prior. In fact freezing Wang et al.'s drive in the renewal equation gives the exact static mean integral. The new claim is the explicit weak-static-field trichotomy and the compact-uniform moving-rate profile, not that integral or the logarithmic escape-time mechanism. No distinct matching indexed or primary conclusion was established in the bounded comparison.

## value

PASS

Separates regimes in which differentiating a stationary response through a reset-age average is valid from those where rare long growth intervals dominate. The exact beta amplitude and compact-uniform crossover quantify more than the instability exponent or escape scale; they give a sharp boundary between singular and ordinary static response in a natural model already used for periodic gain. The result does not claim noise robustness or finite-frequency predictions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
