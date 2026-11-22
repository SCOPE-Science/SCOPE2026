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

`verify.py` requires Python 3 and SymPy. Running `python verify.py` from the package directory checks five independent symbolic algebra identities, including the two-coordinate derivative factorization, stationary derivative and exact optimal-risk identity. It also tests 765 rational ordered pairs across five positive rational noise variances against the analytic optimum at 60 decimal digits. `checks.txt` contains actual replayed output.

The analytic argument, not the finite grid or floating-point tests, covers all real positive noise levels and all point pairs. Independent expert verification and full historical priority review have not been performed.
