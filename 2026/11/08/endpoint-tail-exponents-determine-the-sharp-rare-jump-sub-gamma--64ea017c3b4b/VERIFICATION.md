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

This result is supported by a self-contained analytic argument and a separate diagnostic checker. The defining variance is \(\sigma^2+\lambda\mathbb E J^2\); the small mixing parameter is \(\delta=\lambda\mathbb E J^2/(\sigma^2+\lambda\mathbb E J^2)\). The exact normalized remainder MGF is \(1+\delta(F(s)-1)\), with \(F\) given explicitly in `RESULT.md`. The critical steps are endpoint-tail Laplace asymptotics, logarithmic derivative control, global-maximizer localization and the stationary-equation comparison. Their proofs are in `RESULT.md`.

To replay finite checks: run `python check.py` from the extracted package directory. The checker uses Python standard-library arithmetic only. Observed output during preparation: `PASS: 262 exact-rational and numeric diagnostic assertions`. It checks Taylor coefficients for the uniform and triangular jump laws and finite stationarity/asymptotic samples for \(L\in\{25,50,100,200\}\).

These samples do not establish the theorem for arbitrary exponents, all small intensities or infinitely many test points. The rigorous proof does. Independent audit was not performed.
