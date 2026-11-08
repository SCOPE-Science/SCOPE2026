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

`verify.py` is a standalone Python 3 verifier requiring only the standard library. Execute `python verify.py` in the directory containing this file. It checks exact cyclotomic determinants for all 3-by-3 minors of the order-8 and order-16 Fourier transforms, modular rank-one conditions, and exact count identities for exponents 2 through 13. It prints `DYADIC_THIRD_ORDER_FOURIER_MINOR_CHECKS_OK` on success.

The infinite claims are established by the unimodular-determinant lemma, dyadic signature classification, and finite geometric-series identities in RESULT.md. These are proof arguments, not inferred from finite tests. The checker does not evaluate floating-point Fourier matrices and does not independently establish originality or mathematical value. Independent audit and validation have not been performed.
