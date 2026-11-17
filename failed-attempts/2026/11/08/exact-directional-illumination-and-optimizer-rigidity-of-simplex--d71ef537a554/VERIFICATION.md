---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The type-A root polytope P_n=conv{e_i-e_j} is the simplex difference body with facets sum_{i in S}x_i<=1. At root e_i-e_j, a direction v illuminates iff v_i<0<v_j and -v_i+v_j>T(v)=sum_{v_l>0}v_l. Two illuminated roots with distinct tails and heads would contradict the two available sign masses, hence an illuminated graph is a star of size at most n-1. Explicit n full tail stars cover the boundary, while fractional vertex-coverage summation yields lower bound n. Equality forces all positive-weight directions to be full stars; off-diagonal constraints alpha_i+beta_j=1 on connected K_{n,n} minus a matching give alpha_i=t,beta_j=1-t. This establishes exact I=I*=n and the stated optimizer rigidity for n>=3. The complete earlier 2026-10-25 proof was inspected and contains precisely the same argument and quantifiers. Source integer checker also independently inspected; independent small-dimensional active-facet reasoning corroborated the star criterion.

## originality

FAIL

FAIL decisively: an October 25 2026 published finding, 'Exact illumination and optimizer rigidity for type-A root polytopes', proves the identical theorem for R_m=conv{e_i-e_j}, including both ordinary/fractional value m, the exact one-positive/one-negative star criterion, the aggregate t/(1-t) family and only two optimal ordinary patterns. Its proof explicitly identifies the difference body of every nondegenerate simplex. Renaming n to m or choosing alternate examples gives no surviving original claim. Full prior mathematical proof read; this is not a snippet-only inference.

## value

PASS

The exact illumination numbers and incidence optimizer classification for a natural all-dimensional centrally symmetric root-polytope family are mathematically motivated and structurally useful. Intrinsic value survives, but the complete prior publication defeats originality of this submitted claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
