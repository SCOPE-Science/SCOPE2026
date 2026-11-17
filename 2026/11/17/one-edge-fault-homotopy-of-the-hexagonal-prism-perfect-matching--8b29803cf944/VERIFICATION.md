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

# Reproduction

Run `python3 fault_n6_verify.py` in Python 3 using only the standard library. The enclosed `fault_n6_output.txt` records actual successful output. Graph edges, perfect matchings, downward-closed simplicial faces, acyclic discrete-Morse pairing, signed gradient-path cancellation, boundary matrices, and unit-minor conditions are reconstructed from scratch. Both edge orbits are checked; vertex-transitivity within each edge orbit gives the classification for every graph edge.

The number of graph edges is 18. For rung deletion, 12 facets, 562 augmented faces and 279 face pairs leave critical cells in dimensions one and two only. For rim deletion, 14 facets, 598 augmented faces and 296 face pairs leave one, four, and one critical cells in dimensions one through three. The signed Morse matrices are printed by the script and satisfy the chain relation.

# Limits

This verifier exhausts a specified finite graph. The topological identification also uses standard CW cell cancellation and the Hurewicz identification of second homotopy for a simply connected two-dimensional wedge. The checked code cannot establish novelty against every inaccessible or unindexed source. Independent external validation has not been performed.
