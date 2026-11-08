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

Run `python3 check_five_runs.py` using Python 3 without third-party packages. This independently constructs the finite binary word for every \((a,b,c,d,e)\in\{1,\ldots,6\}^5\), extracts distinct contiguous palindromes by center expansion, and compares the *entire* factor set with the transition-based classification; it additionally tests the numerical defect. All \(7776\) factor-set and \(7776\) defect comparisons passed. Every fixed-length spectrum for \(5\le n\le30\) was also exhaustively compared to the claimed interval.

These tests are finite corroboration only. For all unbounded positive run lengths, the proof derives the classification from the maximum of four transitions, counts family overlaps and gives an explicit witness for every attainable defect. No external/independent review or formal proof certification was performed.
