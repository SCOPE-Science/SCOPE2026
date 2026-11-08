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

Both Python 3 standard-library programs were run on the exact packaged source files and produced `VERIFY_OK`. `verify_functional_graph.py` iterates all \(3^{12}\) encodings, builds indegrees, peels noncycle states, then propagates entry times backward. `verify_trajectories.py` instead uses a separately coded local update, a distinct LCF graph construction and a path-memoization decomposition. Their complete 74-class census digest is identical, and their primitive orbit counts, maximal time, and 3 extremal configurations agree after the explicit graph isomorphism.

The standalone files `census.json`, `extremal_witnesses.json`, `functional_graph_output.txt`, and `trajectories_output.txt` are complete outputs, not samples. They are not a substitute for independent external review. The finite classification makes no assertion for other graphs.
