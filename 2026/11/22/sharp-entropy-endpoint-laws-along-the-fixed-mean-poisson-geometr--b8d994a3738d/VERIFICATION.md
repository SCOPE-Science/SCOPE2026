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

# Reproduction and verification

Run `python3 verify.py` from a directory containing `verify.py` and `RESULT.md`. The code uses only Python 3's standard library and computes the finite Poisson–geometric masses using a stable positive recurrence.

The script compares numerical entropy values at 21 points for each of three fixed means, tests normalization, exact mean/variance, representative mass log-concavity, both quadratic endpoint constants, and the exact geometric endpoint score norm. Its observed success marker is `VERIFICATION_OK`. The code does not enumerate all integers or all parameters. The mathematical proof in `RESULT.md`, not these finite computations, establishes the infinite and continuum statements.

The first-public-source date is identified from the original 4 January 2023 arXiv submission; the 2024 journal date is not substituted for the earlier public date. The complete originating preprint and publisher article were unavailable for historical-priority comparison. This access limitation does not alter the displayed algebraic derivation. No independent external mathematical audit has been performed.
