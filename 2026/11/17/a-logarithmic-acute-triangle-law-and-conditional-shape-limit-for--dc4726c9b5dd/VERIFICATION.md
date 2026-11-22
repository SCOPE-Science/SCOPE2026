---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Actual arclength projection density is sqrt(1+epsilon²x²/(1-x²))/Iepsilon, with nonnegative exceptional mixture mass O(epsilon² log). For sorted uniform-x triples, density is 3/4 and the middle-angle dot product forces st<4epsilon². Same-branch and one-neighbor-matching sign patterns contribute lower order by the global half-Holder sqrt(1-x²) bound. In the two opposite-middle patterns the middle positivity is st<4epsilon²(1-x²)+o(epsilon²) on compact interiors; integrating the hyperbolic region gives area 8epsilon²(1-x²)log, then 3/4 times 2/8 and integration over x gives precisely coefficient 2. The other two vertex angles exclude only O(epsilon²) layers. Jacobian of s=epsilon^lambda, t=4epsilon²(1-x²)u/s yields product conditional law. Exceptional arclength draws enter the acute event only O(epsilon^4 log²), so transfer of conditioning is legitimate. All error orders are as epsilon->0, not claimed finite-epsilon exactness.

## originality

PASS

Best-of-knowledge original as an exact statement/implication after direct comparison of primary material and relevant published mathematical results; significant inaccessible or indirect antecedents are retained below rather than equated to novelty proof.

## value

PASS

The acute event is a natural rare geometric property of thin convex curves with different eccentric-anomaly versus physical-arclength laws. It identifies both sharp singular logarithmic coefficient and the complete asymptotic conditional shape; these are useful beyond the previously available unevaluated finite-eccentricity perimeter integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
