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

# Verification of the spherical-sector boundary law

The mathematical proof uses the spherical volume Jacobian \(d\sigma=\tfrac12\,dT\,du\,dv\), four inward geodesic facet margins, and the exact integration over the uniformly distributed \(T\). The upper-support endpoint is obtained from the harmonic combination \(q=A^2B^2/(A^2+B^2)\). Its local positive interval has a linear-linear, quadratic-linear, or quadratic-quadratic shape according to the number of merged facet pairs. Each local domain is compact after the indicated rescaling, permitting dominated convergence. In the interior case the limiting three-dimensional polytope is affinely the standard simplex, which proves the four-slack Dirichlet law in total variation.

The self-contained `checker.py` computes the exact angular integral by high-order Gauss–Legendre quadrature and compares finite-deficit values to all three sharp coefficients, the direct hemispheric formula, and both critical crossover expressions. With Python, NumPy and SciPy installed, execute `python checker.py`; a complete run prints `ALL_CHECKS_PASSED`. The checker is a numerical diagnostic, not a formal proof or independent certification.

The statement does not extend without further work to nonorthogonal spherical polyhedral joins, general curvature, arbitrary boundary sampling, or unbounded crossover parameters. Historical priority remains provisional because an unlocated general spherical inner-parallel-volume result could overlap. No independent audit was performed.
