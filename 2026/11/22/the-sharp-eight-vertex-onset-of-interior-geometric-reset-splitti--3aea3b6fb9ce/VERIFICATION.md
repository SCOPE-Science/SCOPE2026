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

The mathematical proof uses the renewal quotient, exact tridiagonal inverse/continuant identities, a symmetric-similarity spectral factorization, and an elementary one-variable quadratic sign analysis. It covers every strictly positive nearest-neighbor transition environment on every path with at most seven edges (eight total vertices), including the endpoint values and strictness classification stated in `RESULT.md`.

`verify.py` is a standalone supplementary checker requiring Python 3 and SymPy. Running it from the delivered package produced `PASS: 801 exact algebraic/rational assertions; full theorem requires analytic proof.` It reproduced the illustrative critical survival probability approximately 0.9369685842877506 and minimal lower-exit probability approximately 0.6362752323028684. The checked finite grids are not evidence of exhaustive continuous-parameter coverage; that coverage relies on the displayed symbolic inequalities.

No independent audit or external proof certification has been performed.
