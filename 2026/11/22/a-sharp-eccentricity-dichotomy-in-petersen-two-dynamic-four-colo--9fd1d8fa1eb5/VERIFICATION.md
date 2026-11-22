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

The finite-domain check uses two standalone sources included in the same package. `verify_kneser.py` generates proper set partitions on the disjointness graph of the ten two-element subsets of a five-element set, checks the neighborhood condition, verifies all four group orbit equalities, and applies four breadth-first searches. `verify_gp.cpp` independently builds the ordinary generalized Petersen graph with ten vertices, enumerates named proper assignments, and applies breadth-first search from all 5760 valid four-colourings. Both programs were run on their embedded sources and their stdout compared byte-for-byte with the included expected output files.

Exhaustive scope: all proper three- and four-palette assignments; all valid four-palette recolouring adjacencies; every starting state via four verified symmetry classes in one implementation and every single starting state in the other. In particular, absence of a three-colour solution comes from exhaustive testing of all 120 proper named three-colourings, not an unsupported computational timeout. The full pair-distance histogram has total \(\binom{5760}{2}\).

Limits: computations establish a finite theorem about the ten-vertex Petersen graph only. The historical-priority comparison relies on accessible published sources and record searches; inaccessible full texts and unindexed historical findings may exist. No external scholarly audit or independent certification is represented as completed.
