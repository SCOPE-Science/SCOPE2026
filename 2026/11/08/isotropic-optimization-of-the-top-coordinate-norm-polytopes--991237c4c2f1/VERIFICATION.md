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

# Reproducible verification

Run `python check.py` with Python 3.10+ and the installed NumPy, SciPy, and SymPy dependencies. This file is packaged alongside that standalone checker. The checker was executed from this source and returned `TOP_K_NORM_ISOTROPY_CHECKS_PASSED`.

The checker independently verified 91 exact-rational ordered-gap chamber formulas in dimensions 2 through 14, symbolic differentiation and the asymptotic function, 69 dimensions of finite candidate classification, and 12 independent exact-rational convex-hull integrations in dimensions 2, 3 and 4, assembling 526 facet simplices. The latter method first determines hull simplices numerically with Qhull, then integrates the selected simplices with exact rational determinant and moment arithmetic. Exact agreement was obtained between these integrals and the separate ordered-gap calculation. The geometric combinatorics in those 12 tests have finite scope; no exhaustive all-dimensional checking is claimed.

The mathematical proof depends on the convex-hull gauge identity, simplex Jacobian, Dirichlet moment identity, sign analysis of explicit quadratics, and Stirling limit; these are presented in `RESULT.md`. Computational tests corroborate the algebra but do not prove the universal theorem or historical originality. Independent mathematical audit has not been performed.
