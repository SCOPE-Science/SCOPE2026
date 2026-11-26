---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Gaussian regression minimizes the displayed exact quadratic risk since the marginal noise matrix is positive definite. Nonnegative regression cross-covariances and right-hand sides rule out both weights being negative; when both are nonnegative, each positive weight is strictly below 1/2. The site Hessian has positive determinant 4uv(1−u−v) for positive weights, and its feasible minimizer is a=(1−v)/2, b=(1+u)/2. Independently, writing p=u+v and j=uv, the minimized risk is 1/12−p/4+(1/4+η)p²−j[p/4+2η(1−ρ)]; the same formula holds on the axes, where the unused site is irrelevant. At fixed p, equality of weights uniquely maximizes j. The strictly convex diagonal profile has the stated smaller root w and gain (w−w³)/4. For a negative weight, strict site concavity forces collision or a pinned endpoint; collision has equal nonnegative weights and is strictly worse than the symmetric optimum. Conditioning on endpoint noise leaves variance η(1−ρ²), uniquely optimized at the midpoint; the zero-weight cases cannot tie, since unequal nonnegative weights lose strictly and both zero yield no gain. Thus only the stated geometries attain the maximum, including all three at a tie up to label order. The symmetric gain decreases and the reference gain increases with ρ, and at ρ=1/2 the reference equals the repeated-midpoint benchmark and loses strictly. Comparing their limits at ρ↑1 gives η_c and the crossing if and only if η>η_c. For each fixed ρ>1/2 their large-η gain ratio tends to 2(1−ρ)<1, which together with the lower bound ρ_c>1/2 proves the large-noise limit without interchanging a moving critical point with a nonuniform expansion. The low-noise endpoint limit follows by continuity and the strict inequality at every ρ<1 when η=η_c. Independent bisection reproduced the quoted sample crossings. No assertion includes ρ=1, negative correlation, or more queries.

## originality

PASS

The independent-noise optimum, the endpoint benchmark and a limiting high-noise transition at 1/2 are already represented in distinct records. The surviving claim is the finite-η global optimization over all site pairs, including the positive onset η_c, exact critical curve and exhaustive tie geometries. The strongest inspected overlapping statement does not give this finite-parameter characterization. Same-day catalog dates are not used as evidence of priority.

## value

PASS

An exhaustive finite-parameter optimal-design theorem for a canonical Gaussian integration problem goes beyond a pairwise benchmark or high-noise expansion. It explains when a measurement carrying zero signal is globally preferable as a correlated-noise reference, gives the exact onset and ties, and rules out all intermediate geometries. This is a substantive finite-noise design conclusion even with only two fixed queries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
