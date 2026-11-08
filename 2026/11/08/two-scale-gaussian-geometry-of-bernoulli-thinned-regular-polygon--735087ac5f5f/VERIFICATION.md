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

`verify_polygon.py` uses the standard Python library alone. Its geometric checks evaluate every nonempty subset of radius-one regular \(N\)-gons for \(3\le N\le9\), comparing Cartesian shoelace areas and chord lengths to the exact cyclic-gap formulas. It also checks the deterministic fifth-order gap cancellation against a rigorous Taylor envelope for additional random samples. Exact fraction arithmetic verifies the geometric moment values \((\rho_3,\rho_5,\sigma_{33},\sigma_{35},\sigma_{55})=(13,541,3240,465480,98058600)\) when \(p=1/2\), as well as their strictly positive determinant \(101038233600\).

An independent Monte Carlo exercise with 3,600 samples on the 2,500-vertex polygon compares rescaled cubic- and quintic-gap rewards against the analytical covariance. The checker concluded with `BERNOULLI_POLYGON_TWO_SCALE_CHECKS_PASSED`; this finite diagnostic does not prove asymptotic weak convergence or exclude a prior equivalent result.

The proof supplies the infinite statement by geometric renewal coupling, a multivariate renewal-reward CLT, moment control, a maximum-gap bound, and polynomial support rigidity. Historical priority remains provisional; no independent mathematical audit has been performed.
