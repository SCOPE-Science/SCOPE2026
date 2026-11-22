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

PASS: Reconstructed the actual two-site bisector and the corner-triangle area T=(a sqrt(p/q)+b sqrt(q/p))^2/2, carefully retaining the p<a and q<b constraints and fixed rectangle bounds. Face-reaching caps have O(t^4) four-dimensional measure, negligible against O(t^2). With A=a sqrt(r), B=b/sqrt(r), r=p/q, c=sqrt(2t), the (a,b,p,q) Jacobian is q and the triangular wedge has one-corner/one-label measure c^4/48=t^2/12. The site-pair-to-(mean,half-difference) determinant is 4 and there are 8 classes, yielding 8/3 after normalization by S^2. The normalized density factors into Dirichlet(2,2,1), lambda density min(lambda,lambda^-3), and uniform j; Dirichlet factorization and ell=log lambda give the four stated independent laws. Fixed-rectangle indicators tend to one almost everywhere under the integrable scaled density, proving L1/TV convergence, not just weak convergence. Finite clipping and Monte Carlo are corroboration only; no uniformity over changing aspect ratios is established.

## originality

PASS

PASS qualified: Fixed-n=2, rectangle-clipped *minimum of two cells* with a six-coordinate conditional law is not implied by the accessible many-site typical-cell limit, Poisson line small-cell shape laws or two-point random-ball midpoint formulas. The source event and sampling law differ materially; no searched exact two-site rectangle formula matching coefficient and factorized marks was found. This is a best-of-knowledge assessment, not a proof of historical priority; unindexed finite-site formulae remain possible.

## value

PASS

PASS: The natural small-cell problem is the stochastic-geometric small-cap tail for a finite point sample. The universal 8/3 coefficient is independent of the rectangle aspect ratio and its complete four independent Beta–Laplace–uniform marks describe a nontrivial geometric mechanism invisible to scalar area tails; a researcher investigating fixed-site Voronoi rare events could use the exact multivariate law. It is not a renamed Poisson-cell theorem or a tiny arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
