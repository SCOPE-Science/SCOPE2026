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

The proof reduces the entire standard domination game on the explicitly defined twenty-vertex graph to a strictly increasing finite dominated-mask game. Replaying `artifacts/game_dp.cpp` (C++17 bottom-up evaluation over all \(2^{20}\) states) and `artifacts/game_dp.py` (independent Python memoization) confirmed that both root scores and all 760 conditional first-two-move scores agree with the claim.

Both checkers reconstruct \(\operatorname{GP}(10,2)\), assert degree three, perform graph-distance checks at all twenty vertices, and verify the exact distance response table for both starting conventions. See the included output files. The count 760 refers to \(20\cdot19\) ordered opening/reply pairs under each of two starting conventions; it does not imply there are 760 distinct dominated masks.

This is a finite computation-supported mathematical proof. Its correctness depends on the accompanying source, the explicit recurrence and the completeness of the twenty-bit state enumeration; no independent audit or proof-assistant verification has been conducted. Historical-source priority remains qualified by the limits reported in `REVIEW.md`.
