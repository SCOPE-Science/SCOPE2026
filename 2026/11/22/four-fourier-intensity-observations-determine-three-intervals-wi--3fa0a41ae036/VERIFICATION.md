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
# Verification and reproducibility

With Python 3.10+ and SymPy installed, run `python checker.py`. The checker verifies exactly that the second coefficient of the complementary-spacing expression is the claimed quadratic and, after eliminating the competing reflection parameter, its fourth coefficient factors into the positive-product obstruction. It then performs 1,500 independent numerical comparisons between interval-by-interval integration and the subtracted-hole formula, with deterministic parameters.

The formal proof, including the two spacing possibilities and strict positivity of the four excluded factors, is in `RESULT.md`. A finite sample is not evidence for an infinite-domain theorem; the symbolic calculations check algebra rather than analytic assumptions, which are reconstructed in the proof. The actual final claim is limited to exact noiseless observations, known span, positive interval and gap lengths, equal gaps, and uniqueness only within that family.

Self-review passed; independent mathematical audit and validation not performed.
