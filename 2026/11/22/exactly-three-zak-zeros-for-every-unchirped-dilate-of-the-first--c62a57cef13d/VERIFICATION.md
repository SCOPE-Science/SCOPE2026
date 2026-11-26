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

Absolute locally uniform convergence follows from Gaussian tails. Poisson summation gives the periodized Gaussian's Jacobi product with q=exp(−π²/β); its logarithmic derivative is strictly negative for 0<x<1/2 since every denominator is positive and sin(2πx)>0. Thus the Zak value at ω=0 is strictly positive there, and odd pairing gives zeros at x=0 and 1/2. For β≥2, u exp(−βu²) is strictly decreasing on [1/2,∞), including at β=2 (the derivative vanishes only at the left endpoint). Grouping ±n makes Re Z at least its ω=0 value for 0<x≤1/2, strictly above it at x=1/2 for ω not an integer by the n=1 term. On x=0, the sine coefficient tail divided by the first lower bound is at most ∑(m+1)² exp(−6m)<1, using |sin(nθ)|≤n sin θ on 0<θ<π. One can also derive this fiber directly at every scale by differentiating ∑exp(−βn²)exp(−2πinω) in ω and using the same Jacobi product with nome exp(−β). The substitution k↦−1−k in the reflected fiber establishes the sign and phase in the reflection identity, excluding the other half strip. With the specified negative Fourier convention the transform of t exp(−βt²) is −i(π/β)^(3/2) ξ exp(−π²ξ²/β). Poisson on f(t)exp(−2πitω) gives Zf(x,ω)=exp(2πixω) Zf̂(ω,−x). For β<2 the dual scale is >2, and the map (x,ω)↦(ω,−x) permutes the claimed three points modulo the quasiperiod lattice. This proves the precise half-open-domain count for all β>0 without relying on samples.

## originality

PASS

Credit the three guaranteed parity zeros and the previously stated conjecture. The distinct theorem is global exclusion of any other Zak zeros for arbitrary positive dilation with zero chirp. The strongest accessible earlier result asserts the same three forced zeros but leaves exclusivity open in the larger family. Related rectangular-frame and half-density results do not count the zeros of one Zak transform. The accessible abstract of the plausibly titled older Janssen chapter treats nonnegative windows, not the odd first Gaussian derivative; its full text remained unassessed.

## value

PASS

Unchirped dilation is a natural full continuous family of first-Hermite windows and a clearly defined slice of an explicit published conjecture. Global exclusion gives information beyond the forced zeros and frame obstructions at a particular density: it locates every scalar Zak zero, which can be used directly when analyzing simultaneous-zero conditions. The proof is scale-uniform and does not claim to settle the chirped family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
