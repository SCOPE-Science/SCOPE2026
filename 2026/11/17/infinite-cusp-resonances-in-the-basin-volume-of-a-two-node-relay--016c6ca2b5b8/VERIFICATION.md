---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For 0<λ<1, same-side quadrants are invariant fixed-point basins; mixed quadrant x<1/2<y has pre-flip x_k=1−λ^k(1−x0), y_k=λ^k y0. Their first half-threshold crossing times agree exactly on the basin of the alternating prime two-cycle; simultaneous flipping enters an alternating invariant strip, with contraction λ² for the two-step return. For uniform initial coordinates, the two crossing clocks are independent with bin widths ℓ_j=(1−λ)/(2λ^j), final ℓ_K=1−1/(2λ^{K−1}), K=ceil(log(1/2)/logλ), so A=2Σℓ_j², other two basin measures (1−A)/2. Differentiation of bins on both sides of λ_m=2^(−1/m), m≥2, gives positive left and negative right derivatives, with maximum 3(1−λ_m)/(2(1+λ_m)); asymptotically A=3(1−λ)/4+O((1−λ)²) as λ↑1. Checked rational-bin algebra and exact λ=2/3 A=1/4; independently compared one-sided derivative signs m=2..13 and numerical weak-contraction ratios 0.753141,0.750056,0.750016 for decreasing deficits. Only algebra/finite parameters were computed; proof covers infinite cusps.

## originality

PASS

Gaivão–Pires establish generic asymptotic periodicity for certain higher-dimensional piecewise contractions with variable partition hyperplanes; this does not compute the exact Lebesgue area of a tuned two-coordinate relay basin or its infinite cusp parameters. Calderón–Villar-Sepúlveda address one-dimensional injective piecewise contractions. Closely named coupled cusp/threshold records in Resultary refer to different maps and observables. No inspected same-model prior provides the crossing-clock squared-bin formula.

## value

PASS

Even a two-node bistable hard-threshold network has a nontrivial phase basin-volume response: infinite nondifferentiable resonances accumulating at λ→1 despite fixed attractor inventory. The all-parameter exact measure and sharp weak-contraction scaling quantify a natural sensitivity invariant unavailable from generic attraction/periodicity statements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
