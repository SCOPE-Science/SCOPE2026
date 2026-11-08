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

Run `python3 verify_signal.py` using only Python 3 standard library. The script was executed directly and again after extraction from the packaged JSONL; it reported 1,499 passed checks. Its tests include exact rational stationary moment balances at 12 chain sites, 16 heterogeneous downstream-noise profiles, independent Runge–Kutta integration of the linear conditional-mean equations, stationary forward/reverse asymmetry, unique-peak sign tests through depth 200, peak-root limits through depth 2,000, and independent numerical quadrature of the integrated covariance formulas. Its printed example for depth ten is reproducible.

The mathematical proof in `RESULT.md` is responsible for the universal stationarity, uniqueness, derivative sign, all-depth asymptotics and exact integration. Finite numerical checks do not prove infinite-depth limits. The formulas concern raw covariance, not normalized Pearson correlation. The package uses no external theorem-proving service and has not received an independent scientific audit.
