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

# Verification and scientific limits

Reproduce the deterministic finite checks with `python CHECK.py`; the code uses the Python standard library and the `mpmath` package and reports the assertion count. The extracted script completed successfully with 734 assertions. Its exact rational torus-integral calculations verify low-order orthogonality and binomial norms independently of the generating-function expression. The high-precision checks compare the derived generating series with the closed formula, inspect the positive-half-plane bound, test the complete-Pick coefficient and examine diagonal metric asymptotics.

The all-degree Hilbert-space decomposition, kernel identity, zero-free inequality, complete-Pick obstruction and sharp boundary exponent are proved symbolically in `RESULT.md`. No finite numerical experiment is used to prove those general assertions. Literature comparison is grounded in cited source text and public mathematical records; it does not constitute an independent publication-priority determination. The complete kernel on off-axis pairs has not been assessed for zero-freeness, nor has a global boundary metric been determined.
