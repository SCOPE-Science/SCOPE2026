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

Run `python3 checker.py` with Python 3 and no third-party packages. The script checks the BPL parameterization against the original convolution using exact rational arithmetic, compares the three-inequality decision to the sign of sixty consecutive canonical differences on 648 rational parameter pairs, and reproduces the rational creation/destruction witness. On completion it prints `PASS` with the exact fractions.

Finite tests do **not** certify the all-index conclusion. The proof in `RESULT.md` derives the complete canonical sequence, uses an all-index exponential comparison to reduce infinitely many tests to two, and applies Steutel–van Harn's published characterization. No independent audit or external certificate has been performed. Historical priority is not guaranteed by a search.
