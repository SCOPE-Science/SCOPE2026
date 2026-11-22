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

The attached standalone Python 3 checker `verify_theta_covariance.py` enumerates all edge-sign assignments for each of the eight tuples \((2,2,2)\), \((2,2,3)\), \((2,3,4)\), \((3,3,3)\), \((2,2,2,2)\), \((2,2,2,3)\), \((2,2,2,2,2)\), and \((2,2,2,2,2,2)\). It rejects precisely those containing oppositely coherent entire paths and sums exact integer outer products of the corresponding doubled Euclidean vertices. It then separately computes the claimed symbolic integer-matrix expression and compares every matrix entry exactly. This verifies vertex counts, all second moments and normalization for those tests without floating-point arithmetic or external packages.

Command: `python3 verify_theta_covariance.py`

Observed terminal line: `THETA_MULTIARM_COVARIANCE_EXACT_PASS`.

The finite checks do not prove the claim beyond their tested tuples. The analytic proof of the general result is the inclusion–exclusion calculation of the complete allowed sign space, exact within- and between-path correlations, and telescoping of incidence columns; no computational assumption is needed for its universal quantifiers. No independent audit has been performed.
