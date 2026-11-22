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

The dependency-free program `checks/four_graph_threshold.py` exhaustively enumerates finite posets of sizes one through five after linear-extension relabeling. Its masks enforce every transitivity implication; graph signatures are canonicalized over every simultaneous vertex permutation; every higher-dimensional face is removed only in a checked free-face/coface pair. The checker verifies both six-point witness posets, exact graph equality and their face totals. Reproducing the check requires Python 3 and the extracted named file.

Expected output counts for sizes one through five are 1, 2, 7, 40 and 357 posets, with 1, 2, 5, 15 and 52 simultaneous four-graph classes and zero classwise weak-homotopy collisions. There is no claim of independent audit, of full published-priority coverage, or of an arbitrary-size finite-space theorem.
