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

The beta moments give the specified positive normalizer. The left endpoint factor is never zero. The right endpoint vanishes only at (rho,delta)=(0,1), where absorbing (1-x)^2 adds exactly two to the right shape. After this reduction, equality of endpoint orders fixes alpha and the canonical right shape b; the factor with constant term one is then uniquely fixed. For its nonzero linear/quadratic coefficients p,q, delta=-2q/p and rho=4q/p^2-1. A constant factor gives exactly the reported beta fibers, including the strict cutoff b>2. Density zeros inside the interval do not affect this argument. At rho>0, delta=0 the rho score vanishes, and the other scores are multiples of centered log(x), log(1-x), x. A putative constant linear combination, differentiated and multiplied by x(1-x), has all three coefficients zero. The scores are square integrable, so this proves the exact Gram rank. Identical laws at every sample size give the stated consistency obstruction. The frozen SymPy checker was inspected, not executed; its algebraic checks do not prove exhaustiveness or Fisher rank.

## originality

PASS

The beta reduction at zero tilt and the model itself are known. The reviewed contribution is the exhaustive collision classification, the resulting reconstruction criterion and the exact zero-tilt rank, not rediscovery of the beta reduction. The preprint's injectivity assertion is contradicted by an admissible collision; the journal's mixture restriction does not imply the reviewed result. No independent equivalent was verified in the bounded source comparison.

## value

PASS

The result tells which model parameters can be recovered from arbitrarily many observations, corrects an unrestricted published-preprint inference, and distinguishes the globally nonidentifiable fibers from the exactly three first-order identifiable directions on the interior beta submodel. The boundary collision and complete off-fiber reconstruction are useful beyond the trivial zero-tilt degeneracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
