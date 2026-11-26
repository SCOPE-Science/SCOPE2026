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

Normalizing independent Gaussian pairs in the two planes gives the uniform squared plane radius T and independent angular coordinates; conditioning on the sectors retains those properties. Distance to the complement of the hemisphere intersection is the minimum inward margin, and folding each angle chooses the lesser sine for apertures ≤π. The two inequalities on T give exactly the asserted positive interval length. Its maximum is at the two half apertures, giving q and inradius ρ. For endpoint asymptotics I bounded the positive support using convexity of csc² at fixed subhemispheric aperture and sec²(d+δ)−sec²(d)≥δ²+2dδ near the hemispheric limit, where d is the half-aperture deficit and δ the folded-angle deficit. This gives bounded rescaled domains and a rigorous dominated-convergence argument. The limiting interval lengths are the stated positive parts with linear or quadratic terms; integrating gives H³/(6c_ac_b), 4H^(5/2)/(15c_b√q), and π before the folded-angle factor 4/(αβ), hence the three coefficients. For moving d=λ√h/2, expansion of the difference of sec² values gives h(x²+λx) when δ=√h x. Centering at the moving ρ before expanding gives the two window integrals, also at zero window parameters. The description 'Gaussian-quadrant integrals' in the last proof line of this part is imprecise: these are compact positive-part polynomial integrals. For the both-hemisphere case the normalized marginal density of X₂=s≥0 is (4/π)√(1−s²), and the conditional X₄ is uniform on [0,√(1−s²)]. Differentiating both sin t cutoffs and integrating verifies the exact closed form including the endpoints. For fixed subhemispheric apertures the rescaled conditional density is constant on bounded domains whose indicators converge in L¹ to the indicator of Ω. The affine four-slack map yields uniform measure on the simplex, giving the claimed TV convergence and Dirichlet limit. Full analytic replay: /workspace/calculations/geometric_checks.md. The frozen quadrature code was inspected, not executed; finite samples are not certificates for the limits.

## originality

PASS

The distinct result is the joined two-sector law and its full classification, particularly the aperture-dependent coefficients, the single/double square-root merger windows, and the four-slack marked law. The exactly both-hemispheric tail formula and its quadratic endpoint are demonstrably covered by the distinct same-day spherical-lune result at a right-angle aperture, so those are not credited as independent originality. This mathematical coverage does not establish priority order within the day. Standard inner-volume, local-scaling and simplex arguments also are not claimed as new.

## value

PASS

For a tractable spherical family with distinct or coalescing facets, the problem identifies exactly how clearance near the inradius changes, and gives both moving-aperture profiles and a conditional shape law. Those describe a quantitative loss of the fixed-aperture regime that plain width or a static tail exponent cannot capture. The value rests on the coupled two-sector classification, not on reevaluating the already covered right-angle-lune tail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
