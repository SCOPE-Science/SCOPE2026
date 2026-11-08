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

# Verification record

The claim is the sharp stabilization and minimum separating size theorem for \(\alpha_k=(\Box\Diamond)^k\top\) on finite arbitrary Kripke frames. Its core argument is symbolic: the recurrence for first-failure sets is monotone; each newly failing rank has a successor of infinite rank and rank-controlled outgoing edges; and these witnesses assemble into a simple path of twice the failure rank. Directed paths attain equality.

`checker.py` is a standalone standard-library Python 3 file. The command `python3 checker.py` was executed on the packaged code. It exhaustively checks 66,066 finite frames on up to four worlds, samples a further 10,000 five-to-eight-world frames with a fixed seed, and checks thirty sharp path examples. It reports `ALTERNATING_MODAL_HALF_SIZE_OK`. Finite checks corroborate definitions and edge cases but are not general proof or exhaustive evidence above four worlds.

The source comparison is limited to the cited 2026 paper's material and available indexed records, plus general literature on modal approximants. The cited paper's upper-bound path and three small SAT minimality instances are prior results. Older inaccessible literature may contain equivalent formulations. No external independent validation is claimed.
