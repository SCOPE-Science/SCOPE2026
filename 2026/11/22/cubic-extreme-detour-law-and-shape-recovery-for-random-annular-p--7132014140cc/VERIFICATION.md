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

Replacing just the intercepted subchord of length c by its minor inner-circle arc gives d_K≤d_E−c+(π/2)c. Equality at π/2 requires c=d_E and an inner diameter, and antipodal inner endpoints do attain it. For small d_E the arc excess is O_r(c³), so the ratio extends continuously to the diagonal by 1; the global comparison and triangle inequality also give continuity of d_K in the endpoints. Compactness then confines sufficiently extreme pairs to a neighborhood of inner antipodes. The tangent-plus-arc formula in that neighborhood can be checked by a lower bound on every path: if its minimum radius is q, polar arclength is at least √(1−q²/ρ_path²)|dρ_path|+q|dθ|. Integrating gives at least qφ plus the sum, over endpoint radii b, of √(b²−q²)−q arccos(q/b). This bound is increasing in q≥r when φ exceeds the sum of the two tangent angles at r, and the path with q=r, two tangents and the intervening arc attains it. Thus with u=(ρ−r)/r, v=(σ−r)/r and η=π−φ, the numerator in units of r is π−η+F(u)+F(v), F(z)=(2√2/3)z^{3/2}+O(z^{5/2}); the chord is 2+u+v+O((u+v)²+η²). Dividing gives deficit (π/4)(u+v)+η/2 with a uniformly smaller remainder. Once localized, this confines u,v,η to O(ε). After rescaling as in the marks, the event is sandwiched between positive-octant simplexes of sizes 1±O(√ε). The independent polar density is 4r⁴(1+u)(1+v)/(πH²), and the rescaling Jacobian is 32ε³/π². The volume 1/6 yields 64r⁴/(3π³H²); the boundary layer contributes O_{r,R}(ε^{7/2}). Normalizing the same integrals gives density six on the limiting simplex. Finally s=√(3π³C/64)=r²/(R²−r²), proving the scale-free inversion.

## originality

PASS

The distinct result is the upper tail of the ratio for area samples, with a sharp coefficient and error and its marked law and aspect-ratio recovery. The circular-obstacle path geometry and elementary dilation bound are background. The strongest prior annulus result uses essentially related simplex-tail analysis, but for the intrinsic distance marginal, with outer rather than inner extremizers and a different coefficient. A same-day group of geometrically different stretch theorems was also compared, without using the common date as evidence of priority.

## value

PASS

The ratio measures how much a hole can lengthen a trip relative to the chord, rather than which pair has the longest trip. Quantifying the chance of near-worst distortion, the geometry of the pairs producing it, and the dimensionless shape information encoded by that chance is worthwhile beyond the deterministic upper bound. The inner-rim extremal locus contrasts with the outer-rim distance maximum. The exact coefficient, rather than the cubic exponent alone, makes recovery possible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
