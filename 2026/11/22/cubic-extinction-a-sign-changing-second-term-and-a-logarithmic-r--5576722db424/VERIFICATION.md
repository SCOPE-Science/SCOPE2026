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

## Reproducible checks
- Run `python check.py` in the directory containing this file. SymPy is required.
- Symbolic identities: exact change of coordinates, cubic, quartic and quintic coefficients after third-order locking, and the \(\gamma=1\) coefficient of the inverse-square logarithm.
- Finite trajectory diagnostics: positive states and leading/next-order asymptotics for \((\gamma,m,\delta)=(1,1,1),(2,1,0.8),(0.5,2,1.5)\). They are not infinite proofs and converge slowly at some parameter choices.
- Analytic proof: invariant-wedge contraction, positivity, slow-fast tracking, reciprocal-square summation and summable residuals are written in `RESULT.md`.

## Unproved limits
No claim outside the stated local wedge, no claim at the prey flip boundary \(\delta=2\), and no numerical inference of global attraction. Independent mathematical validation has not been performed.
