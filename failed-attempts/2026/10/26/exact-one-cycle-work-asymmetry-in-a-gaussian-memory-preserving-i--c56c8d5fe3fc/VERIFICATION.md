---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The prefeedback linear Gaussian recursion has triangular deterministic part with eigenvalues (1−g)ρ and ν, both of modulus below one, and V>0 from the thermal noise. The stationary active marginal variance is A². Between feedback times C−C∞ decays at rate 1/τ_r+1/τ_c, and V−V∞ obeys a scalar inhomogeneous equation driven by C−C∞ with integrating factor exp(2t/τ_r). Integrating gives the stated F, including the repeated-rate limit. Applying C_+=(1−g)C and V_+=(1−g)²V+g²σ² yields the two displayed stationary formulas. Independently, W factors as X Y with X=g(y_-+ε) and Y=(κ/2)((2−g)y_-−gε); the centered normal pair has covariance m and covariance determinant d>0. Its product density and moment transform match the record; the exponential ratio follows by evenness of K₀, and the normal quadrant probability is 1/2+arcsin(m/√(m²+d))/π, equal to the asserted arctangent formula. There is no atom at zero, and symmetry is equivalent to m=0 because both density signs have positive support. A fresh Lyapunov computation for five parameter sets agreed within 4.44×10⁻¹⁶ in the covariance entries; finite density, tail and ratio comparisons also agreed without executing the frozen script.

## originality

FAIL

The actual single-event law and finite-cycle covariance are correct but are mechanically implied by two directly applicable existing results. Gaunt's general centered correlated-normal product theorem gives the claimed density exactly for a difference of squares factored into two Gaussian linear forms. Bahng, Lee & Ghim already give the exact relaxation and feedback covariance recurrences for this engine, including the coincident-rate interpretation; the displayed stationary covariance is their two scalar fixed-point substitutions. The physical parameterization is not credited as a new distribution or as a distinct substantive mathematical theorem merely because the two existing formulas were not previously written together.

## value

FAIL

An explicit single-event risk measure is useful in this engine, and assembling it makes a useful worked example. But the exact invariant as submitted adds only substitution into the known Gaussian product law and the solution of the previously printed triangular fixed point. The gain diagnostic at fixed V is immediate from the same formulas and does not give an optimized periodic engine or a new dynamical conclusion. No independently valuable unknown remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
