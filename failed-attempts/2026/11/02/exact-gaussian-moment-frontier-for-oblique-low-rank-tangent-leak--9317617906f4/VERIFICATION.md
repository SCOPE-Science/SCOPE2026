---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

In the orthogonal frames the leakage has disjoint blocks −ACBᵀ, AC and CBᵀ, with independent A=G†K and B=J†M. For any fixed nonzero c the conditional law of Ac/||c|| is mean-zero Gaussian with covariance (GᵀG)⁻¹. Multiplying by the Wishart density raises the determinant power by 1/2; the positive-definite gamma integral gives det(I+xxᵀ)^{−(ℓ_L+1)/2}=(1+||x||²)^{−(ℓ_L+1)/2}. The polar beta integral gives the stated gamma quotient and diverges at q=ℓ_L−r+1 as well as above it. A nonzero column and row of C force the left and right necessary cutoffs and give nonzero leakage almost surely; for sufficiency finite entry moments and independence bound the moment of the product block. For finite second moments the radial second moment r/(ℓ−r−1), Gaussian column symmetry and side independence give the three coefficients α, β and αβ. Finite first moments and conditional centering give zero mean when both sketches have at least one extra row. The equal-size examples and positive-tolerance oversampling bound follow by rearrangement; zero tolerance is unattainable for the stipulated nonzero Z.

## originality

FAIL

The exact frontier and finite second moment for this two-sided leakage are direct consequences of the published exact one-sided law and the already-published complementary product form of this projector. The earlier law is for the same Gaussian oblique lift acting on a fixed orthogonal residual, not merely a similar heavy-tail model. Sequential conditioning applies it without a new estimate. This is demonstrated implication, not a claim that the exact formula was printed verbatim or that a same-day/later record establishes priority.

## value

FAIL

Diagnosing infinite variance is useful for sketch design, but for this exact fixed-state diagnostic the cutoff, multiplier, and oversampling threshold follow mechanically once the previously known complementary lifts and exact single-lift law are applied. No distinct structural result, new probabilistic bound, or new regime survives that implication. The record does not establish a trajectory or adaptive-state conclusion that would require additional ideas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
