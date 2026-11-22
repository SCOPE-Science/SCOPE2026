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

# Computational verification and proof boundary

The accompanying `verify_tail.py` (Python 3; NumPy, SciPy, SymPy required) was executed from the package before delivery. Its SymPy calculation verifies the phase Hessian \(\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\), determinant \(3\), and inverse covariance \(\frac13\left(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\right)\). For two independent positive-parameter choices it computes the exact single-clock Bessel-integral density after analytical gamma-diffusivity integration, and compares its exponential-rescaled value with the claimed full asymptotic equivalent at \(q=20,40,80\). Ratios fall monotonically toward one; the high-range terminal ratios are approximately \(1.04870\) and \(1.01014\). It also checks selected variance inequalities \(0<V(s)<as\).

These checks are finite numerical and symbolic evidence only. The infinite-distance density equivalent, the conditional normal limit and their global parameter scope follow from the analytical derivation in `RESULT.md`, including the explicit noncompact-tail localization argument. No external or independent audit has been performed. No claim of numerical exhaustiveness or certified error bounds is made.
