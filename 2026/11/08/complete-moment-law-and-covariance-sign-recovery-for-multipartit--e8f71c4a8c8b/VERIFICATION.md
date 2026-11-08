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
# Reproducibility checks and boundaries

Run `python geometry_stable_set_moment_checker.py` with the requirements listed in `requirements.txt`. The script builds all stable-set vertices from part sizes, invokes an independent convex-hull triangulation, calculates simplex volumes and first/second moments by exact rational arithmetic, and checks the resulting covariance signs and inertia. It also expands barycentric polynomials to integrate arbitrary specified cubic and quartic monomials exactly.

The script was executed from its actual local file path and returned:

```
MULTIPARTITE_STAB_EXACT_SIMPLEX_MOMENTS_PASSED 17 653
MULTIPARTITE_STAB_ALL_MOMENTS_CUBIC_QUARTIC_CHECKS_PASSED 368
```

The first marker corresponds to 17 unordered part-size profiles in dimensions 2 to 5 and 653 nonzero hull-to-interior simplices. The second counts 368 distinct checked monomials of degrees three and four in dimensions 2 to 4. The script skips zero-volume simplices arising from some triangulated nonsimplicial faces. All algebraic computations use `sympy` rational expressions; Qhull determines a proposed boundary triangulation, whose integration is done over exact rational vertex coordinates.

These finite checks do not prove the all-dimensional or arbitrary-order theorem. The proofs of the density, moment formula, covariance signs, and Schur extrema are analytical and appear in `RESULT.md`. No independent mathematical audit has been performed.
