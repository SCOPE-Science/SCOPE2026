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

# Verification record

The complete geometric law is reconstructed in RESULT.md from a nearest-face projection and a Gaussian/Beta factorization. Exact normalization is checked at zero and at the maximum, and the hemisphere is handled by a separate beta tail rather than by substituting into the fixed-opening asymptotic. All incomplete beta functions in the moment formula are unregularized, except the explicitly identified regularized hemispherical survival function. The marked laws are conditional total-variation limits proved by convergence of rescaled densities in \(L^1\).

`checker.py` was executed with Python 3, NumPy and SciPy. It reported: `PASS 5186 independent numerical assertions; analytic proof in RESULT.md`. These cover sampled geodesic nearest-face distances, distribution quadrature, second moments, exact hemisphere beta distribution, tail coefficients, aperture ordering and critical crossover. No analytic claim is derived solely from the numerical tests. Independent mathematical auditing and independent validation are not performed.

The geometric data are restricted to round spheres, surface-uniform sampling, integer dimensions at least three and lune opening no greater than \(\pi\). The historical priority comparison remains provisional, particularly with respect to classical spherical inner-parallel geometry. The scientific proof and numerical checker use no third-party paper text as an executable dependency.
