---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational verification and proof boundary

The accompanying `verify_tail.py` (Python 3; NumPy, SciPy, SymPy required) was executed from the package before delivery. Its SymPy calculation verifies the phase Hessian \(\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\), determinant \(3\), and inverse covariance \(\frac13\left(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\right)\). For two positive-parameter choices it approximates the single-clock Bessel integral after analytical gamma-diffusivity integration, using finite quadrature over the rescaled clock interval \([0.04,4]\). It compares its exponential-rescaled estimate with the claimed asymptotic equivalent at \(q=20,40,80\). The sampled ratios decrease toward one, with terminal values approximately \(1.04870\) and \(1.01014\). It also checks selected variance inequalities \(0<V(s)<as\).

These checks are finite numerical and symbolic evidence only. The infinite-distance density equivalent, the conditional normal limit and their global parameter scope follow from the analytical derivation in `RESULT.md`, including the explicit noncompact-tail localization argument. No external or independent audit has been performed. No claim of numerical exhaustiveness or certified error bounds is made.
