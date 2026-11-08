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
# Verification instructions and limits

The quantitative claim is a closed-form theorem for noiseless quadratic functions, not an empirical statistical claim. The self-contained proof in `RESULT.md` uses only fourth-order sphere moments and conditional uniformity of an orthogonal Haar-frame pair. The nonstandard calculation is the exact Frobenius pair covariance; its derivation and normalization are explicit.

Run `python verification/check.py` from the extracted package root (Python 3 with NumPy and SymPy installed). Its exact symbolic assertions verify the risk difference algebra, the dimension-two and dimension-three transition ratios and the sharp risk-inflation constants. Direct deterministic circle quadrature and seeded higher-dimensional Monte Carlo provide separate diagnostic checks. The recorded standard output is in `verification/output.txt`.

Finite deterministic assertions or stochastic simulations do not independently prove the theorem for all dimensions or all symmetric Hessians. They supplement the analytic derivation. No independent audit, specialist referee review, or external formal certification is asserted. The source comparisons are bounded by inspected literature and might miss an older equivalent statement.
