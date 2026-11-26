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

On a neighborhood of a regular initial condition the whole finite itinerary is fixed. Each Bayesian update is a coordinate translation by −log γ in log-odds, so the belief-space Jacobian is the stated positive diagonal endpoint ratio. Each numerator is at most 1/4, which bounds every singular value uniformly in the horizon at that initial state. The log of the logistic derivative differs from minus the absolute log-odds by a bounded amount, giving both versions of the coordinate exponent. In the sharpness example the horizon-dependent initial log-odds are T log γ and the final belief is exactly 1/2; fixing any one initial point instead gives exponent log γ<0. The example rules out uniform asymptotic nonpositivity or a uniform vanishing upper bound over initial states, not every finite positive upper bound. All conclusions are branchwise, not estimates across switching boundaries.

## originality

FAIL

Dong and Marzen already supply the same update, its one-step derivative and explicitly the rule to multiply these diagonal entries. Their factors are exactly adjacent ratios of b(1−b), so the endpoint law and its time-uniform bound are mechanically implied, not an independent theorem merely because the product was not printed in simplified form. The drift and finite-horizon witness add explicit interpretation but require only the logistic derivative and the inverse of a scalar translation.

## value

FAIL

Distinguishing tangent growth at a chosen horizon from asymptotic sensitivity and from cross-branch separation is useful clarification. As a mathematical finding the proposed refinement is a routine simplification of a published diagonal product, followed by a scalar inverse and a bounded logistic correction; no additional independent invariant or switching result is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
