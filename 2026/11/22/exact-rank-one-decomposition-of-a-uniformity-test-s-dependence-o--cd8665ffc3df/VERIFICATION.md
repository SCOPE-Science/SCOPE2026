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

# Verification and scope

The result is proved using exact polynomial kernel contractions and a finite-sample index-partition identity, rather than a numerical extrapolation. Run `python3 check.py` from this directory: it uses only Python 3 standard-library modules and reports `PASS 13510 checks`. Numerical/statistic-form comparisons supplement the all-sample proof. The Pearson correlations are only defined for sample sizes at least two; fitted-null samples are outside the theorem. No independent audit has been performed.
