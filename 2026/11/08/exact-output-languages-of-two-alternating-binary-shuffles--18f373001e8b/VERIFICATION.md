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

# Reproducibility notes

Run `python3 checker.py` with Python 3 and no third-party packages. The checker enumerates every source-position mask for both inputs for each integer parameter from one through five, removes duplicate output words, independently evaluates the prefix-height condition and two-letter block-language condition, and asserts exact set equality. It also checks each displayed cardinality and intersection and prints `PASS` if every assertion succeeds. The checked cases are finite, and general correctness relies on the mathematical proof in `RESULT.md`. No external or independent validation has been performed.
