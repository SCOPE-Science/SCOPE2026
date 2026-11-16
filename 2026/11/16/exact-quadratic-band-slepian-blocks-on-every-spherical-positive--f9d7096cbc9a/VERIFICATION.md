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

# Reproducibility checks

The standalone `checker.py` independently computes full low-pass spherical-harmonic orthant Gram matrices using products of gamma functions for all monomial moments of degree at most four, and compares their eigenvalue multisets with the asserted reduced blocks in ambient dimensions 3 through 9. It reported `PASS: direct absolute-sphere monomial moments vs block spectra, dimensions 3..9: 224 checks` on the delivered source before packaging. Its additional diagnostic dimensions were 10, 20, 50, 100, 300, and 1000; the computed condition-number-to-dimension-squared ratios approached the analytic limit \(2/[\pi(\pi-3)]\). The first computational dimension, 3, is included only as an independent boundary check; the new theorem is stated for dimensions at least 4. Code needs Python 3, NumPy and SciPy.

All-dimensional validity rests on the moment identity, the explicit symmetric-group decomposition, the positive-definite exact moment matrix, and the rigorous asymptotic moment argument in RESULT.md. Floating-point eigenvalue comparisons are supplemental and do not certify the limiting identity. No independent audit was performed.
