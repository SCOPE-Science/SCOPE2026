---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification record

Run `python3 verify.py` with the standard library. The diagnostic computes finite binomial-log singular weights and brackets the omitted infinite tail by Jensen's inequality, a logarithm Taylor bound, and a trapezoidal error estimate (ordinary floating-point rounding is not certified). It compares the resulting finite normalized corrections with the claimed operator-norm and Schatten coefficients, including one quasi-Schatten choice. The infinite asymptotics and all parameter quantifiers are justified by the analytical proof in `RESULT.md`.
