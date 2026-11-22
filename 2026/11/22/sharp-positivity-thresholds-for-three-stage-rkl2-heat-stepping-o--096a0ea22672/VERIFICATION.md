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

The proof in `RESULT.md` is analytic, using the four spectral entry types, factored cubic signs, and strict monotonicity of the scalar RKL2 stability polynomial. The self-contained standard-library Python program `verify.py` tests the polynomial and projector-entry formulas by exact rational matrix operations, checks exact threshold signs on finite graph ranges, and brackets the star thresholds by rational bisection.

Run `python3 verify.py` in the directory containing this file and `RESULT.md`. Expected program output: `VERIFY_OK 52755`.

Finite computation does not prove statements quantified over all graph sizes. No floating-point numerical simulations are used as proof, and no independent mathematical audit has been performed.
