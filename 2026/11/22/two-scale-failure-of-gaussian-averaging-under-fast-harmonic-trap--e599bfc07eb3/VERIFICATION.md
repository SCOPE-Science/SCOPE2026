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

This verdict applies to repairs/5/RESULT.md. The frozen large-|y| expansion at line 141 is false as written: its additive constant counts b=1/(2α) twice. With v+=D/α and δ=1−z_y, the saddle gives δ=c/y²+O(y⁻⁴), c=2bv+²/L. The variance term contributes +b, while the entropy contributes a log z₀+b log(1−z₀)−b log c beyond 2b log|y|, with no second +b. The corrected remainder is O(y⁻²). Independently, the normalized weak/strong variance conditional laws are Beta(aq+1,bq) and Beta(aq,bq+1), each with mass 1/2. The resulting mixture yields the stated positive amplitude and strictly convex phase with unique interior minimum, and Stirling plus Laplace yields the leading prefactor and the posterior normal limit. Compact-y uniformity follows by a uniform saddle gap and integrable endpoint majorant after extracting one phase factor. The derivative in y² is positive, giving increasing z_y and current-state posterior. Expanding the saddle at zero gives the quartic coefficient L²/(8v₀⁴H₀)=(α+β)(β−α)²/(64D²) and the relative-error bounds at smaller/intermediate scales. The fixed-q endpoint power and prefactor use the separate one-sided Laplace integral with exponent bq−1. Replay: python /workspace/checks/reproduce.py 5. It independently confirms the constant discrepancy (frozen error tends to −1/2 at α=D=1, β=3 in the residual-minus-constant convention) and corroborates the rare prefactor, posterior and crossover by separate-state Gauss–Jacobi quadrature. The uploaded code was inspected, not run; it checks remote saddle location, not the additive cost constant. The replay does not prove the asymptotics.

## originality

PASS

For the corrected result, credit the exact stationary mixture and usual central Gaussian to prior work. The remaining contribution is its quantified two-scale fast-switching density limit and current-state posterior in the positive-stiffness model. No inspected result states or directly specializes to this full asymptotic claim; the stationary integral is a strong precursor from which the result is derived, not itself a new law. Priority remains bounded.

## value

PASS

The repaired result quantifies the first breakdown of Gaussian relative accuracy rather than merely observing nonuniform tails, distinguishes a quartic correction from a nonlinear rare-displacement rate, and recovers both stiffnesses from their separate signatures at known diffusivity. The posterior shows what information about the current hidden state survives averaging in a rare observation. These are natural features of the known stationary law, not a new notation for it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
