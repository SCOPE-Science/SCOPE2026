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

The theorem is proved by a truth-table reduction and a bijection with upsets of a finite induced product poset, not by finite enumeration. The standalone `newcheck.py` independently enumerates all three-grade labelled matrices for up to four worlds and checks their original Łukasiewicz transitivity inequalities against the proposed threshold-relation conditions. It then enumerates all labelled posets up to size four, independently computes their upset counts and verifies the Stirling reconstruction. For chain cores it checks the Catalan specialization through seven classes.

Verified direct frame counts: 1, 9, 281, 29027. Verified labelled-poset counts for one through four elements: 1, 3, 19, 219. Verified aggregate upset counts: 1, 8, 256, 27434. The computations are exact integer operations. There is no exhaustive test beyond four worlds and no independent historical-priority examination. The general arbitrary-size assertion depends on the proof in RESULT.md.
