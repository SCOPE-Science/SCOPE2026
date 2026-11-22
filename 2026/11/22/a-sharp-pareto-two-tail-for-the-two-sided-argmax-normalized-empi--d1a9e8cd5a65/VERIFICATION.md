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

The analytical argument uses the uniform order-statistic joint density, exact disjoint interval volumes at two endpoint corners, and a binomial bound for the configurations containing two endpoint-near observations. Its sharp tail is established as the threshold tends to infinity at fixed sample size.

Run `python3 checker.py` from the same directory. The standalone test of exact formulas, discrete corner geometry and independent full-statistic simulation passed 96 assertions at packaging. Simulation corroborates but cannot replace the analytic proof. All second-moment and quantile statements concern the specified two-sided statistic; no full CDF, finite-threshold error constant or independent validation is asserted.
