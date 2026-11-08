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

The analytical proof uses the factorization of the Gaussian quadratic-form moment generating function into a cubic polynomial, the exact radial moments of a standard three-dimensional Gaussian, and the discriminant of a real traceless cubic. In particular the sixth-moment values are exact fractions, not numerical estimates.

Run `python3 artifacts/verify_even_spherical.py` with Python 3 standard library. Its direct evaluation of 640 rational-sphere moments is independent of the cubic generating-function expansion in the proof. The program also checks representative spectral discriminants and the endpoint equality patterns. Finite tests are evidence of consistency, not a proof of statements quantified over all matrices and all even orders.

The only review completed is self-review. Independent audit has not been performed.
