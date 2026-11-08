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

The attached `verify.py` uses only Python's standard library. It verifies the exact stationary branch, the Routh polynomial identities and factorization, and the sharp witness across rational coupling/detuning examples. For each set of exact parameters it also compares the four calculated spectral roots at damping values on both sides of the critical point. These are finite reproducibility checks, not a proof for all network sizes or all parameter values.

The argument establishing the general theorem is the exact Jacobian reduction followed by the real-symmetric spectral similarity for positive-semidefinite interaction matrices. The constructive two-mode converse is proved by exact quartic algebra, Routh–Hurwitz inequalities and a derivative calculation. No simulations of nonlinear cycles and no quantum claims are included.

To reproduce: `python3 verify.py`.
