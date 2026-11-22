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

The accompanying `verify.py` can be executed with Python 3 and the standard library only. It calculates the one-pass bubble-sort image of each generated source, and independently computes actual neighboring swaps and breadth-first-search connected components of every image fiber through length eight. It compares the exact component-size multiset, per-fiber edge counts, uniqueness of source encodings, and the global connected-fiber count. The enumerator is also checked symbolically in integer arithmetic for lengths through 250.

These finite tests confirm the proof's formulas in the stated test range but do not replace the all-length argument. The decisive theoretical verification consists of the record-subset preimage parametrization, the one-record-change lemma for adjacent transpositions, and the frozen-coordinate product decomposition, all written explicitly in `RESULT.md`. No external mathematical audit or formal machine-checked proof is claimed.
