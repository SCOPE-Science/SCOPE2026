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

Reconstruct the weighted matrix-tree identity sum_T product_w x_w^{deg_T(w)}=(prod_w x_w)S^{r-2}prod_i(S-S_i)^{n_i-1}, noting r=2 works by S^0. Dividing by the count realizes excess degrees as independent categorical one-hot allocations, yielding covariance -(r-2)/N² minus (n_i-1)/(N-n_i)^2 over parts excluding both marked vertices. For f(s)=(s-1)/(N-s)^2, strict increasing convexity and g(s)=f(s)+1/N² strict superadditivity concentrate all nonmarked vertices in one N-2 part. Same-part pairs are strictly weaker; K3 versus K1,2 boundary checked separately. In extremal host, one binomial allocation and a single multinomial allocation give variance (N-3)/4+(N-1)/N² and covariance -(N-3)/4-1/N², so the correlation rate follows. Independent Prüfer enumeration across 40 hosts N<=7 and 4,063 bounded assertions corroborated the formulas.

## originality

PASS

PASS best knowledge for the universal sharp covariance envelope, sole extremal complete-multipartite composition and near-perfect anticorrelation rate; NOT a claim of originality for the classical multipartite tree enumerator or its degree-generating function.

## value

PASS

The unique optimizer K_{1,1,N-2} is a natural all-host extremal theorem for dependent random tree vertex degrees; the exact bound and N^-2 approach to perfect anticorrelation quantify a sharp probabilistic geometry not supplied by counting formulas alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
