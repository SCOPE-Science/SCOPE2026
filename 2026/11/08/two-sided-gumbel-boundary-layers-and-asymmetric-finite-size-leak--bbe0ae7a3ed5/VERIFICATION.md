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

# Numerical and analytical verification scope

The analytical argument in `RESULT.md` is the basis for the asymptotic theorem. Its critical premises are the stationary Gaussian-mixture representation from Biroli et al. (arXiv:2312.02570) and standard normal Mills inequalities. The mixture normalization and the exact maximum CDF are written explicitly. The two endpoint changes of variables, the conditional hidden-state measures and the separate unshifted-endpoint arguments are supplied in the proof. No finite array of computations can certify an infinite asymptotic statement.

Run `python verify_edge.py` with Python 3, NumPy-compatible SciPy, and the standard library. The code directly evaluates the finite-\(N\) mixture CDF, the limiting fractional-Gumbel integrals and hidden-state conditional means. It also checks both exact mixture normalizations and the two unshifted-endpoint asymptotics for two asymmetric parameter tuples, several arguments and very large formal populations. This package's script was run and returned **PASS: 66 numerical/integral diagnostic assertions**. Absolute floating-point and quadrature precision limit the diagnostic meaning of the checks, particularly because the asymptotic convergence is logarithmic. No source data or code outside this package is required to replay the checks except the documented Python/SciPy dependency.

The scientific and priority limitations are stated in `RESULT.md` and `REVIEW.md`. Independent audit is not performed.
