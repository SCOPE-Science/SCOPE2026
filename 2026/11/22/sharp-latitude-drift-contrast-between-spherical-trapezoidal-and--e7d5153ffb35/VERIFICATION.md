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

Azimuthal equivariance reduces the two discrete schemes to scalar height maps. Using the spherical exponential C p+S(e3×p), with C=cos(tρ), S=sin(tρ)/ρ and ρ²=p_x²+p_y², I checked the sixth-degree vector Taylor coefficients in exact rational arithmetic, using the squared norm of the sum for the normalized midpoint and (2−||q_f−q_c||²)q_f−q_c for the extrapolation. With m=1−c², the two height multipliers are 1+m(2m−1)t⁴/8+m²(2−m)t⁶/24 and 1−m(1−m)t⁴/8+m²(1−m)t⁶/24, where t=ωh. Reflection reverses t without changing height, so the analytic remainders start at order eight. Uniformity near fixed interior c permits scalar telescoping over N=T/h. The per-step deviation satisfies |δ_{n+1}|≤(1+C h⁴)|δ_n|+O(h⁴) generally, with forcing O(h⁶) at c²=1/2 because the fourth-degree coefficient vanishes there. This gives δ_n=O(h³) or O(h⁵), respectively, and proves all three stated limits. Differentiating u³(1−u²)/8 gives the maximum at u²=3/5 and value 3√15/500 after factoring out Tω⁴. At the poles the vector field vanishes, and at the equator the stages and the local geodesic remain in the equatorial plane.

## originality

PASS

The methods themselves and their position convergence are prior. The supported distinct claim is the invariant-specific leading coefficient and sign contrast for rigid rotation, with the exact exceptional fifth-order term. No available matching statement covers those claims; the most relevant primary full texts could not be confirmed, so this is a bounded assessment.

## value

PASS

Height is a natural exact first integral for the canonical rigid-axis flow. The result distinguishes two norm-preserving, second-order schemes in a property that their position order leaves undecided, quantifies the largest Richardson drift, and resolves a nontrivial cancellation latitude including its first surviving term. This supplies a precise benchmark for invariant preservation, not a claim of better position order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
