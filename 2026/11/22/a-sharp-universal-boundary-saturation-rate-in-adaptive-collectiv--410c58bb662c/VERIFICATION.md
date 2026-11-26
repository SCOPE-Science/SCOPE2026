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

The polynomial equations have boundary factors and bounded interior logit derivatives, giving global forward interior solutions. Subtracting κ times the risk-logit derivative from the cost-logit derivative cancels x and gives h(r−ρ), with h=(α−β)s. For a=(c−β)/(α−β) and u=1−r, one has min(a,u)^(1+κ)≤au^κ=Q(1−a)r^κ≤Q. For ρ>1, Q(t)≤Q(0)e^(−λt), proving the uniform-in-trajectory exponent, with an initial-state-dependent prefactor. When ρ=1, either ∫u diverges and Q→0, or ∫u converges and bounded u' forces u→0 by uniform continuity. Both cases give the boundary-union limit and exclude nonempty compact interior forward-invariant sets. For the sharp witness, ρ=2, κ=11/20 and λ=11/10. At x*=102/155 the identity 2b x*(1−x*)=β makes E* an equilibrium. The three diagonal entries in the triangular linearization are β(1−2x*)=−49/775, −(4−5x*)=−22/31 and (11/20)(2−5x*)=−22/31. Hyperbolic attraction gives exponential convergence on an open interior part of the neighborhood. Division of the scalar u and c−β equations by their positive deficits then gives two log derivatives equal to −22/31 plus integrable errors. Integration yields strictly positive asymptotic coefficients, establishing actual saturation of the bound rather than just equal linearized exponents. For b=1, E₀ has diagonal spectrum −3/4, −4, −11/10. At E₁ the cost eigenvalue is −121/80; the in-face block has trace −3/25 and determinant 3/50 (off-diagonals 32/625 and −75/64), giving the claimed stable conjugate pair. The basins contain interior points, and the two limits exclude replacing the union by either face alone. Direct substitution also checks the stated counterexample at ρ=1/2.

## originality

PASS

Credit the strongest same-day indexed comparison, not just the previously cited opposite-sign result: it gives the identical cancellation, strict odds bound and exclusion of compact interior invariance at and above the threshold. Its odds bound mechanically implies the displayed supercritical minimum estimate, so the rate bound as an upper estimate is not counted as distinct. The pass is for the sharpness claim, supported by a stable interior-accessible example whose two face deficits attain the predicted exponent, together with the explicit critical face-union convergence and counterexamples to strengthening that union. The checked same-day source proves sharpness only for existence of a compact interior invariant set at subcritical ratios, not sharpness of the saturation exponent. The shared date does not settle priority.

## value

PASS

An odds bound controls a product, not the actual slowest approach of the two coordinates to the stated union. The rational hyperbolic witness proves that the loss in passing to a minimum really occurs on an open set of strictly interior starts, rather than being only an artifact of an inequality. The stable alternative outcomes and critical analysis further give a precise interpretation of what can and cannot be concluded about long-time saturation in the motivated three-variable model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
