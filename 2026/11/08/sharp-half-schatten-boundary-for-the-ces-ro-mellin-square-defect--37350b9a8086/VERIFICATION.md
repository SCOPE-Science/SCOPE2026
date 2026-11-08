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

# Finite verification and analytic limits

Run `python3 check_mellin_square.py` in the same directory. A successful local execution printed `MELLIN_SQUARE_DEFECT_FINITE_OK 456187` (456,187 exact finite identities/inequalities and auxiliary numerical consistency assertions). The checker reconstructs finite Cesàro matrices, tests harmonic and factorized formulas, checks the finite inverse identity and evaluates representative matrix singular values. The checker does not certify asymptotic singular-value bounds or infinite Schatten membership; those follow from the proof in RESULT.md. No independent external audit or validation has been performed.
