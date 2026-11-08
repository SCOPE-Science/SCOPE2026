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

The finite-field checker `verify.py` is standalone except for standard Python and SymPy. It evaluates the displayed characteristic-two smooth cubic over three exact binary extension fields. It constructs its gradient and Hessian by formal derivatives, builds bases of affine tangent spaces, and computes the rank of the differential modulo the gradient. The expected counts and `ALL_CHECKS_PASSED` output are stored in `CHECKS.txt`. It also checks a symbolic local-chart \(2\times2\) minor equal to \(u^4/t^3\), on the chart where \(t\ne0\), for that sample cubic.

The checker covers finitely many rational points and one exact local chart identity; these alone do not prove the universal fourth-order theorem. The complete all-fields proof is the symbolic algebra and local divisor argument in `RESULT.md`. Historical priority is not independently established. No external verification has been performed.
