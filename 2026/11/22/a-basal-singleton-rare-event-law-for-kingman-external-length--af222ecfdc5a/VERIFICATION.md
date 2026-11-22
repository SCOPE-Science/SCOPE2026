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

The independent audit has not been performed. A standalone exact checker `check.py` enumerates all ordered pair-merger histories through seven original leaves, totaling 3, 18, 180, 2,700 and 56,700 histories for \(n=3,4,5,6,7\) respectively. It computes expected waiting-time contributions using exact rational arithmetic, and checks all finite probability, mean, conditional mean and covariance identities. Additional exact arithmetic verifies the conditional-stage sum and positivity for sizes through 500. The infinite rare-event limit follows from the analytic coupling and established ordinary Kingman external-length variance, not from finite enumeration.

To replay, place `check.py` in the working directory and invoke `python check.py` under Python 3. No third-party package is needed. The external mathematical literature remains subject to independent historical-priority assessment, especially the full Disanto–Wiehe 2020 paper.
