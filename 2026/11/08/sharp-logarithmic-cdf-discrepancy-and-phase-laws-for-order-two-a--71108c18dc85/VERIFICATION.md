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

Finite exact checks: run `python3 verify_almost_golomb.py` with Python standard library. The verifier checks the recurrence at 16,382 applicable indices against the explicit formula, 308 phase CDF samples, 4,950 additional exact thresholds, and 4,997 initial cutoffs for the exceptional endpoint count. Fraction arithmetic is used throughout for ratios and cumulative distributions. The full infinite result requires the analytic block count and endpoint argument in RESULT.md; the program alone cannot establish an infinite proof. The bound's constant 30 is not claimed sharp. Independent audit is not performed.
