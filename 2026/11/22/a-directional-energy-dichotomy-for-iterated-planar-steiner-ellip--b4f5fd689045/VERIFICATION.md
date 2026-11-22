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

# Verification notes

The exact scalar recurrence follows from centering perpendicular chords of a positive-definite ellipse matrix. Its loss identity is a rational algebraic identity, and the infinite-energy conclusion uses the uniform lower loss bound; the finite-energy converse uses positivity of convergent products. Finite arithmetic checks cannot replace these arguments.

The standalone `checker.py` numerically verifies direct matrix symmetrization against the derived scalar recurrence, invariance of determinant, the loss identity, the iterative 45-degree law and the cumulative energy envelope. It requires Python 3 standard library only. The deterministic pseudorandom seed is fixed; run `python3 checker.py` from the extracted file set. Its tests do not test every direction or prove originality.

Literature comparison was based on accessible source passages from arXiv:2610.05113v1, arXiv:1206.2041 and arXiv:2611.21167v1. Historical priority remains subject to independent checking. No independent audit has been performed.
