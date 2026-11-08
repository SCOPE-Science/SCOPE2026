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

Run the attached self-contained `verify_signed_language.py` with Python 3 (standard library only). The script computes the Rule 30 predecessor graph from the eight local truth-table entries. It checks the exact recurrent off-diagonal states and the orientation signs of all seven quotient transitions, then independently checks the signed-graph language, the cyclic signed-block language, and direct enumerated predecessor counts for each output of every ring length from 3 through 16.

Expected terminal text:

```
INDEPENDENT_PAIR_GRAPH_REDUCTION_OK 12 offdiagonal, 8 recurrent
SIGNED_BLOCK_LANGUAGE_EQUIVALENCE_OK 3..16 131064 targets
```

These exhaustive finite tests do not assert an all-length proof; the all-length proof follows by finite graph reduction, exact characterization of arbitrary closed walks, and the even-flip lift condition given in `RESULT.md`. No external proof assistant, independent human or external review was used.
