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

The universal classification is the six-step proof in RESULT.md. In particular, the graph model is obtained by a complete support-size argument, and the fundamental group follows from its full vertex and edge counts. It does not depend on a numerical extrapolation.

Run `python check_sparse_frames.py` in this directory to enumerate the exact graph in degrees 2 through 6. The script checks the number of signed coordinate injections, all distinct neighbors, regular degree, connectivity by breadth-first search, exact edges, and the cycle-rank formula. A successful run ends with `SPARSE_REAL_FRAME_GRAPH_EXACT_OK`.

The finite check is a reproducibility aid, not a substitute for the proof at arbitrary dimension. The standard fundamental group of the real Stiefel manifold is used only for the final comparison; the surjective loop is explicitly constructed. No independent mathematical audit or external certification was performed.
