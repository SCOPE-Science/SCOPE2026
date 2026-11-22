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

The proof in RESULT.md uses exact differentiation, three finite gcd computations, a weighted local regular sequence, Bézout's theorem and generic smoothness of affine sections. A self-contained Python/SymPy checker is included as `verify.py`, with exact integer symbolic computations for exponents \(3\) through \(8\) and all four tested prolongation orders. All tests completed successfully. Its finite sample is consistency evidence, not a substitute for the displayed proof for every exponent.

The source comparison distinguishes the existing conjecture and numerical experiments from a universal proof of the stated initial-order case. Priority outside accessible literature is unresolved. Independent audit is not performed.
