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

Execute the standalone script with `python verify_gyrator.py` after installing SymPy. Its recorded execution produced `PASS: 219 symbolic and rational checks`. It verifies the exact stationary Lyapunov covariance, Isserlis/Wick fourth-moment simplification, one-time SNR formula, derivative sign polynomial, analytic maximizer, strict-parameter rational specializations, and numerical inequality examples.

The decisive mathematical steps are the Hurwitz stability argument, the explicit analytic covariance, the Gaussian fourth-moment identity, and the derivative factorization. Finite tests are not a substitute for the proof of positivity and global uniqueness. No formal external certification, experiment, or independent validation was performed. The literature priority limitation concerning the full inaccessible ellipsoid manuscript remains distinct from algebraic validity.
