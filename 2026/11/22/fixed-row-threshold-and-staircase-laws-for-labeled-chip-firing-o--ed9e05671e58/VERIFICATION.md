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

Run `python verify.py` using Python 3.10 or later and its standard library. The executable constructs two independent representations of the finite counts: a direct sorted-label firing simulation and an exact integer floor recurrence. It also computes the continuous binomial-polynomial solution using exact rational arithmetic.

The checker tests 7,497 bounded recurrence triples, 164 actual chip-arrival targets over depth at most eight, 24 large-width threshold cases, and 60 nonintegral staircase tests. It asserts the exact nested-floor identity and an all-parameter rounding-error upper bound for the sampled triples. A successful replay finishes with `VERIFY_OK`.

The infinite fixed-row asymptotic is proved by the localized rounding-loss estimate in RESULT.md; its validity is not inferred from finite tests. Integer limiting staircase levels and growing first coordinate are excluded. Independent audit has not been performed.
