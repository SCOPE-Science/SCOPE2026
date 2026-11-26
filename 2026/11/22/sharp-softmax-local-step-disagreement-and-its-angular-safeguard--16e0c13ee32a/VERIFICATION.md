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

For the stated one-hot, one-example logit path d=e₁−q, the second-order cross-entropy loss and first-order softmax squared residual minimize at ‖d‖²/(dᵀHd) and (dᵀHd)/‖Hd‖². The covariance form is positive on zero-sum nonzero d, giving the reciprocal squared cosine. Proportionality requires all incorrect probabilities equal, since (Hd)_j/d_j=q_j+qᵀd for j>1 and the remaining component is determined by zero sum; thus binary always gives one. Independently, in the ternary case with v=1−p, imbalance t and u=t², resolve Hd along d and the orthogonal zero-sum vector w=(t,(3−t)/2,−(3+t)/2). Conditional covariance over true versus incorrect classes gives dᵀHd=v³D/4 and wᵀHd=−3v²t(1−u)/4, where D=p(u+3)²+u(1−u); the norm ratio ‖d‖²/‖w‖²=v²/3 then gives R=1+3u(1−u)²/D². Differentiation gives the stated sign factor p(u+3)(u²−12u+3)−u(1−u)². On (0,6−sqrt(33)) the critical equation's map Φ(u) increases strictly from zero to infinity by its positive derivative; after this interval the sign factor is negative. This proves a unique interior maximizing u for every p, up to exchanging the two incorrect classes. Φ(u)/u→1/9 gives u_p/p→9 and pR(p,u_p)→27/18²=1/12. For each fixed K>3, continuity by assigning additional classes arbitrarily small positive masses transfers arbitrarily large ternary ratios. The rule cosφ≥c gives the exact sharp ceiling c⁻², attained at an interior ternary distribution by continuity from u=0 to a larger ratio; the ceiling 16 is an all-retained-samples zero-probe bound, not a rare-p asymptotic. The mathematics applies to the explicitly specified local estimates and cutoff; attribution to the exact source equations and strict rejection wording could not be independently resolved. If the comparison used strict retention, the same supremum would hold by approach, without equality. Read RESULT.md:3–93, VERIFICATION.md and verify.py; did not execute submitted code. No finite-probe, minibatch, parameter-Jacobian or actual-step claim follows.

## originality

PASS

The supported distinctive claim is the exact worst-case ternary law at fixed true-class probability, its unique imbalance and its sharp 1/(12p) growth, together making precise when the two defined local rate estimates can disagree and whether the angular ceiling can be saturated. The estimator definitions, rejection rule, and elementary angle algebra are not independently credited as novel. Attribution and broader priority are qualified by actual access below.

## value

PASS

The comparison is between two independently motivated local surrogates for the same learning step. The binary agreement does not generalize: a fully sharp ternary law identifies both the probability imbalance causing arbitrarily large disagreement and its precise leading rate. This separates empirical averaged agreement from pointwise guarantees, and makes the local safeguard sharp rather than merely conservative, without overclaiming loss descent or training stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
