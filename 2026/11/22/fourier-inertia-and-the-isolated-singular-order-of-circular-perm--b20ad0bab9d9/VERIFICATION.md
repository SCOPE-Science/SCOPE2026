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
`cyclic_verify.py` uses only the Python standard library. Running `python3 cyclic_verify.py` passed 21,975 exact assertions. It directly enumerates all permutations at each order from two through nine, computes full Walsh transforms using an independent butterfly, and compares each coefficient with the analytic formula. It checks all weight coefficients and signs through order 200 by exact factorial sums, and separately checks the rational recurrence for the exceptional full-support character. Finite tests are evidence of implementation agreement, not proofs for all dimensions; the all-dimensional proof appears in `RESULT.md`. No independent audit has been performed.
