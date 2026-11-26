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

For real BV the positive and negative parts of Df have mass V(f)/2. Their product coupling writes the residual as V(f)/2 times the mean of the residuals of oriented arcs. In an equality case the arc residuals all have maximal norm and zero Hilbert-space variance, so they agree almost surely. Injectivity modulo constants gives the same ordered pair of derivative atoms. Parseval, the two frequencies ±n and V(1_arc)=2 give the stated 1/(2π²) coefficient, and continuity on [0,1/2] gives attainment. On the line the step residual is (sgn x)/2 times erfc(|x|/(2√t)); the inner product between two translates has absolute bound √(2πt) exp(−separation²/(8t))/4. Summing shifts at distances at least |k|−1/2 proves the exponentially small, uniform error needed for varying maximizing lengths. The line rescaling v=2π√t|ξ| gives √t F(d/(2√t)). Splitting the unregularized Dirichlet term from the Gaussian terms gives F′=erfc(z)−erfc(z/√2)/2. The increasing Gaussian hazard makes the tail ratio strictly increasing from 1 to infinity. The unique maximum lies strictly above the limit at infinity, so every maximizing rescaled length converges. Independent bisection on [0,2] with erfc rechecked the stated constants; higher-precision bisection using the alternating erf series on [0.9,1.1] gave z*=0.992269655382049579 and F(z*)=0.198313496197009020. The prefactor rounds to 0.445324035054261 at 15 decimal places (one final digit different from the frozen decimal); the exact formula is unaffected.

## originality

PASS

The generic pair-of-jumps reduction and sharp arc-norm representation substantially overlap the periodic multiplier work and are not the distinct content. The best-supported distinction is the Gaussian endpoint calculation: its uniform sharp profile, explicit erfc critical equation and unique microscopic optimizer for every maximizing sequence, with the strict gain over fixed arcs. No inspected statement gives that package. The closest fractional result excludes α=2, and its negative-tail proof degenerates there, rather than proving the Gaussian strict gap or uniqueness. This is a bounded evidence conclusion, not a chronology or priority claim.

## value

PASS

In a natural approximation norm the asymptotic constant cannot be recovered by holding a test arc fixed. The two jumps interact at a uniquely determined diffusion-scale separation, yielding about 20.01% more squared error than separated jumps. This settles both the sharp small-time benchmark and the geometry of all optimizers in that limit, rather than only substituting a heat multiplier in a formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
