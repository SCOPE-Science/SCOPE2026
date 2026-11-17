---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

In the actual RESULT.md the first-jet distance delta=-2F^2+||grad F||^2/3 is reduced in meridian coordinates to explicit rational N/(1+u^2)^3; derivative P and angular derivative -4(c+2u^3) at b=0 were checked symbolically. Seven classes yield 30 simple critical points by stated exact nonzero Hessian determinants. Each of six degenerate equatorial critical points splits into two simple points because P/u has derivative -24c and b derivative 8 at origin. Each polar chart has four nondegenerate stationary points of Q_sigma=4(X^2+Y^2)-8sigma(X^3-3XY^2), so total 30+12+8=50 persistent real simple points by IFT for small epsilon>0. A generic coefficient perturbation intersects the known Zariski-open complex-count-50 locus. The source verifier checks polynomial/Hessian identities; independent symbolic meridian and splitting checks corroborate. No numerical epsilon bound claimed.

## originality

PASS

The motivating Kozhasov–Mourrain–Parusiński 2026 first-jet discriminant article supplies the exact complex critical point count 50 and poses all-real attainment, whereas Kozhasov 2018 concerns fully real tensor eigenconfigurations (critical points of F itself), not the first-jet discriminant distance. A targeted Resultary semantic query found only this record with the full 50 first-jet claim; similar examples about cubic Newton systems and discriminants use different functions. Full motivating paper was not retrieved through available arXiv/OA routes and Oxford VPN disconnected; theorem/problem numbering is supported by inspected source package but not independently confirmed in primary full text. Residual specialist-priority risk is stated; no decisive covering result found.

## value

PASS

The first-jet discriminant distance is a natural geometric optimization invariant. An explicit perturbative real family making all fifty complex critical points real and nondegenerate answers a specific all-real sharpness case for ternary cubics, with an open coefficient neighborhood, a meaningful unresolved geometric gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
