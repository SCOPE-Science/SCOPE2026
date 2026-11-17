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

# Verification notes

The result is based on an analytic proof using the exact inverse of a tridiagonal cardinal-spline recurrence, a piecewise-cubic step response, an exact geometric variation sum, and an \(\ell^1\) jump decomposition. The standalone `verify.py` directly tests symbolic identities and the algebraic characterization of the gain, then independently integrates derivatives of natural cubic interpolants using their exact critical points on large finite domains. Randomly generated finite-variation data test the inequality. No finite experiment is used as an infinite proof.

Run `python verify.py` with Python 3, `sympy`, `numpy`, and `scipy`. Success requires `ALL_CARDINAL_CUBIC_VARIATION_CHECKS_PASS`. The diagnostic finite-domain boundary convention does not extend the stated bi-infinite theorem to finite domains.

Independent validation has not been performed.
