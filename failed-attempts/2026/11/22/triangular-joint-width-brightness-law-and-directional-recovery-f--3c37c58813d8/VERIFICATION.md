---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

With Λ=diag(λ_i) the squared support function is uᵀΛu and the determinant of the projected ellipse matrix on u-perp is uᵀadj(Λ)u, giving the claimed normalized area squared. Squared Haar coordinates are normalized independent gamma variables of shape 1/2. The columns v_i−v_3 equal (λ_i−λ_3)(1,−D/(λ_iλ_3)) for i=1,2, so their signed determinant is minus the Vandermonde in the stated order. Dividing the normalized Dirichlet density by its absolute value gives the stated planar density, with full closed-triangle support and the open-edge singularities. The extreme-point abscissas recover λ_i, and an interior point uniquely gives all three strictly positive squares and eight signs, modulo simultaneous negation for lines. From E[P_i²]=1/5 and E[P_iP_j]=1/15, the covariance is −2D((Σλ_i)(Σ1/λ_i)−9)/45, whose bracket is exactly the sum of squared differences divided by products. Coincident knots aggregate Dirichlet parameters, giving the isolated-coordinate Beta(1/2,1) segment or the sphere point mass.

## originality

FAIL

A decisive lawful 2014 primary source was inspected. Dunkl et al.'s real numerical-shadow formula gives the distribution of every linear projection of this pair, and its Dirichlet-spline model specializes directly. There is no assertion that the exact ellipsoid terminology or the displayed physical formula appears verbatim there. The complete claim follows mechanically by substituting the two classical geometry forms, inverting a full-rank simplex map, and expanding its moment formula.

## value

FAIL

The common-direction ellipsoid experiment is natural and the worked physical example can be useful pedagogically, but all exact conclusions are routine consequences of the previously supplied real numerical-shadow model once width and orthogonal projection are written as their classical quadratic forms. The inverse, repeated-axis behavior and covariance do not give a surviving independent mathematical result beyond that specialization. There is no new estimation, stability, or noncommuting tomography result in the finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
