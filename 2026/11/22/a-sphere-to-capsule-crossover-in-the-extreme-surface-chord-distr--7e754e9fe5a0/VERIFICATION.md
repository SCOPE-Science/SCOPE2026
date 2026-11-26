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

For fixed a>0 the Minkowski-sum triangle inequality has equality only at the opposite axial poles, and compactness localizes the event to those charts. The quartic Taylor error is O(ε²) on the event by positive definiteness. Squeezing between the quadratic ellipsoids at thresholds ε±O(ε²) and including the O(ε) density correction yields the stated O(ε³) probability error. The four-dimensional volume, Jacobian 1/4, two ordered pole pairs and [4πr(r+a)]² normalization give 1/[4a(a+r)]. For moving a=λε, each sample point is rn+se₃ with |s|≤a, so the event forces r|n−m|>2r−ε. This uniformly localizes the second normal in an antipodal angular ball of area O(ε). The conditional probability given a cylindrical first sample is O(ε): cap directions satisfy the angular bound, and the entire band has probability O(ε). Cylinder-involved pairs are thus O(ε²). Same-cap pairs can only occur in an O(√ε) equatorial strip and are o(ε). Away from that strip, the opposite-cap distance expands as a deficit 2a(1−|n₃|)+rδ²/4+O(ε^{3/2}); positive-part angular bounds squeeze the conditional tail, and the uniform O(ε) domination controls the strip. The conditional cap normals are uniform on S² and |n₃| is uniform on [0,1], yielding the profile and the stated derivative jump. The sphere law and the recovery map and feasible range check by direct algebra. Neither argument asserts uniformity as λ→∞. The finite quadrature was inspected, not executed, and is not used as all-shape proof.

## originality

PASS

The exact spherical law is known. Moving-ellipsoid crossover work is a material conceptual precedent but uses different geometry and sampling; the closest same-body record concerns central section area. The new mathematical statement is the capsule surface-pair coefficient and especially its explicit singular crossover, not the idea of local quadratic/asymptotic estimates.

## value

PASS

A natural physical deformation changes a continuum of antipodal maximizers into a unique pole pair, so the two competing deficit exponents require different asymptotics. The sharp profile resolves this degeneracy at the natural joint scale and identifies an exact transition. The fixed-shape coefficient also identifies the two shape parameters from exact diameter and tail data. The crossover, not the elementary spherical endpoint or algebraic recovery on its own, carries the main value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
