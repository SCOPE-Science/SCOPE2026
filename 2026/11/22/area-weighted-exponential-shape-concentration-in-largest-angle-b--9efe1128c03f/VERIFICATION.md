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

A uniform point selects each depth-n leaf with probability equal to its true area fraction. If all parent angles are at least c and its maximum is at least 2c, each child's angles are at least c and its maximum is at least c+alpha/2>=2c, giving the claimed invariant by induction. The child retaining beta has weight sin(gamma)/(sin(beta)+sin(gamma)); the complementary child has the other weight. Both are in [s,1-s] because beta,gamma are at most pi/2. Independently checking the projective step: for a sorted child triple (a,b,c') the factor exp(D) is max(a/2,b,c')/min(a/2,b,c'). Sorting (1/2,x,y+1/2) and (1/2,y,x+1/2) gives nonincrease, with equality for L exactly on y>=1/2 or x=y<=1/2, and for R exactly on x<=1/2 or x=y>=1/2. Away from p each equality step lands outside the other child's equality set: the new coordinates straddle 1/2, allowing equality in one coordinate only on the relevant boundary. This proves strict decrease for both mixed words; the all-chart compact minimum is positive off the fixed-point sublevel. Conditional on each previous block and its next first symbol, the second symbol differs with probability at least s. Coupling the block indicators by uniform thresholds yields binomial stochastic domination without an independence assumption on the shape path. If the final D is at least epsilon, every mixed pair decrements it by at least Delta_epsilon, so at most floor((D0-epsilon)/Delta_epsilon) such pairs occurred. The argument includes odd depths, epsilon=D0, and the fixed root; a fixed polynomial times (1-s)^N tends to zero exponentially. Replay: RESULT.md lines 35–56, the equality tests above, and Michaud's Lemmas 2 and 4 and Theorem 8. The analytic result does not rely on check_area.py. Static inspection shows that script reverses the two geometric child weights and does not actually test a binomial-tail comparison despite the description in VERIFICATION.md; its symmetric branch bounds and normalization checks do not detect the reversal.

## originality

PASS

The supported distinct claim is the area-weighted finite-depth tail for a complete tree. The known decrease theorems and equal-count rates are not credited as new. Michaud explicitly separates the equal-weight statistic from the area-weighted extension. The closer prior Resultary finding gives a stronger deterministic mixed-step inequality, but its statistical theorem does not control dependent physical-area sampling. The new ingredient is matching those paths with conditional switching uniformly from below, and controlling their finite-depth tail.

## value

PASS

Euclidean area sampling answers a different and explicitly motivated mesh question from counting leaves: it controls the fraction of the initial physical domain in badly shaped descendants. An all-depth bound valid despite dependence is useful in its own right. Credit is limited to complete unconstrained trees and does not include sharper deterministic contraction or an adaptive-mesh guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
