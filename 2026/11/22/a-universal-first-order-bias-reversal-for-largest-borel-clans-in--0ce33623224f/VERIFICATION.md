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

# Reproducibility

Run `python3 check_borel_max.py` using Python 3 and its standard library. The script computes exact Borel-clan no-exceedance probabilities for four thresholds and three values of sample size, compares with the analytic first correction, and verifies its sign switch and numerical root. All implemented comparisons passed on the supplied script.

The infinite-domain assertion rests on the proof's factorial asymptotic with an integrably uniform remainder and the exact Poisson maximum identity. Numerical finite-\(n\) tests do not independently certify the asymptotic or novelty. Exact finite-\(n\) one-crossing, a second coefficient at the special threshold, and independent verification are not claimed.
