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

# Reproducible checks

Run `python3 verify.py` using Python 3 and the standard library only. The program exhaustively groups every labeled word of the tested lengths by its complete palindrome-radius array, verifies the predicted maximum and unique maximizing array, and compares two different palindrome-fingerprint implementations on the smaller cases.

The verified ranges are \(q=4\), \(2\le n\le9\); \(q=5\), \(2\le n\le8\); and \(q=6\), \(2\le n\le7\). The code reports `FINITE_ENUMERATION_PASS` only after all assertions succeed. Finite enumeration is not the proof of an unbounded statement. The standalone proof is in `RESULT.md`.

The work is not an independent scientific audit. Historical priority remains subject to external verification, especially against the inaccessible complete text of the 2010 SPIRE chapter.
