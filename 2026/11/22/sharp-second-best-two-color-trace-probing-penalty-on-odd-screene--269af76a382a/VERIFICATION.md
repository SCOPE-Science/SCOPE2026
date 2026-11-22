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

# Verification record

The displayed formulas are proved symbolically in `RESULT.md`. The standalone `check.py` uses Python 3 standard-library `fractions.Fraction` and exhaustive binary-word enumeration at the stated **finite** sizes only, checks the exact Gaussian Green recurrence and the exact first variance gap, and needs no external packages.

Run: `python check.py`

Observed output: `PASS: 15 exact parameter cases, 16368 exact spin tests, 135 Green recurrence tests; sharp nonoptimal variance gap.`

This is a computational cross-check, not an infinite-domain certificate. The proof assumes independent symmetric signs restricted to the two classes, positive screening and an odd cycle of at least five vertices. Historical publication priority and independent proof validation are not established by these checks.
