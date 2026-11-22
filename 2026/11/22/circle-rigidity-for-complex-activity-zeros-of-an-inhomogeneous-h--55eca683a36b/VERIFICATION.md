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

# Reproducibility and mathematical limits

`verify_circle.py` is self-contained, using only the Python standard library. Run `python3 verify_circle.py` next to the result. It returned `VERIFIED 9965 exact transfer/coefficient, root-modulus, and rigidity-witness cases`.

The script independently builds the independent-set partition polynomial by enumerating all occupation masks for small even cycles and compares its coefficients exactly with the matrix-transfer trace. It checks the extreme coefficients, tests algebraic factor-root residuals and radii, and checks the strict coefficient inequality over thousands of background vectors. Floating-point residual tests are illustrative only. The all-size theorem rests on the explicit coefficient/AM–GM argument and exact characteristic polynomial factorizations in `RESULT.md`, not on finite sampling or external certification.

Self-review passed; no independent audit or independent validation has been performed. The cited literature establishes context, not historical-uniqueness certification.
