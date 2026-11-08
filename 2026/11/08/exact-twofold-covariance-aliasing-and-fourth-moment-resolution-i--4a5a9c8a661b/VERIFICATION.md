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

# Reproducibility and limits

The theorem is analytic: the full covariance comes from a two-state linear regression and its characteristic polynomial, and the fourth moment comes from the stationary generator. The standalone `checker.py` reproduces symbolic identities for the generator, matrix, and moment inverse; it also computes 30 independent matrix-exponential values at five lags for each of six rational parameter choices and compares both aliases.

Run `python checker.py` with SymPy and mpmath installed. Expected output contains `PASS symbolic moment generator, covariance ODE, duality, exact inverse, and 30 independent matrix-exponential comparisons`. This computation is a diagnostic supplement to the proof, not a certificate of infinite quantifiers or publication priority.

The source-article stationary characteristic function was also independently expanded through order four in its Fourier variable, reproducing the source second and fourth moments exactly. The source-derived forward formulas are credited in RESULT.md. Statistical estimation from finite observations and independent external validation remain unperformed.
