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

# Verification and limits

Run `python verify.py` with Python 3 and SymPy. The script reconstructs the exact movement generators, resolvents, next-generation infection matrix, transition matrix, and determinant from rational parameters. It checks the cubic determinant as an identity, exact rational sign brackets, and the small-contact bound. No floating-point output is used in a proof.

The monotonicity theorem is proved symbolically in RESULT.md by an M-matrix comparison for arbitrary finite numbers of patches and all admissible birth/ongoing vaccination increases. The exact witness uses two patches with strictly positive directed movement and transmission in every defined channel. Computations validate the supplied rational identity but do not substitute for the mathematical Perron–Frobenius/rank-one threshold argument.

A source-priority risk remains from inaccessible full text of one relevant older mover–stayer vaccination paper; no independent literature priority certification or experimental validation is claimed.
