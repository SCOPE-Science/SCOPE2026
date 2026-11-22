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

# Reproducibility and limits

The standalone Python 3 file `VERIFY.py` uses only the standard library. Execute `python3 VERIFY.py` after extracting the artifact files. It recomputes the saturated rational variance identity using exact fractions at 1999 distinct polymer lengths, enumerates all 24 possible first-clock orderings for length two and all 5040 for length three, and performs 30 independent numerical quadrature comparisons for the time-dependent covariance.

The finite enumerations reconstruct the conditional expected multiplicity from the original interval-acceptance test, checking the pivotal-clock argument independently of its analytic derivation. The printed checks are diagnostic evidence; the proof of sharp finite range, all lengths and all positive observation times is the conditional-independence argument in `RESULT.md`. Full historical priority has not been independently established. Independent audit has not been performed.
