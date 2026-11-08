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

# Mathematical verification

The independent standalone `verify.py` assembles the transient generator directly, verifies its resolvent and determinant, differentiates the survival transform with respect to the allocation product, checks the fourth-order short-deadline coefficient, and tests exact expected times and finite-horizon matrix exponentials for several asymmetric rates and both endpoints. A complete execution passed 541 assertions with Python 3, SymPy, NumPy and SciPy.

The full strictly positive survival gap for all real positive deadlines comes from the reversible-generator Dirichlet form, positive exponential convolution and strict positive absorption-density convolution in `RESULT.md`. Finite checks are diagnostics only and cannot establish the infinite quantifier. The scope is closed two-patch occupancy, initial joint occupation, and fixed total rescue budget; the singleton starting-state expansion shows that dropping the initial-state condition changes the optimization.

No independent external validation is asserted.
