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

# Reproducible checks and boundaries
Run `python3 verify_row_parameter.py` and `python3 verify_independent.py` from the extracted artifact directory. Both require only Python 3 standard library.

The first script generates all balanced 3-by-3 integer tables by choosing four free corner entries and inferring the other five; for each margin from one through eight it generates every signed 2x2 rectangle move, verifies connectivity and every vertex eccentricity, and counts all unordered pairs at the maximum distance. The second script independently enumerates all triples of row compositions, filters the column margins, rebuilds the nine rectangle generators, runs complete breadth-first searches, and verifies the extremal pairs as the six disjoint permutation-multiple pairs. It also checks the nine potential step bounds and the explicit three-move shortcut.

Both scripts were executed successfully from the artifacts used to build this package. Their finite domains are only n=1..8; the all-positive-n conclusion follows from the mathematical proof in RESULT.md, not from extrapolating their output. No independent scholarly audit has been performed.
