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

# Reproducibility

Run `python3 verify_cyclic_cumulant.py` using the standard Python 3 library from the package directory. Expected output: `CYCLIC_THIRD_CUMULANT_EXACT_OK 64 checks`.

The script independently enumerates all independent subsets for four cycle orders and evaluates exact-rational first, second, and third occupation moments. It checks the all-size transfer and factorization formulas and separately evaluates the special-fugacity signs for a further range of lengths. The program is finite supporting evidence. All-size claims follow from the algebraic proof in `RESULT.md` and do not depend on the program's test range. Global root uniqueness is not claimed. External independent audit and validation have not been performed.
