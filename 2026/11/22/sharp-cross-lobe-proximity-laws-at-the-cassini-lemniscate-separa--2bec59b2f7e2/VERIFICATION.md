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

For independent area-uniform points in the specified opposite lobes, A_0=1/2 by polar integration and A_q→A_0. The axial quartic gives the exact tip gap: dropping y² from the left and adding it on the right forces x⁴≤x²−q², with the lower axial root attainable at y=0. In the opposite cones the dot product is nonpositive, so a pair at distance <R has both norms <R. At q=0 the missed angular strips on this bounded rescaled domain have width O(ε²); the cone-coordinate integral (1/4)∫_{A,B≥0,A²+B²<2} AB dA dB equals 1/8. This proves the ε⁴/2 coefficient, its O(ε⁶) remainder and conditional TV convergence by normalization of indicator densities. Scaling by q gives x²−y²≥1+q²|(x,y)|⁴, so localized dominated convergence yields 4Φ, including the zero region λ≤2, and TV for λ>2. Integrating horizontal depths gives the claimed triangular-area integral. Near λ=2+δ the depths are O(δ) and transverse coordinates O(√δ). In m=(s+t)/2,d=s−t coordinates the quadratic distance term is m²+d²/2 with unit Jacobian from (s,t); half the integral of its squared positive deficit is πδ³/(3√2). Scaling H± by 1/λ recovers the cone integral for the large-λ tail. The critical limit is for fixed λ; the onset is a subsequent limit, not uniform down to the finite-q tip gap. Bound verification notes and Python verifier were inspected, not executed; the independent reproduction is the exact integrals and localization argument above.

## originality

PASS

Pass the distinct Cassini cross-lobe cone and fixed-λ hyperbolic crossover with conditional laws. Credit the cubic edge as an instance of a shared smooth positive-curvature local normal form, not as a separately original contact exponent or constant. The earlier smooth result has a different original scaling, and does not supply the full hyperbolic profile or transverse cone law.

## value

PASS

A natural topology-change geometry gives a quantitative and useful rare-event benchmark: the exact normalization and conditional law at the touching point, and the full q-scale connection from the gap to the cone. These determine more than an exponent or a numerical constant and distinguish transverse from smooth contact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
