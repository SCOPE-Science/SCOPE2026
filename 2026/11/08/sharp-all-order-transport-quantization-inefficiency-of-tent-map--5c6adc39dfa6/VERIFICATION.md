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

Run `python verify.py` using Python 3 and the standard library only. The program independently enumerates the inverse affine branches of each iterate, solves for their rational fixed points, orders the points and computes transport integrals by exact rational arithmetic.

The checker tests every integer \(1\le n\le10\) against the proved fixed-point grid and exact \(W_1\), \(W_2^2\), \(W_\infty\) formulas, as well as exact largest neighbor gaps. It also tests the \(p=3\) and \(p=4\) rescaled cost against a deliberately loose but rigorously numerical error envelope in rational arithmetic. The expected terminal message is:

`VERIFY_OK independent_inverse_branch_enumerations=10 W1_exact=10 W2_exact=10 Winfty_exact=10 max_gap_exact=10 higher_p_exact_Riemann_bounds=20`

These computations do not prove any all-\(n\) or all-real-\(p\) statement. The general theorem relies on the analytic semiconjugacy, monotone transport, elementary power sums and offset-grid Riemann limit proved in `RESULT.md`. Independent scientific validation has not been performed.
