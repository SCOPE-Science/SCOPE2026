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

For S³, the zonal normalized Gegenbauer/U_ell character is sin((ell+1)t)/((ell+1)sin t) and polar density sin²t, so for ell≥1 the averaging multiplier equals [sin(ell θ)/ell−sin((ell+2)θ)/(ell+2)]/[2(ell+1)V(θ)], V=θ/2−sin(2θ)/4>0. Vanishing at rational θ/π transforms, with n=ell+1≥2 and z=e^(2iθ), to P_n(z)=(n−1)z^(n+1)−(n+1)z^n+(n+1)z−(n−1). If four-term rational root-of-unity relation reduces, equal coefficient sizes force paired cancellations and z²=1; if irreducible, Mann's four-term theorem forces order(z)|6. Direct exact cyclotomic reductions at orders 1,2,3,6 exclude all except z=−1 with n odd. Hence all nonhemispherical rational cap angles have nonzero harmonic multipliers, while θ=π/2 kills precisely positive even ell; completeness of S³ harmonics identifies the full kernel. Multipliers decay O_θ(ell^(−2)), so injectivity does not imply a bounded inverse. Ends θ=0,π and irrational θ intentionally excluded.

## originality

PASS

PASS qualified: earlier geometric-tomography and harmonic cap-transform work treats generic injectivity and some rational heights, and already explains hemisphere loss of even harmonics. The inspected Kiderlen text cites Rubin's rational-radius estimates but explicitly does not establish all rational S³ apertures with the sole hemisphere exception. This exact if-and-only-if arithmetic classification, based on Mann's theorem and finite order6 exclusions, is not a direct corollary of the located prior statements. An inaccessible/unindexed stronger spherical-means result remains a residual priority risk, not itself proof of coverage.

## value

PASS

PASS: Cap averaging is a basic rotationally invariant smoothing/measurement operator, and which rational apertures lose harmonic information is a natural structural problem. The theorem gives a complete rational family injectivity dichotomy, an infinite-dimensional exceptional nullspace, and clarifies non-stable inversion. It involves nontrivial roots-of-unity arithmetic beyond routine spherical harmonic diagonalization; the exact rational boundary can be used directly in spherical imaging/tomography.

The dated certificate retains the supplied scientific assessment, sources and limitations.
