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

The support maximizer for t=|u_d| is unconstrained when t≤a and is on the rim of the slab otherwise, giving H_a(t)=at+b√(1−t²) on that branch, with quadratic loss (t−a)²/(2b²) at contact. Projection preserves support on the unit sphere of E (the intended domain of the sphere integral). The in-plane axis length is s=sinθ, so support is averaged against the absolute coordinate distribution of that sphere. This gives the whole profile and strict decrease for s>a. The plateau is exactly the ball event and sin²θ has the stated beta law; pushing forward the acute-angle measure gives the continuous CDF and the unique jump. In the coordinate integral set sz=a+δv, δ=s−a. The resulting beta moment ∫v²(1−v)^(α−1)dv is B(3,α); δ∼bη gives the quoted contact constant. Differentiating the integral with the same substitution and H'_a(a+h)∼−h/b² gives a derivative of order η^(α+1) with coefficient (α+2)κ, justifying the density exponent, not merely the integrated mass. At s=1 the derivative majorant is (1−z)^((d−5)/2), integrable for d≥4. In d=3 the localized derivative integral has divergent part (2b/π)∫dφ/√(1−s²+φ²), with bounded error, giving (b/π)log(1/(1−s)). Integrating and using 1−s∼η²/2 gives the stated logarithmic gap and its inverted probability constant. Direct planar integration recovers the minimum, and the top support and atom invert R and a by scaling and the strictly increasing beta CDF.

## originality

PASS

The supported distinct claim is the mixed mean-support law for a centered spherical slab, with the sharp contact coefficient and dimension-sensitive side-on endpoint. General support/projection identities and the occurrence of contact exponents or logarithms in other bodies are not credited as new.

## value

PASS

At a positive fraction of views a nonspherical convex solid has an exactly round shadow; the continuous remainder starts at a computable fractional contact power and ends at a dimension-dependent geometric singularity. The resulting law distinguishes the two mechanisms and identifies both radius and thickness from population data, giving a motivated exact benchmark for inverse convex geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
