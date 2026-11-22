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

# Reproducibility and evidence

Run `python verify.py` using Python 3.10+ with `sympy` (tested with SymPy 1.14.0). The script reads no external files, makes no network requests, and checks the exact posterior-risk identities, factored derivative, algebraic constants and high-noise gain ratio. It also independently computes numerical Simpson integrals of the piecewise bridge cross covariance at ten nontrivial observation locations, and bisects the root for eight different noise levels, checking that the resulting sensor dominates neighboring candidate times.

The reference execution printed `PASS: 87 exact symbolic and independent numeric checks.` Verification of infinitely many noise levels and global uniqueness relies on the separate sign proof in `RESULT.md`, not on a finite grid. No external independent mathematical validation has been performed. Source access restrictions and scope limitations are documented in `REVIEW.md` and `RESULT.md`.
