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

Rayleigh–Ritz plane minimization of Q has symmetric compression [[e,√e c],[√e c,D]], so new error is its smaller eigenvalue and normalized multiplier has rationalized form 2(D−c²)/(e+D+sqrt((D−e)²+4ec²)). Coupled Gaussian tangent at e→0 gives (Z₂²+⋯+Z_m²)/(Z₁²+⋯+Z_m²), Beta((m−1)/2,1/2). Multipliers are bounded in [0,1]; O(r)×O(m) symmetry makes conditional kernels functions of e only. Since e_{j+1}≤e_j, uniform small-e convergence and induction yield k independent beta limits at each fixed horizon and the gamma-moment formula. Independent Gaussian calculations checked mean and second moments in three codimensions (20,000 samples each), not a substitute for the limit proof.

## originality

PASS

Best-of-knowledge PASS: Bresch–Melnyk global linear convergence with a positive top spectral gap treats a simple leading eigenvalue, not a rank-r≥2 repeated leading eigenspace. Earlier random-plane algorithm and generalized Rayleigh quotient papers give method and general rates but no identified local beta multiplier law or fixed-k independent product. Similar beta errors in Gaussian Krylov/linear-system algorithms arise under different projection kernels and do not prove this Rayleigh–Ritz claim. Full inaccessible relevant primary text remains a residual priority risk.

## value

PASS

Exact local beta multiplier law is a natural stochastic refinement of mean convergence for random-plane eigenvalue ascent when the top eigenvalue is degenerate, beyond existing simple-top spectral-gap analysis. Rank-independent beta shape, all moments and fixed-horizon iid product supply precise, reusable error-distribution information; motivated structural theorem, not a chosen finite test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
