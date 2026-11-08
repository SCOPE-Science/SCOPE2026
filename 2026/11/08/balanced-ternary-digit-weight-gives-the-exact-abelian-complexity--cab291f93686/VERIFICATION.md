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

# Verification notes

The mathematical argument uses exact triple-block decompositions, recurrence of all finite factors, and unique balanced ternary expansions. The included executable `verify.py` independently tests finite instances against direct word generation, with no use of the analytic maximum/minimum recurrence in the window-count check.

Actual execution:

```text
VERIFY_OK directives=34 phase_cases=1794 digit_cases=100000 window_cases=8960 peaks=11
```

Run with `python3 verify.py` and NumPy installed. The phase check enumerates all six patterns, all three starting residues and lengths \(1\) through \(299\); the word check uses \(34\) directive samples (six constant, four structured, 24 seeded pseudorandom), all lengths through \(256\) in \(3^9\)-letter prefixes. Both fills of the persistent-hole example are tested. The digit check covers the stated recurrences, parity and Lipschitz step for all positive integers through \(100000\); eleven peak instances are checked.

The finite tests establish **only** those finite instances. They do not certify infinitely many lengths or arbitrary directives. The symbolic proof provides those steps and must be assessed on its own. No independent audit or external certification has been performed.
