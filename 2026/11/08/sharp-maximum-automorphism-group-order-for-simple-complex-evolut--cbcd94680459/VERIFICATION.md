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

# Verification

Execute `python CHECK.py` with standard Python 3. The output is recorded exactly in `CHECK_OUTPUT.txt`. The checker verifies all individual period bounds for dimensions 1 through 100, the small-dimensional extrema, the complete dimension-six base row, and the factorial inequality at the induction base and in this finite range.

The all-dimensional conclusion is proved by the graph-kernel, graph-period and factorial-induction arguments in RESULT.md. The finite computation cannot independently certify arbitrary graph support patterns or every positive dimension. The two equality examples have explicit structure matrices and groups justified in the proof. Independent audit has not been performed.
