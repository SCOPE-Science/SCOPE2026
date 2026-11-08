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

The standard-library checker `verify.py` directly constructs all \(m\)-coordinate vertices for \(2\le m\le6\) at \(m\le n\le m+6\), calculates every covariance entry as an exact rational, and compares it with both closed-form covariance eigenspaces and the quadratic phase polynomial. It checks 35 parameter values, 16,583 vertex vectors, and exact sign change for 199 further orders through \(m=200\). It passed with the message `PARTIAL_PERMUTOHEDRON_VERTEX_COVARIANCE_CHECKS_PASSED`.

The proof for all \(m,n\) is an exact orbit-averaging and polynomial-sign argument, not an extrapolation from finite checks. Historical priority and additional geometric measures are outside the verification scope.
