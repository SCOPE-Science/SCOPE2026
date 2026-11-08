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

The standalone `verify.py` uses exact rational-pair arithmetic for the quadratic field \(\mathbb Q(\sqrt2)\). Across orders 2 through 100 and five parameter values, it checks all formula normalization identities, row signs, the full eigenvector equation and the rowwise Rayleigh saturation statements; execution reported `VERIFY_OK 495`. An auxiliary independent SymPy/NumPy calculation checked eigenvalue minima against the analytic formula for orders and representative parameters, reporting 71 checks. These finite checks supplement an all-order proof in `RESULT.md`.

For the all-order result, verify first that the positive tent profile makes each normalized row projection exactly one, except the even central comparison, then that the formula solves the Jacobi eigenvector equations and normalization. The ground-state sum-of-squares identity implies the proposed eigenvalue is the least eigenvalue; the Rayleigh equality equations then force the unique even or entire odd optimizer face. Direct summation of the tent profile verifies the rate limit. The statement is limited to fixed iid row probabilities and the one-step worst-direction mean-squared contraction. No independent mathematical audit has been performed.
