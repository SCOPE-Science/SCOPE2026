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

# Reproducible mathematical checks

Run `python3 verify_cycle_edge_multiset.py` with Python 3.10 or later. The checker constructs each cycle by independent adjacency lists, computes all shortest distances by breadth-first search, then exhaustively enumerates all three-vertex subsets and all edge-distance signatures for every order from 3 through 28. It checks the exact gap criterion, the closed count, and the dihedral orbit divisibility for every order at least seven. The captured successful output is in `CHECK_OUTPUT.txt`.

The all-order proof in `RESULT.md` is mathematical: edge-centre isometries, a complete three-element permutation classification, constructive obstructions, integer-composition enumeration, and orbit-stabilizer. The enumerator is corroboration only, not a proof beyond the tested range. The known minimum cardinality three comes from the 2023 cited scalar theorem.

Same-model correctness, originality and value reviews passed. Independent scholarly validation has not been performed. Exhaustive publication priority cannot be guaranteed.
