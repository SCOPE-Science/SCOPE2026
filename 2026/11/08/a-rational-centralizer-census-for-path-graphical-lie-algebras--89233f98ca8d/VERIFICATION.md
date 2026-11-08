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

With Python 3, run `python verify.py` in the directory containing this file. No dependencies beyond the standard library are needed. A successful run reports `VERIFY_OK`.

The checker calculates actual centralizer row spaces from the edge determinant matrices using finite-field row reduction, and counts distinct row spaces. It compares the counts with the generating-function recurrence for field orders 2, 3, 4, and 5 and specified bounded path lengths. The field with four elements is constructed independently as a polynomial quotient. A second algorithm classifies all binary support patterns by their nontrivial runs and forced-zero positions and compares weighted counts through length 17. Results are finite checks only. General validity follows from the kernel classification, uniqueness of canonical output words, and the seven-state transfer calculation in RESULT.md.
