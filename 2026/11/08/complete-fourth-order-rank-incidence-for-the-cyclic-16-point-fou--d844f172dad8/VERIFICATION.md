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

The proof is a finite exact enumeration with symmetry reduction. The accompanying `f16_exact_check.py` is standalone Python 3 using only the standard library.

Run `python3 f16_exact_check.py`. The program confirms all 25 affine row-orbit sizes, every orbit-specific rank count for the 1820 column sets, and the global totals. It computes each of the 45,500 representative submatrix ranks twice: once from exact integer coefficients in the basis of the cyclotomic field, and once using ranks at the eight primitive sixteenth roots modulo 97. Its key assertion is `EXACT_F16_FOURTH_MINOR_TWO_METHODS_PASS`.

The two calculations are mathematically equivalent to the complex claim for minors of size at most four: after reduction by \(T^8+1\), each determinant has degree less than eight and coefficients of magnitude at most 24, strictly smaller than 97. Thus eight-root modular vanishing is precisely integer polynomial vanishing. This is an exhaustive check after a rigorously justified affine reduction, not a probabilistic sample.

The verification establishes exactly the 16-point, fourth-order rank census. It does not establish a general formula in other dimensions, historical novelty, or an independent mathematical audit.
