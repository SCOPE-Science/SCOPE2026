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
# Reproducibility

Run `python verify_leaf_pruning.py` with Python 3. The program has no dependencies outside the standard library. It enumerates small bipartite defect graphs, constructs the associated simplicial complexes directly from independent subsets, checks every intermediate free-face pair and the exact final face set, and computes mod-two Betti groups for forests. `verification_output.txt` records an actual execution of the included script.

The verification is finite: 592 exhaustive small graphs, 48 deterministic additional examples, 440 forest homology checks, and 1,399 elementary-collapse pairs. The all-size, integral, and simple-homotopy assertions are proved in `RESULT.md` and are not inferred from the test set. The relative collapse formula is proved by a descending-cardinality free-face argument; the forest classification follows by iterative pruning and a graph homotopy calculation. No external independent audit has been performed.
