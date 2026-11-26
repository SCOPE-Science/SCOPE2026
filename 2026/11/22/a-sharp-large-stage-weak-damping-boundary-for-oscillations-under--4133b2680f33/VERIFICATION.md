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

The classical row recurrence gives R_s=1−c_s+c_s q_s^s. Write ε=1/s, p=δ_s−γ_s, g=γ_s. Then p+g=ε/c_s and p−g=1/c_s−1. On a fixed bounded complex z-domain, log(1+pz)−log(1−gz) starts at εz; its ε³ coefficient is z/2−z²/4+z³/12, by the linear, quadratic and cubic logarithmic terms. It is odd in ε, with uniform remainder O(ε⁵) by analyticity near ε=0; division by ε and exponentiation give an even R_s expansion through ε². Evaluating at iω−ηε² gives the stated squared-modulus coefficient F(ω)−2η and uniform O(ε⁴). Strict |sin u|<|u| for u≠0 proves the positive defect. On a fixed small real λ interval, the analytic estimates also give convergence of the λ derivative of the squared modulus to 2e^(2λ) by Cauchy estimates. The crossing is unique there for sufficiently large s; the residual at λ=−F/(2s²) is O(s⁻⁴), hence so is the root error. At ω=0 the root is exactly 0. Multiplying the logarithmic squared modulus by floor(Ts²) proves the claimed energy limit. The source's SSP optimality premise is correct for the displayed family, with tableau uniqueness understood up to stage permutations.

## originality

PASS

The exact complex stage-transfer representation and the SSP-optimal family are known and credited. The strongest matched record uses that transfer for a negative-real stability interval and stiff large-stage endpoints. Its theorem, coefficient expansions and finite-stage alternatives do not give an evaluated bounded-complex weak-damping layer or the quadratic-step energy defect. The new result is the uniform asymptotic analysis of the transfer in that distinct regime, not the tableau or transfer itself.

## value

PASS

SSP optimality is not a modal energy guarantee. The defect establishes a concrete cost for a standard optimal family: even fixed undamped nonzero frequencies amplify, and a specific weak damping threshold is needed to offset the artificial energy drift. The first nonzero, frequency-dependent defect matters because its effect is order one after O(s²) steps. This differs from both finite-stage plotting and stiff scalar real-axis decay and gives a quantitative, testable calibration for the intended modal regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
