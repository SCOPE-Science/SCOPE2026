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

# Verification notes

The proof supplies analytic verification of the exact law and of the asymptotic and conditional statements. Its critical steps are the exhaustive four-pattern decomposition, exact integration of the distinct-side slice, the exact separation-product integral, positive logarithmic-series coefficients, and exact simplex factorization in the central layer.

The reproducible checker is `check_parallelogram_boundary_tail.py` (Python 3; `requirements.txt` specifies NumPy and SciPy). It evaluates the near-maximal event independently by one-dimensional quadrature of geometric slice areas, comparing each result to the closed formula at \(\varepsilon=0.12,0.07,0.028\) for adjacent side ratios \(1:1\), \(2:1\), and \(5:1\). At \(\varepsilon=0.07\), each of three independent Cartesian samplings uses 1,600,000 random triples and a different parallelogram shear angle; the resulting deviations in standard-error units were about \(-0.124,-1.291,-2.442\), all inside the predeclared five-standard-error diagnostic threshold. A small-threshold check compares the first asymptotic terms. An actual execution completed with `PARALLELOGRAM_BOUNDARY_LOG_TAIL_AND_DIRICHLET_MARK_OK`.

Finite Monte Carlo tests, floating-point quadrature, and symbolic series expansion are not independent mathematical certification. They corroborate, but do not replace, the explicit proof, and they do not establish historical priority. Independent audit has not been performed.
