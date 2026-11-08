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

# Computational verification

Run `python3 verify.py` with Python 3.9+ standard library. It independently enumerates the conjugacy language and all its scattered subsequences, minimizes by distinct right-residual languages rather than relying on the claimed state-count formula, and checks each predicted residual language from the proof.

An execution returned `VERIFY_OK configurations=280 residuals=61585 accepted_words=61585`. The 280 configurations include exhaustive run-vector grids (2, 3, 4, 5 symbols) and 180 seeded further vectors of total length at most twelve. These are finite consistency checks and not an infinite-parameter proof.

The full parameter theorem requires the human-readable quotient classification and proof in RESULT.md. Its scope excludes words with repeated symbols in separate cyclic runs. Independent validation has not been performed.
