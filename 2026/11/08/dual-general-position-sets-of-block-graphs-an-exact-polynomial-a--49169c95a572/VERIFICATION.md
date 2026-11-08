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

# Reproducibility and limits

Extract `verify.py` alongside this file and run `python3 verify.py` using Python 3. The verifier uses only standard-library modules and is finite. It separately builds graphs, computes their biconnected blocks by depth-first search, identifies articulations by deletion, and enumerates dual general-position sets directly using BFS distances and geodesic distance equalities. It tests all labeled connected graphs on at most six vertices, retaining every block graph, and adds thirty deterministic clique-glued block graphs at each order from seven through eleven. For every selected graph it checks the entire predicted cardinality distribution, exact exceptional-set family, and hereditary criterion.

Observed stdout:

`VERIFY_OK graphs=4943 subsets=414102 dual_sets=89688 exceptional_sets=7822 all_labeled_n_le_6=PASS deterministic_glued_cliques_n_7_to_11=PASS hereditary_boundary=PASS`

No sampling claim is made for all graphs of larger orders, and no finite enumeration proves the infinite theorem. The unrestricted correctness argument is in `RESULT.md`. Independent mathematical validation has not been performed.
