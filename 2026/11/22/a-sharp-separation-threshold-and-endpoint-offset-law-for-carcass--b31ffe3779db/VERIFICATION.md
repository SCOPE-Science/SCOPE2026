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

Use Python 3 and run `python3 checker.py` beside this file. It requires no third-party packages. The program recomputes the pre-search carcass stock from the state recurrence and independently by summing cohort survival and subsequent search possibilities. It checks bisection roots and all positive gap constraints across a parameter grid, checks first/last interval difference and equal intermediate intervals, compares finite-difference stationarity, verifies selected objective values, tests convex combinations and alternate feasible calendars, and uses rational numbers for exact arithmetic checks of the two expected-count formulas.

The tested package reports `PASS: 15020 diagnostics; finite checks supplement the analytical proof`. The proof of optimality is analytical and appears in RESULT.md, not in sampling or diagnostic logs. The proof assumes a homogeneous arrival rate, exponentially distributed scavenging time, and independent constant per-visit detection. Inaccessible historical full text and untested field applicability remain outside computational verification.
