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

# Reproducibility

Run `python3 verify_rank.py` with Python 3's standard library in the directory containing `RESULT.md` and the checker. The checker performs nine exact Gaussian-elimination rank cases, with pole orders one through four and selected polynomial terms, and 729 checks of the direct harmonic-projection formula for commutator entries. It completed successfully in the inspected package.

The proof of the infinite formula requires the independent exponential-polynomial feature lemma and anti-diagonal block-rank argument in `RESULT.md`; no finite computation can replace them. The full text of the older 2013 rank paper was not available, and bibliographic novelty remains qualified. No independent audit has been performed.
