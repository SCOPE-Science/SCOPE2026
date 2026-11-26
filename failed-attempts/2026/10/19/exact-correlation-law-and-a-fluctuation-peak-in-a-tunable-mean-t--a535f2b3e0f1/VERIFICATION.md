---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For 0<b<1/2 both branches expand and their cell transition matrix is primitive. The two-level invariant density is normalized and equivalent to Lebesgue. More explicitly, the stationary itinerary has transition rows (0,1) and (b,1-b), since conditional on a cylinder its final image is uniform on its Markov cell. Shrinking cylinders give mixing; the full-Lebesgue basin gives physicality and uniqueness among acips. In the affine-density transfer matrix, the constant block has polynomial (lambda-1)(lambda+b) and the slope block lambda^2+(1-b)^2 lambda+b^2; the zero-mass subspace has all roots inside the unit circle. Independent integration gives E[X^2]=(1+b^2)/3, E[X T(X)]=(b^2(2+b)+1+2b)/(6(1+b)), and E[X T^2(X)]=(2+5b^2-b^3+b^4)/(6(1+b)), splitting at b and 1-b(1-b) for the last integral. Subtract m_b^2 and apply the cubic recurrence from the zero-mass characteristic polynomial to confirm the full rational generator. Summing the geometrically decaying transfer iterates yields the bounded Gordin correction; the resulting reverse martingale differences are stationary, bounded and ergodic, and the bounded coboundary leaves the CLT and the limiting variance unchanged. The Green–Kubo evaluation 2G_b(1)-G_b(0) gives the stated positive variance. The derivative is -Q/(12(1+b)^4); Q increases from -1 to 9/16 on [0,1/2], proving uniqueness and the sign change. At resonance the denominator is cubic and the unreduced numerator there equals 6b(b^2-b+1)=18b^2>0. The exact formulas also give both small-b limits. The supplied symbolic and integration tests were inspected as recorded checks, not run as evidence for the proof.

## originality

FAIL

A distinct indexed record, 898171b8464a, explicitly covers the same covariance law, stationary CLT variance, variance maximizer, and uncancelled triple pole on a strictly larger parameter interval. This is demonstrated equivalent and dominating coverage, not a claim about which draft came first. The ancillary stationary mean and endpoint behavior leave no scientifically distinct final theorem.

## value

FAIL

The peak and correlation resonance are worth determining for this natural slice, but the frozen theorem adds no independently useful unknown fact once the complete larger-interval law is accounted for. Its remaining endpoint arithmetic and monotonicity do not justify an independent repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
