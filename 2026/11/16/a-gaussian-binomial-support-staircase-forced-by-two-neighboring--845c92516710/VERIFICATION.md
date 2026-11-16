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

The analytic proof uses exact finite cyclic identities, including the product over a complete set of roots of unity and the nonvanishing of the Gaussian-binomial coefficients for exponents strictly smaller than the root order. It checks the generating-step hypothesis and verifies that the full-period product is nonzero before reducing lengths modulo the order. The constructive example uses a positive two-term trigonometric ratio with exactly unit cyclic product, ensuring the periodic recurrence defining the window is consistent.

Execute `python check_staircase.py` with NumPy. It constructs all divisor-order examples for cyclic lengths from 3 through 26, computes discrete STFTs using direct FFTs and checks exact predicted cardinalities using a declared numerical threshold. The execution reported: `PASS 19058 STFT entries checked; all divisor staircases and support totals matched.` The numerical threshold may suppress very small coefficients in other parameters and does not establish an all-size theorem; the proof supplies that conclusion. The source files and this account do not claim an independent audit.
