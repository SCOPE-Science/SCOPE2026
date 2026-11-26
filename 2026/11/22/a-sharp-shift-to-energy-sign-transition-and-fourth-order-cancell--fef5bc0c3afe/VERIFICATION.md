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

For the scheme in RESULT.md, write G(u)=u^3/f(u). The eliminated equation is 2(x_n-u)=h r_n G(u)/(1+hG(u)^2/4). G is strictly increasing on (0,a], and the scalar map v/(1+hv^2/4) is increasing throughout its range for small h. The two sides bracket at u=x_n/2 and u=x_n uniformly for bounded positive r_n, since G(x_n/2)≤x_n^3/(8√C). On every finite prefix the accumulated symmetric chain-rule defect is bounded by const·(max|Δ_n|)^2 Σ|Δ_n|=O(h²): Δ_n=O(h) and Σ|Δ_n|≤a. This bound inductively keeps r positive and bounded (the auxiliary update decreases r while x does), so the branch extends to all steps. At fixed h any positive limiting x contradicts the eliminated step equation and the uniform lower bound on r. The exact energy change is −Δ_n²/h. The per-step defect is −f'''(u)Δ_n³/24+O(|Δ_n|⁵); the mean auxiliary ratio is 1+O(h²) uniformly, so summing and applying composite midpoint quadrature gives h²∫₀ᵃ f'''(u)u⁶du/24+O(h⁴). Both errors use the bounded total variation a, not a fixed number of steps. Substitution t=u⁴/(4C), then s=√(1+t), gives the stated factored coefficient. Its sole zero at s=(2+√10)/3 gives the displayed energy ratio and signs. This proves O(h⁴) at cancellation, not a nonzero h⁴ coefficient or fourth-order state accuracy. VERIFICATION.md and check_quartic_sav.py were inspected, not executed; the decisive verification is the uniform summation and exact integral.

## originality

PASS

The underlying midpoint DG–SAV scheme, exact modified-energy law, and second-order accuracy are prior work. The supported distinct result is the signed leading coefficient of the infinite-time auxiliary constraint defect on this quartic flow, including its unique cancellation ratio. Accessible comparisons do not establish that result as prior coverage.

## value

PASS

Quartic decay is a canonical scalar gradient flow with a degenerate equilibrium, and the shifted auxiliary variable is meant to represent its physical energy. An artificial, permanently retained bias can have either sign despite the exact discrete dissipation law. The precise coefficient and ratio provide a reproducible benchmark for diagnosing that distinction and for choosing the shift in this model, not a general integrator order upgrade.

The dated certificate retains the supplied scientific assessment, sources and limitations.
