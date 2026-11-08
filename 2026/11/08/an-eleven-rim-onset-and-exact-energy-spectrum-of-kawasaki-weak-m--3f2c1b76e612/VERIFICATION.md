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

# Reproducibility and limits

The standalone `verify.py` requires Python 3 and no external packages. Run it from a directory containing the file, with `python3 verify.py`. It should print `VERIFY_OK` and its finite test counter. It derives the same energy-resolved count in three different ways: direct enumeration of all balanced wheel spin assignments and every adjacent exchange for odd sizes from 3 through 15; an independent cyclic forbidden-word transfer computation through rim size 47; and the published binomial finite sum. It also tests the direct forbidden-word criterion through size 11 and the eleven-rim cutoff through size 119.

The proof in RESULT.md is an all-size bijection; finite checks do not certify infinitely many cases. The polynomial counts weak exchange-local minima (no strictly decreasing adjacent exchange), not absorbing states under zero-energy hopping. Literature priority and independent scientific validation remain open.
