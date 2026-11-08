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

The closed finite sum in RESULT.md is derived from an exact all-length run classification; finite programs are checks rather than a proof by enumeration.

Run `python3 code/formula_check.py` to check the sharp integer incidence intervals for run counts through eight and compute the sum through length 30. It prints `EDGE_INTERVAL_OK` and `FORMULA_CHECK_OK` on success.

Compile `code/direct_enum.cpp` with `c++ -std=c++17 -O3 -o direct_enum code/direct_enum.cpp`, then run `./direct_enum` to count the 14-coordinate array for every indexed binary word through length 20. The counts must match `data/counts_1_20.tsv` and the first 20 terms of the formula script.

Run `python3 code/threshold_check.py` to independently verify that length-four compositions do not refine shorter-read classes at lengths one through seven, but do refine them at length eight. It prints `SHARP_READ_THRESHOLD_OK` on success. The proof gives an explicit pair of witnesses for every length eight or more.

These executable tests do not independently certify historical priority, a complete literature search, or the unbounded theorem. The mathematical proof states the unrestricted steps separately. No independent scientific audit has been performed.
