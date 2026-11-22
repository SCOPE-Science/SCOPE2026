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

# Reproducibility and verification

Run `python3 verify.py` from the directory containing this document. The program uses Python's standard library only. It independently enumerates permutations and checks their classical pattern restrictions, recomputes all position-adjacent swap edges, checks degree multiplicities and graph edge counts, and computes all-pairs shortest paths at sizes 2 through 8. It checks the constructed Hamilton ordering through size 14. During preparation, all assertions passed. This is finite corroboration; correctness for every size follows from the proof in RESULT.md, particularly the local-move equivalence and the sharp diameter witness.

There has been no independent mathematical audit or external certification. Historical originality remains conditional on unindexed equivalent sources not discovered in the comparison.
