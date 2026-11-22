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

# Reproduction and boundaries

The exact analytic reduction, convexity, inverse formulas, and fold expansion are in `RESULT.md`. The included `check.py` is a standalone Python 3 standard-library script. In a directory containing `check.py`, run `python3 check.py`; its expected completion statement starts `passed: 5000 random parameter regimes`. The script uses a fixed pseudorandom seed for reproducibility. It does not require network or external dependencies. On the checked execution it completed with 5,000 model classifications, 212 two-reversal inverse checks, the exact example, and five fold-limit comparisons. These tests cannot demonstrate infinite-parameter correctness or uniqueness of historical priority. Independent audit has not been performed.
