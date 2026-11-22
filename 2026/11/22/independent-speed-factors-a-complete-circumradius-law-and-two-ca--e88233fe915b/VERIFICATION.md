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

# Verification and reproducibility

The exact mathematical argument, including normalization and critical Hessian signs, is in `RESULT.md`. Re-run the self-contained numerical diagnostic with `python3 verify_circumradius.py` (Python 3.10 or later, no third-party modules). Its recorded output was `ALL_CHECKS_PASSED 1845`.

The checker constructs triangle circumradii directly from Euclidean side lengths and signed cross-product areas, independently evaluates the pairwise-half-sum product formula, and uses Simpson integration to compare ordinary moments, logarithmic moments, and the dilogarithm series. It also verifies all four critical-point Hessian coefficients and the log-moment inversion for four noncircular ellipses; a seeded random sample corroborates ordinary moments. The coefficient of the square-root cusp and its side are deduced analytically in `RESULT.md` using the Morse/coarea computation, not estimated solely from finite samples.

The verified scope is a fixed, noncircular ellipse with three independent uniform eccentric anomalies. No finite-data confidence bounds or claims of historical uniqueness are supplied. Numerical agreement is not an independent audit or a substitute for the infinite proof.
