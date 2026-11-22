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

# Reproducibility and proof boundaries

The exact result follows from standard Gaussian orthant integration, the explicit split integral for the information score, and strict concavity of that score on the full admissible time interval. The included standalone `check.py` uses 40-digit arithmetic and the pinned `mpmath` dependency to test independently evaluated integrals, the stationarity equation, selected time ranges, and finite-noise limits. Execute `python check.py` from the extracted package. The tested execution printed `PASS` for 32 direct numerical integrations, 2,400 random off-optimum risk comparisons, the exact endpoint constants, and a largest integral discrepancy below \(6.5\times10^{-40}\).

These are finite computational checks and do not certify every real parameter or independently prove theorem originality. The exact global argument uses the displayed analytic first and second derivative formulas for all \(0<a\leq1\), not a finite search. The infinite-noise model is only a limit and has no unique optimal observation time at the limit itself. No independent audit or externally validated proof is claimed.
