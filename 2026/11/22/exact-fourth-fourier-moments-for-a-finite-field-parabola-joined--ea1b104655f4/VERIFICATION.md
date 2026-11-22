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

# Reproduction and verification

Run `python3 checker.py` with standard Python 3; no external dependencies are required. It builds finite fields of odd prime order and degree-two extensions using polynomial bases, enumerates ordered two-sums directly from supports, and computes the exact integer additive energy by summing squared representation multiplicities. It then compares with the closed-form polynomial for the corresponding line type.

Observed test outcome: 236 configurations passed (12 over F3, 30 over F5, 56 over F7, 90 over F9 and eight configurations each over F11, F13, F17, F19, F25 and F49). The checks include vertical, exterior, tangent and secant lines and both quadratic-character signs for -1. The proof in RESULT.md is algebraic and valid for all odd prime powers; no claim of exhaustive verification over infinitely many fields is made.

The standard normalization is \(\widehat{f}(\xi)=q^{-1}\sum_{x\in\mathbb F_q^2}f(x)\psi(-\xi\cdot x)\). The resulting exact identity is \(\sum_\xi|\widehat{\mathbf1_S}(\xi)|^4=q^{-2}E(S)\).

Only a self-review has been performed. Independent mathematical validation remains unperformed.
