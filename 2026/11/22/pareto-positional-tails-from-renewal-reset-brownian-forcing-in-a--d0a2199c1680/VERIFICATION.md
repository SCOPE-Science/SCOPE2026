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

# Verification and limits

Extract the package and run `python3 verification.py` in the same directory after installing the small numerical dependencies in `requirements.txt`. The checker must report `PASS 57 deterministic consistency checks` (checked with Python 3.11 and SciPy 1.17). It compares the renewal covariance resolvent and independently integrated affine-epoch/age decomposition for four clock families, the Itô innovation variance using direct quadrature, strict periodic-vs-random variance inequalities, and the asymptotic coefficient of the stationary-age Gaussian core under three Pareto exponents. Three additional Pareto cases check the exact finite-variance decomposition.

Finite quadrature verifies formulas and constants only; it does not certify every possible clock or the full infinite-position tail. Those conclusions rest on the mathematical argument in `RESULT.md`: stationary affine contraction, regular variation of renewal age, independent Gaussian product, negligible preceding-epoch term, exact force covariance, and strict Jensen convexity. The asymptotic coefficient is for the **full stationary position**, including previous reset epochs; numeric tail checks test the leading current-cycle component because the older-epoch term is proven negligible analytically.

No independent audit or third-party certification has been performed.
