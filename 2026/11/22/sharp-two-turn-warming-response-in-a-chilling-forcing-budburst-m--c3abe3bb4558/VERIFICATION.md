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

# Reproducibility and limits

The analytical proof is in RESULT.md. `checker.py` uses Python's standard library and can be run with `python3 checker.py` from the extracted directory. In this package it completed 11,288 supplementary assertions without exceptions. The checks cover algebraic tangency relations, subcritical and supercritical root counts, sign patterns, finite-difference differentiation, fold coefficients, and the stated numerical example.

For independent inspection, first verify the derivative of the date formula on either side of the zero-chill boundary. Next verify strict monotonicity of \(x^2(1-s/2)\), followed by elimination in the two tangency equations and the nondegenerate Taylor expansion. Numerical bracketing and finite sampling are not substitutes for these arguments. The source comparison is provisional: the full original 1983 study was not retrieved. No independently audited mathematical or field validation is asserted.
