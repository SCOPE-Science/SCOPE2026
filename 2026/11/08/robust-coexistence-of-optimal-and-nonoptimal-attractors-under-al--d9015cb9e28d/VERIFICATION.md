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

Run `python3 verify.py` in a directory containing the standalone `verify.py` with SymPy installed. The script uses symbolic exact algebra rather than finite floating-point orbit sampling. It verifies the ninth-degree factorization, nine exact fixed roots, the derivative multipliers, the strict nonminimum two-cycle, exact loss values, and the derivative nondegeneracy used in the real implicit-function theorem.

Recorded run output:

`VERIFY_OK exact_epoch_factorization=1 fixed_points=9 attracting=4 repelling=5 loss_mean=5/32 IFT_nondegenerate=2`

The open-neighborhood statement is proved by analytic dependence, simplicity of roots, continuity of multipliers, and fixed polynomial degree. No explicit largest safe neighborhood is claimed; finite computations alone do not establish this universal local statement. Global dynamics beyond epoch-fixed points and independent priority certification are outside the verification scope.
