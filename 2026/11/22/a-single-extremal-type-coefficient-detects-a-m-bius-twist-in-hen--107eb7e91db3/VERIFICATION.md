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

# Reproducibility and checked limits

Run `python3 checker.py` with standard Python 3. The program constructs explicit ordinary and twisted rail systems, confirms the graphs are simple cubic and triangle-free, enumerates all edge covers at widths four through six, compares all cardinality coefficients, and independently enumerates every permissible line-graph singleton neighborhood at widths four and five. Site-variable specializations with unequal rail/rung weights are checked by brute force at widths four and five, and transfer traces are compared through width twelve. The recorded output is in `checker_output.txt`.

The all-width, full-multivariate assertion is proved by the two-dimensional row-swap decomposition in `RESULT.md`; exhaustive verification of small graph instances is not an infinite proof. There is no external independent audit and no claim of computational validation beyond the stated ranges.
