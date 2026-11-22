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

# Reproduction and limits

From this directory, run `python3 check.py` (Python 3 standard library only). A successful execution prints `PASS: exact 2x2 matrix equalities, 2x2 sharp angular test, 9800 finite endpoint tests`.

The checker compares both sides of the two-by-two Schur/Loewner equivalence on 1,400 rational test matrices and checks seven finite coarse-endpoint maps per matrix by separate forward substitution. It also checks exact \(\theta=0\) and \(\theta=\pi/4\) matrices, the determinant at four rational unit-circle angles, and the instability of the noncommuting example. Random choices use fixed seed `34011` and exact `fractions.Fraction` arithmetic.

Finite checks do not prove a claim in arbitrary dimension. The proof uses algebraic identities, a positive-definite similarity, the symmetric Schur-complement theorem, and a two-by-two determinant sign characterization. The endpoint result assumes exactly specified coarse initialization, one exact FCF sweep, and the long-trajectory limit; no finite-precision or nonlinear result is claimed. Independent audit has not been performed.
