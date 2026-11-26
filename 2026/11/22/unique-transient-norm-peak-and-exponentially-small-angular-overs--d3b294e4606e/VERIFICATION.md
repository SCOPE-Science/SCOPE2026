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

The stated two unitary displacements cancel the linear exponential coefficient and produce the constant e^(−|b|²/[2(1−|a|²)]); the monomial diagonal has norm one. With b=c(1−a) this yields the exact R profile and the factor |c|²/2 for the given Fock normalization. Norm convergence also follows by replacing the diagonal composition C_az by the constant projection onto the zeroth monomial (error norm |a|), since the remaining rank-one vectors and scalar in the displacement identity converge in norm. For κ>0, the derivative numerator F has F'=(1+κ²)sinh(τ)cos(κτ), starts positive after zero, and has opposite signs at consecutive cosine zeros because κ sinh(π/(2κ))>1. This proves exactly one critical point per indicated open half-period and alternation. Where R>1, its excess is strictly increasing in q=e^(−τ) at fixed cosine phase, so every value above one after the first angular period is strictly dominated by its earlier phase representative. In the first period the endpoint values are below one and the unique local maximum is above one, giving the unique global peak; alternating signs at odd and even angular multiples also prove infinitely many crossings. For the asymptotics the rescaled stationary equation differs from cos θ+κ sin θ=0 by O(e^(−τ)). For fixed κ, q is bounded on J_m by a constant times e^(−τ_m^(0)); the simple cosine zero then yields the stated critical-time error and alternating excess. For the first half-period as κ→0 the angular shift is O(e^(−π/(2κ))), hence its time shift is O(e^(−π/(2κ))/κ), negligible both for the time expansion and relative to the leading cosine of order κ. This gives the relative norm excess as stated, not the additive norm difference. The κ=0 formula is tanh(τ/2), with no finite peak. Independent high-precision checks of the relative excess at c=1 gave ratios 0.998340250355… at κ=0.1 and 0.999999833333… at κ=0.001 to the claimed equivalent.

## originality

PASS

Credit established pointwise norms and norm convergence. Also credit the materially overlapping rotating Fock norm-jump record: its scalar maximum already gives the same leading weak-angular law after comparison of the two objectives and localization of the affine peak. The supported distinct contribution is the exact time-domain structure for the normalized affine composition norm: its own critical-point equation, one-per-half-period classification and unique first global peak, infinitely many limiting-level crossings, and the late alternating asymptotics. This does not assert priority over the related scalar asymptotic or formula for pointwise norms.

## value

PASS

For a norm-convergent evolution around a nonzero fixed point, convergence alone does not distinguish monotonic approach from transient amplification. The exact global peak, the count and location of all later extrema, and crossings of the limiting norm answer this qualitative and quantitative question for the full affine rotation family. The weak-angular scale explains apparent monotonicity at limited precision, but the value of the distinct result is its exact normalized time-envelope classification, not a rederivation of the known pointwise norm or overlapping leading scalar coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
