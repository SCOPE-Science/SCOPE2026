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

Complete resets give the unique stationary law by averaging a fresh excursion over its exponential age. To rederive the transform, write F for the diffusive component, B for the sum of the ballistic components and M for their difference. With Fourier convention E[e^(ikX)], the equations are (r+a+Dk²)F−bB=r(1−θ), ℓB−ikvM−aF=rθ, and ℓM−ikvB=0. Elimination gives F+B=r(ℓS+A_θ k²)/Q with A_θ=v²−θΔ, so Φ(0)=1. The real quadratic Q(i√t) is positive at zero, negative at both ℓ²/v² and (r+a)/D (value −abℓ), and has positive leading coefficient. Thus there are two simple positive roots u<w. The density can be written as (1−β_θ)(√u/2)e^(−√u|x|)+β_θ(√w/2)e^(−√w|x|), allowing a signed β_θ, where β_θ=[rA_θ/(Dv²)−u]/(w−u). At the numerator zeros t₀=ℓS/v² and t₁=S/D both t_j>u, so the slow weight is positive. Evaluating Q(i√t_j) gives −aℓSΔ/v² and bSΔ/D respectively, proving opposite fast-weight signs off balance. Positivity of the density follows independently from the regenerative law's positive contribution from excursions spending positive time diffusively, even for ballistic-only resets. Cancellation of the fast weight is unique and interior; cancellation of the slow weight is impossible. At balance Q=ℓ(r+Dk²)(S+Dk²), giving the stated common Laplace law. For x>0 take y=e^(−(√w−√u)x); the derivative in y of the ratio of the two affine factors has the sign of β_θ₁−β_θ₂, the sign of Δ, and y decreases. The density difference is proportional to √w e^(−√w x)−√u e^(−√u x), giving the common crossing and the stated strict tail order on integration. Logarithmic curvature is the product of the signed fast and positive slow weights times a positive factor. Strict loss comparisons follow by integrating the tail difference against the nonzero Stieltjes measure of the monotone continuous loss, and real positive moments are finite by exponential decay. The reset-rate and numerical example agree with these formulas.

## originality

PASS

The positive-rate complete-reset model, pure-phase stationary solutions, and balanced Laplace equality are not new. The supported distinct result is the physical-parameter off-balance classification, especially the strict radial order reversal and the unique feasible Laplace mixing weight with its curvature interpretation. The verified exact prior is credited; nearby same-model and analogous catalogue results do not establish this classification in the material read. Primary full-text gaps are explicit below.

## value

PASS

Choosing which phase to restart is a natural control parameter for this published process. Uniform radial order over all mixing probabilities yields a strict all-increasing-loss comparison and identifies when changing the reset rate changes which phase is preferable, beyond variance. The inverse design answers a different concrete question: whether a feasible intervention can make an exactly Laplace stationary law when both pure reset modes fail. The unique interior design and curvature boundary, with the common crossing and analytic parameter guarantees, constitute a useful complete stationary classification in this model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
