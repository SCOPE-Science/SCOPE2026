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

Execute `python verify.py` from a directory containing the standalone checker. It uses only the Python standard library. For every unordered shore split with three through eight labeled candidates, the checker constructs the domain directly, performs a multi-source breadth-first search in the adjacent-swap graph of all rankings, and independently checks the shortest distance from **every** ranking. Rational exact arithmetic is then used to compare the complete empirical mass function, expectation, and normalized diversity formula against the claimed values. A successful run prints `PASS` with the exact number of cases and checked rankings.

The experiment exhausts the finite indicated cases only; the proof handles arbitrary positive integer shore sizes and the limiting distributions. Independent scientific auditing has not been performed. The code makes no network calls and uses no external source content.
