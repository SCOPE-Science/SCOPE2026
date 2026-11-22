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

# Verification and reproducibility

Run `python artifacts/verify_two_step.py` with Python 3 and SymPy in the same directory as `RESULT.md`. Its recorded output is provided in `artifacts/verification.txt`.

The checker independently expands the initial quadratic objective ratio, computes the exact two-update expression with a symbolic second stepsize, verifies the positive-coefficient denominator-margin certificate, and evaluates the explicit witness using rational arithmetic. It also tests 5,000 seeded pairs of positive condition numbers and spectral weights by comparing the objective after direct gradient updates with the formula, and reports a high-conditioning sequence.

The proof of the universal inequality and sharp asymptotic coefficient is contained in `RESULT.md`: finite numerical tests alone cannot establish either result. The sample sequence is evidence for reproducibility, not a substitute for the asymptotic argument. The relationship to previous results is a qualified literature assessment, not a certificate of comprehensive priority or independent audit.
