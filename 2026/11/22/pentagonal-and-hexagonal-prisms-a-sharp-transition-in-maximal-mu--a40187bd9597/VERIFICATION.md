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

Finite exact checks: `verify_paths.py` enumerated every shortest path internally for all vertex pairs of each graph and evaluated every vertex subset; `verify_bfs.py` independently tested whether each pair stays at its original distance after deleting other selected vertices. Both implementations agreed on the entire feasibility bitmap, the sorted minimum-maximal masks, the two maximal-set polynomials and all relocation graph size and distance metrics. The scripts are standalone Python 3 programs requiring no third-party package. `paths_results.txt` and `bfs_results.txt` contain their saved actual outputs.

No general assertion for other cycle lengths was verified or claimed. There has been no independent scholarly audit.
