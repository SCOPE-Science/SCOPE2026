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

The frozen ellipsoid theorem was correct, but the law on sizes 0 and 2 for a block of size 3, for instance, assigns no mass to its singleton or full-set vertices, contrary to the full-support reading of the contribution statement. The repaired RESULT.md explicitly mixes each sparse law 3:1 with the uniform Boolean law. The latter has the same one- and two-coordinate moments; every nonzero contact has positive weight, and each weighted empty-set contribution before subtracting 1 exceeds 1/2 (at least 9/16 for even block sizes and 3/4 for odd ones). Thus the final measure really has full support. Independently, the Boolean vertex gauge is constant on each block because the linear coefficient in the weight vanishes, and the origin has unit gauge. The inverse relation HΣ=I/n holds on the contrast spaces since (q+1)wa/2=(p+1)wb/2=1/n. On normalized constant vectors, Σ is (p+1)(q+1)/(4(n+1)^2) times the matrix with diagonal p+1,q+1 and off-diagonal −√(pq), giving exactly the inverse of the precision restriction divided by n. This also covers one-element blocks, which have no contrasts. Independent rational tests checked the two-dimensional restriction for (1,1),(1,3),(2,3),(2,2),(7,10). Averaging containment and using determinant AM–GM proves global uniqueness, and the determinant and orthogonal order-polytope reflection agree. The revised verification paragraph distinguishes the finite Boolean gauge checks at p+q≤12 from the larger covariance test. The uploaded verifier was inspected, not run.

## originality

PASS

The supported distinct claim is the outer ellipsoid in the unequal regime, together with an explicit full-support contact design. The balanced formula is known and explicitly not credited as new. The nearest inner result, symmetric direct-sum law, and general optimization formulation do not supply the evaluated one-sided unequal case. The repaired full-support certificate does not change the object or covered range.

## value

PASS

The unequal family is the natural two-rank extension of the balanced chain-polytope problem, not an arbitrary cutoff. The exact center, cross-block precision and volume answer outer-ellipsoid questions unanswered by the inner optimizer. Proving that boundary contact persists at every vertex despite asymmetry, and furnishing a usable positive-mass design with only two inclusion moments, makes the formulas reusable without numerical optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
