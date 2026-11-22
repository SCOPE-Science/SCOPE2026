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

The standalone `checker.py` validates the probability-generating-function normalization and numerator-root boundary with exact symbolic algebra. It derives logarithmic coefficients independently from probability masses using a formal recurrence, including a negative degree-two coefficient at \(\theta=1\), \(\pi=-1/3\), and a positive sequence at the exact critical parameter. It also checks a below-boundary parameter with several strictly positive initial coefficients.

All-degree sign assertions are established in the accompanying analytic proof by numerator-root magnitude comparisons. The checker supplies supporting finite calculations and does not certify the infinite claim by enumeration. The earliest source date is the first arXiv submission date, not a later journal or revision date. Independent audit has not been performed.
