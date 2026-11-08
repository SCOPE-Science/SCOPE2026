---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The stationary distribution was checked by substituting explicit unnormalized weights into all four equations of the continuous-time generator. `verify.py` evaluates ten exact multivariate polynomial identities, then separately solves 4-by-4 rational stationarity systems by Gaussian elimination over a finite parameter grid, including both boundary allocations, and checks the closed forms and signs. The run completed with 12,514 exact assertions passing. The source of the universal quantifier is the derivative proof in RESULT.md, not the finite grid.

The strict side-of-midpoint comparisons use positivity of the stationary denominator and of the complement numerator \(H\) over the entire compact budget interval. The joint objective's derivative numerator has strict negative derivative, ensuring a unique global maximum including boundary cases. The rational example has an exact algebraic optimizer and was isolated by rational sign bounds. No independent audit, external proof-assistant certification, or empirical validation has been performed.
