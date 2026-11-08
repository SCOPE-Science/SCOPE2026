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

Run `python checker.py` with Python and NumPy. The program verifies the explicit real-matrix representation of conformal/anticonformal operators, computes group numerical radii separately using symmetric-matrix eigenvalues, and compares them against the scalar formulas. It verifies the inequalities, equality witnesses, and rank-one modulus criterion for tested group orders, completing 11,998 finite assertions with no failure.

These finite checks do **not** establish completeness of a search over all matrices, correctness for arbitrary group orders, or nonexistence of prior equivalent theorems. The analytical derivation of the exact formula, the elementary angular-support bound, and density of infinite circle subgroups are the proof of the universal result. No independent audit is represented.
