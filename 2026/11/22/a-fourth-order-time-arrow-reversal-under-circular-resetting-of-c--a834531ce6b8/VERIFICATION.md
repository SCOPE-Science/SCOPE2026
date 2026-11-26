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

An independent reset-age calculation gives the formula. Write a_±=1±u, A=R²/2 and let the common stationary age s be exponential of rate r. The conditional mean of each square is T/a_i+(A−T/a_i)e^(−2a_i s), and conditional covariance of the squares is −A²e^(−4s)/2 (the uniform-circle mark covariance times the deterministic damping). The covariance of the two age factors is 4a_+a_-r/[(r+4)(r+2a_+)(r+2a_-)]. Adding the mean conditional covariance gives the stated K, including its limit −R⁴/8. At a positive lag, the event of any intervening reset removes all dependence on the initial state. On the complementary event, centered OU squared-position regression carries the factor e^(−2a_i t) for the observed later mode, and the no-reset probability supplies e^(−rt). The reset and thermal symmetries give zero cross-mode positional covariance for both orders. For t>0 the difference of the exponential factors is positive, so its sign is the sign of the bracket in K. That bracket decreases strictly in r>0 from 4[(1−u²)z²−4z+2], with positive roots in z as stated, to −∞. This checks both crossing branches, strict negativity at the radius boundaries for r>0, and the simultaneous vanishing of both ordered covariances at the crossing. The ratio is claimed only where K is nonzero. No computation or thermodynamic reversibility claim is needed. The uploaded checker was inspected, not executed.

## originality

PASS

The supported distinction is the exact circle-induced reversal and complete two-threshold sign classification for the ordered observable. The underlying model, stationary law, and elementary reset/OU regression are not independent contributions. A related common-contraction result has the same chronological ratio, so that ratio alone does not distinguish the finding. This assessment is limited to the available statements and explicitly leaves primary-text risks.

## value

PASS

The two competing effects of a common reset age and mutually constrained reset marks produce a nonmonotone radius criterion: both sufficiently small and sufficiently large radii permit a rate crossing, but all intermediate radii have negative asymmetry at positive rates. This exact phase boundary and the all-lag disappearance of the fourth-order diagnostic at the crossing distinguish mechanisms invisible in second cross moments. The value is in the complete classification for this natural reset geometry, not the routine regression step.

The dated certificate retains the supplied scientific assessment, sources and limitations.
