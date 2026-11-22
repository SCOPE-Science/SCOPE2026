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

# Reproducibility and mathematical checks

The standalone `verify_watson_frequency.py` checker ran successfully using Python, NumPy, and SciPy and reported `PASS: 56 deterministic checks`. It compares the exact Bernoulli-polynomial pairwise statistic with a high-frequency Fourier approximation in orders one and two, checks the exceptional Fourier moment by quadrature, verifies the exact finite-sample expected-value formula for three orders, and tests the threshold and critical-normalization algebra. The Fourier truncation comparison uses its explicitly stated finite cutoff and numerical tolerances; it is **not** an exhaustive check of the infinite series.

The proof's key analytical certificates are the trigonometric Fourier moments, exact expectation bound for all nonexceptional high modes, the bounded triangular-array multivariate CLT for fixed low modes, the uniform summable Fourier-tail estimate, and the exceptional-mode law of large numbers. These are stated and justified in `RESULT.md`, not inferred from software logs. The total-variation bound is analytical via Hoeffding's inequality.

No independent mathematical audit was performed. Historical-priority risk and scope restrictions are described in `REVIEW.md` and `RESULT.md`.
