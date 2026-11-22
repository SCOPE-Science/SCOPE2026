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

# Reproducible verification

Run `python verification/escape_clock_check.py` with Python 3.9 or newer. The script uses only standard-library `fractions` and `random` and requires no files beyond its own source. It checks 400 generic exact-rational one-step/two-step lower inequalities, plus 72 rational checks of the invariant-cone and exact two-step recurrences, all of which passed when the result package was assembled.

The proof establishes claims for all real parameters and all forward times, which cannot be verified by these finite experiments alone. The key exact symbolic statements are \(y_{n+1}+r y_n=cx_n\), \(y_{n+2}=(r^2+bc x_n)y_n\) when \(a=r\) and \(y_n\ge0\), and the resulting positive quadratic recurrence for the two boundary rays. The standard forced-Fibonacci recurrence comparison establishes the interior limit; no computer enumeration is asserted to certify infinite-time completeness.

No independent audit has been performed.
