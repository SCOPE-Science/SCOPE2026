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

Run `python3 spectral_check.py` with the Python standard library (no downloads required). Actual execution passed for every integer \(2\le n\le48\): 47 independent rational Cox–de Boor collocation matrix and affine-reproduction checks, 1,175 trigonometric eigenpair identities and 1,316 finite iteration-expansion equalities. Additional analytical checks independently establish the two endpoint rows, the anti-reflection ghost conditions, orthogonality of the half-grid sine basis and the \(n^{-2}\) gap limit. A finite checker cannot prove an all-dimension theorem and does not independently certify the mathematical novelty of the result. Reproduction involves precisely the clamped knot sequence and degree-two Greville nodes defined in `RESULT.md`.
