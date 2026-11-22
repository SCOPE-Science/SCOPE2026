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

# Verification of the punctured Lucas-cube routing theorem

The entire infinite-family distance, exceptional-pair and eccentricity assertions are proved in `RESULT.md`. `check.py` is a self-contained Python standard-library verifier; it requires no network connection, compiled extension or external dataset.

Run `python3 check.py` in the directory containing the files. For rim sizes \(3\) through \(8\), the checker independently enumerates the original helms' optimum independent dominating sets and direct adjacency-preserving token slides. For sizes \(5\) through \(13\), it enumerates all ordered pairs of states and compares BFS distances with the closed metric, plus the extremal formulas. It verifies the exact state and edge counts throughout. The tests terminate with an explicit `PASS` line.

The finite range is not a proof for larger rim sizes; the separate combinatorial argument establishes the all-size theorem. No independent mathematical audit has been performed.
