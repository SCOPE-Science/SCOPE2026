---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

On an intrinsic Euclidean cone disk, radial area density 2r/R² and uniform shorter angular difference δ on [0,x] (x=α/2) combine with d²=r²+s²-2rs cos(min(δ,π)). Using E r²=R²/2 and E(rs)=4R²/9 gives F(x)=(9x-8sin x)/(9x²) to π and (17x-8π)/(9x²) above π, with apex-geodesic probability 1-π/x only for x>π. For the ordinary cone branch the derivative numerator G=16sin x-x(9+8cos x), G''=8xcos x, and endpoint signs prove exactly two roots x_-≈0.925373 and x_+≈2.922168 and one global minimum at x_-; the upper root is a local maximum. The exact F(7π/8)>F(π) gives three solutions for levels in (1/π,F(x_+)). For x>π, F'<0. Expansion about π verifies F is C² not C³ with third derivative jump -8/(9π²). The analytic derivation, not the finite Monte Carlo checker read in full, proves all parameter claims.

## originality

PASS

The full published 2026-11-02 cone-disk result ALREADY states the ordinary-angle moment formula and at-least-threefold inverse ambiguity on a smaller open range: these pieces are NOT new. The assessed surviving result is the exact stationary-root count/unique fixed-area optimizer, maximal exact triplicity interval, and explicit extension to abstract α>2π giving the apex-route onset and C²-but-not-C³ phase transition. The earlier proof contains no x>π statement and proves only at least three roots, not exact counts, so no stronger implication was established. Best-knowledge with incomplete external cone-geometry primary full texts.

## value

PASS

The strictly evaluated fixed-area intrinsic distance statistic is natural for conical surfaces. The exact global minimizer within embedded right cones, two critical points with exact three-to-one inverse interval, and apex-geodesic phase onset at 2π with third-derivative discontinuity form a nontrivial full qualitative classification. It strengthens the prior at-least-three ambiguity and extends beyond its geometric domain, rather than merely reprinting the already known moment identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
