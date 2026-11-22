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

## Reproduction
Run `python3 verify.py` with ordinary Python 3, without optional packages. The script recomputes all prescribed n-window edge multiplicities rather than reading a prior output. It checks 80 parameter families with alphabet sizes from one to four and window lengths from two to six, bounded by 20,000 constructed cyclic positions. For eight small parameter families it also exhaustively enumerates every shorter labeled alternating circular word and confirms no cover occurs.

The observed result was: `VERIFY_OK: 80 constructive tour families and 8 exact exhaustive shorter-cover obstructions`.

## Mathematical verification boundary
The exhaustive tests establish their finite checked cases only. General correctness follows from the word-edge correspondence, the per-vertex degree-deficit lower bound, the bijective one-place-rotation edge additions, strong connectivity and the existence of an Euler circuit. The source correspondence and both parity cases are detailed in `RESULT.md`. No independent external review is claimed.
