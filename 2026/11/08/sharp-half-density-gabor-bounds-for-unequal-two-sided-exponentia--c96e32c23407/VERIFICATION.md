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

The analytic proof in `RESULT.md` derives the unit-spaced Zak multiplier directly from geometric series and optimizes it over both fiber variables. The complete claim holds for all strictly positive decay rates and translation spacings, independently of the numerical checker.

The included `check_asym_gabor.py` uses standard-library arithmetic, tests the exact rational-symbol and extremal formulas on 28 parameter pairs and 12,320 randomly selected Zak fibers, and compares rational Zak sums against truncated bilateral series in 27 additional tests. On execution the checker prints `ASYMMETRIC_EXPONENTIAL_GABOR_CHECKS_PASS 12431`. Finite checks do not prove assertions for all rates, and independently audited proof verification has not been performed.
