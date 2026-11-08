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
# Reproducibility and verification

The algebraic derivation in RESULT.md establishes the theorem for all positive real parameters. Run `python CHECK.py` using Python 3 with `sympy` and `mpmath`; no outside files or external connections are required. The executable check passed with `EQUAL_WIDTH_THREE_INTERVAL_JET_CHECKS_PASSED 164`.

The symbolic checks cover exact power-sum relations and the Taylor-derivative coefficients through degree six. The numerical tests include 27 interior parameter triples, a symmetric-spacing boundary, cubic-root inversion, and four small symmetry-breaking perturbations, using 65 digits of working precision. They check sample formulas and do not constitute exhaustive or independent validation. For the self-review and remaining originality risk, see REVIEW.md and AUDIT.json.
