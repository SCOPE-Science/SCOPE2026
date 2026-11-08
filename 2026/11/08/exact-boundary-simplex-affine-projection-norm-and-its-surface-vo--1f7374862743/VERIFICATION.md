---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Exact formulas were derived from barycentric second moments and the facet Dirichlet mixture. `verify_boundary_simplex.py` independently recomputes the covariance identities and the kernel's negative-mass integral as rational integrals in 16 dimensions, checks a symbolic identity certifying the universal strict surface-volume inequality, and verifies the asymptotic correction constants by symbolic limits. It uses Python 3 and SymPy and requires no external data.

The analytical proof, not finite testing, establishes the all-dimensional claim, the vertex-only norming classification, the universal strict inequality and the asymptotic limit. The input sign kernel gives an attained \(L^\infty\) norm. Only regular-simplex Hausdorff surface measure or equal-facet sampling is covered. Independent scientific validation has not been performed.
