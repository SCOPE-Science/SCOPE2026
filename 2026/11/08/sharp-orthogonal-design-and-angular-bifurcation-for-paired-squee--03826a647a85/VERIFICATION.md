---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The stated unit normalization and Fourier convention give ambiguity magnitude exp[-pi(s x^2+s^(-1) xi^2)/2] before rotation. Both positive summands strictly decrease along each ray, so the closed-disk minimum is on its boundary. Doubling the angular coordinate and shifting by pi gives the two exponential-cosine terms. At antipodal doubled centers the floor is the minimum of a strictly convex exponential sum in x=cos(t); its derivative gives the clipped logarithm. To compare any other angle, relabel if needed so the antipodal minimizing cosine is nonpositive, hold that cosine fixed and choose the sign of sin(t) to decrease the other cosine. This is strict for a negative minimizing cosine, even at -1; for cosine zero it is strict whenever sin(beta) is nonzero, and for coincident centers t=pi makes both terms smaller. This proves exact equality only at perpendicular physical axes. For equal weights and s_1>s_2, the stationary cosine is x_infinity minus a positive multiple of R^(-2); direct subtraction shows 0<x_infinity<1. It enters the interval through -1 at the stated R_0 and never reaches +1. Inverting the doubled cosine proves the one- and two-line classification, square-root opening at threshold, and the pi/4 crossing. The variables are real phase-space coordinates; no requirement that a fractional Fourier transform preserve real-valued windows is needed.

## originality

PASS

The positive-sum reconstruction denominator and equal-spacing design are known, as are related three-window squeezing thresholds. The supported distinct claims are exact two-window maximin over relative orientation for arbitrary positive weights and genuine squeezings, with strict equality classification, and the exact change of the minimizing directions for unequal squeezings at equal weight. The strongest inspected precedents use different objectives, a restriction to common kernels, or a different number of windows.

## value

PASS

A weighted positive ambiguity floor is a concrete denominator-design target in multi-window inversion, distinct from ellipse coverage. Fixing the squeezings and weights is a natural constraint when windows are chosen in advance. An exact optimizer with no alternative relative angles, plus the radius where the worst line splits into two, gives both a usable stability floor and the directions at which it is tight.

The dated certificate retains the supplied scientific assessment, sources and limitations.
