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

# Verification and bounds

The accompanying standalone `bunched_cycle_width_checker.py` was executed with Python 3 using only `fractions.Fraction` and the standard library. It returned:

`BUNCHED_CYCLE_WIDTH_EXACT_PASS enumerated_cases=63 phase_checks=9800`

Every nontrivial vertex cut of each of the 63 finite graphs was enumerated (up to complementation). Its exact squared cut-normal width was compared to the theorem, including the *complete* minimizing set, not just the minimum value. The separate phase sweep checked 9800 integer parameter pairs. This finite evidence does not substitute for the analytic all-parameter proof in RESULT.md, and no external or independent mathematical certification has been performed.
