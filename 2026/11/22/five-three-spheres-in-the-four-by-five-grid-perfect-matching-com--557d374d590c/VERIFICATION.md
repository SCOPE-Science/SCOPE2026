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

# Reproducible finite verification

Run `python3 check_4x5_perfect_matching.py` with Python 3 (standard library only). It regenerates all graph edges, all 95 perfect-matchings and all 50,462 nonempty faces, and proves exhaustive face generation by the least-unmatched-vertex recursion.

The script constructs a full acyclic face-poset matching, counting 25,227 pairs and checking precisely one critical zero-cell, one critical two-cell and six critical three-cells. Independently it reverses matched Hasse edges and topologically sorts every one of the 50,462 vertices across 289,078 incidences, excluding all closed gradient paths. It then computes the exact signed integral Morse differential `(1, 0, -1, -1, 0, 0)` from critical three-cells to the unique critical two-cell. A unit entry proves the cellular cancellation and thus five three-spheres by standard CW theory.

The exact expected terminal marker is `GRID_4X5_PERFECT_MATCHING_OK`. The checker is a complete finite mathematical certificate for this graph, not a proof for larger graph families. Its code and its output cannot independently certify publication priority. Independent mathematical audit has not been performed.
