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

The self-contained program `verify_three_deck.py` uses position-based subsequence dynamic programming, not the quadratic gap formulas, to generate deck signatures. It exhaustively checks all three-one binary words for lengths 3 to 30, verifies all two-member classes, their unique partner involution, every pair-count coefficient and the number of distinct decks. Command: `python3 verify_three_deck.py 30`. Observed output: `VERIFY_OK n=3..30 words=31465 pairs=2933`.

Independent symbolic expansion of both relevant quadratic subsequence-count differences gives `s*(z-y+3*s)`. The finite program is a check, not a proof for unbounded length. The full proof appears in RESULT.md. No independent human review or external mathematical certification is claimed.
