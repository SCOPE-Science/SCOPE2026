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

# Reproducibility and boundaries

Run `python3 check.py` using Python 3.8+ and no external modules. `CHECKS.txt` records the actual program output. The program separately enumerates every zero-one partial injection matrix, computes ranks by modular Gaussian elimination, and derives rank spectra via a multivariate exponential recurrence in exact rational arithmetic. All size \(1\) through \(4\) pair comparisons pass in characteristics two and three. For sizes \(5\) through \(8\), coefficient-total consistency is verified against the independent rook-monoid counting formula; these are not exhaustive matrix enumeration checks. The analytical proof of all dimensions is in `RESULT.md`. The two regimes for odd and even finite fields depend only on their characteristics; exhaustive tests over the two prime fields are consistency tests, not finite-field extension tests.

Independent review and independent validation have not been performed. The historical-priority assessment is qualified by the possibility of an unlocated equivalent specialized enumeration.
