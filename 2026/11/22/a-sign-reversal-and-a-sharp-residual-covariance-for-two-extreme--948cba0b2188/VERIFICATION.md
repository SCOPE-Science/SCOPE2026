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

# Reproduction and scope

Run `python3 check.py` with a standard Python 3 interpreter. The checker compares the transfer-matrix formula against direct enumeration of small cyclic binary words, checks \(-1/81\) using exact fractions, integrates the finite joint CDF at several sample sizes, and checks the approach to the analytic \(\sqrt\pi\) coefficient.

The proof of the infinite asymptotic statement requires the change-of-variables expansion and tail bounds in RESULT.md. Numerical quadrature is not an infinite-sample certificate. The location and uniqueness of any finite covariance sign transition remain unproved. Independent validation has not been performed.
