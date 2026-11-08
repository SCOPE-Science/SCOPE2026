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

The companion `verify_rank_greenwood.py` uses only Python's standard library. It checks each exact covariance against direct factorial-based uniform-simplex monomial integration, not by substituting into the result's harmonic simplification; it also checks finite covariance sign order, variances, and asymptotic examples. Execute `python3 verify_rank_greenwood.py`. These are finite validation checks; the infinite sign and limit laws rest on the analytic proof in RESULT.md. No independent external audit was performed.
