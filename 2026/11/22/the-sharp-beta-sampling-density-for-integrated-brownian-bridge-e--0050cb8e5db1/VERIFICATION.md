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
# Reproducibility and verification

Run \(\texttt{python verify.py}\) with NumPy, SciPy and SymPy available. The included recorded execution verifies:

- Exact symbolic integration of both posterior covariance terms and agreement with the gap formula.
- Exact symbolic summation of the uniform-grid risk and its limiting constant.
- Five independently evaluated Gaussian covariance quadratures, each within \(8\times10^{-6}\) of the exact rational formula.
- Nonnegative risk for 986 exact-rational weakly ordered designs, including some coincident sites.
- Convergence of large Beta-quantile grid risk factors toward \(\operatorname{B}(4/3,4/3)^3/3\).

The Gaussian covariance quadrature uses a finite resolution and is only a numerical check. Exact rational enumerations do not establish the infinite theorem. The mathematical proof of the global lower bound, endpoint-tail control and attaining quantile construction appears in RESULT.md; independent mathematical review has not been performed.
