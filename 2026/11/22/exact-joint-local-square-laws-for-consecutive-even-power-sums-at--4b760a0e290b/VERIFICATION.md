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

# Reproducible finite checks

Run `python3 verify.py` with Python 3. It uses integer arithmetic and the standard library only. Checks include 23 complete prime-power periods, 84,031 direct index evaluations, full four-class histograms and output marginals, four direct branch-bijection tests, and covariance signs for thirteen odd primes. The script prints each test result or raises an exception on a discrepancy.

The symbolic proof in RESULT.md is the evidence for the unbounded statement. Finite enumeration is not exhaustive over all primes, powers or index cutoffs. Self-review was completed; independent external audit was not performed.
