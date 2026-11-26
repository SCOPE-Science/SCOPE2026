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

The disk polynomial in w=2^(−s) has its real-part infimum on the unit circle and the stated boundary minimum. Writing x=1+cosθ and η=a/4−b gives the exact completed gap 4ηx+2bx²+2η_-²/b. The disk interior is mapped strictly into Re>1/2 even at δ=0, by nonconstancy and the harmonic minimum principle. Applying Parseval to each n^(−φ(s)) in the single prime variable and Tonelli to the basis sum gives the ζ integral for δ>0. Removing the ζ pole leaves an O(1) remainder uniform over b near a/4. The well coefficients are (a−4b)/2 (one well), a/8 (one quartic well), and 2b(1−a²/(16b²)) (two wells); a circle neighborhood at π includes both sides of the representative endpoint. Quadratic and quartic rescaling with these multiplicities gives each constant in (2). Tonelli also allows divergence of the ζ integral at δ=0, where the local reciprocal gap is not integrable. For b=a/4−κ√δ, θ=π+δ^(1/4)z, the rescaled gap yields the stated polynomial including the energy shift 8κ_-²/a on the two-well side. On any bounded z-interval positivity holds since the full denominator is at least 1; for large z inside a fixed angular neighborhood, x≍δ^(1/2)z², so the quartic term dominates the detuning and dominates the integrand by O(|z|^(-4)). The complement has a uniform positive gap. This proves the fixed-κ limit and justifies integrating on the whole line. Scaling the even quartic integral to x⁴+βx²+1 and averaging the integrals related by x↦1/x reduces it via x−1/x to the elementary quadratic integral; this verifies (4) including its critical value.

## originality

PASS

The supported distinction is the sharp same-prime transition, particularly the positively translated two-parameter profile through merger of the contact points. Quartic contact for the critical symbol itself is already known; Parseval, the Schatten trace method and divergence at the contact are not the originality basis. The retrieved membership and norm papers and indexed distinct-prime asymptotics do not supply the double-scaling profile.

## value

PASS

In the simplest correlated two-harmonic model one contact minimum changes into two. The exact square-root detuning scale and its normalized Hilbert–Schmidt profile resolve behavior not visible in pointwise contact orders or membership criteria. The correction for the shifted minimum on one side is essential and permits a meaningful comparison of the two regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
