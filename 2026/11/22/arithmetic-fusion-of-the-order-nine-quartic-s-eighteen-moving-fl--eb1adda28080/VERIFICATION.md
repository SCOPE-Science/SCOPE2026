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

Execute `python verify_flex_arithmetic.py` with Python 3 and SymPy 1.14.0. The verifier computes the ternary Hessian determinant from second derivatives, reconstructs the affine lex Gröbner basis, checks separability of the residual degree-eighteen polynomial, and verifies all three modular Frobenius-power congruences and both gcd conditions over \(\mathbb F_7\). It also checks the displayed three rational flex candidates and the origin's tangent contact order. The output is `ORDER_NINE_QUARTIC_ARITHMETIC_FLEX_DIVISOR_OK` on success.

The all-characteristic statements are restricted to characteristic zero and to the indicated good characteristic seven. The geometric assertion about the two nine-point automorphism orbits relies on the explicit order-nine automorphism and nonzero roots; arithmetic transitivity follows from the proved irreducibility. The verifier is not a replacement for the local multiplicity reasoning or the standard irreducibility criterion in the proof. Historical priority and independent mathematical audit remain unresolved.
