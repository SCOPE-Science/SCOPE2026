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
# Verification

Run `python3 check.py` with a standard Python 3 interpreter. The exact checker enumerates every cut configuration through ten cards for three rational homogeneous rates and through eight cards for one inhomogeneous rate family. It checks 43 test suites, including the rational moment identities for the limiting matrix and strict negative covariance in every enumerated case. These are finite algebraic checks. The all-size sign follows from product-measure monotonicity, and the Gaussian theorem follows from a renewal-reward limit argument and an explicit terminal-packet bound; no finite computation alone proves either infinite claim. Independent review has not been conducted.
