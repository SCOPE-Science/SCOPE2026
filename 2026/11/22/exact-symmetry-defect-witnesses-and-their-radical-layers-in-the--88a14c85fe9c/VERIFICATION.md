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

# Exact finite checks

`CHECKER.py` directly builds the ring from the eight-element group law and checks the group axioms, the \(256\)-element multiplication table, the radical dimensions, the complete \(65536\)-pair rank census, and the \(16777216\)-triple witness census. The two computational counting methods agree on \(147456\) and the exact valuation profile.

Verified command: `python3 CHECKER.py` (Python 3.10 or later). Observed terminal marker: `QUATERNION_SYMMETRY_DEFECT_OK`.

The kernel-rank identity is proved mathematically in `RESULT.md`; the program certifies the remaining finite numerical census by exhaustive integer loops. It neither certifies historical originality nor covers other finite fields or other minimal rings. No independent audit has been performed.
