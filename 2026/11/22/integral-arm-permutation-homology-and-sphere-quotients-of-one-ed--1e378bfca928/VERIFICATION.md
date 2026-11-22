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

# Reproduction and limits

Run the standard-library script `python3 verify.py`. The attached `verification_output.txt` records the actual output from the final script, not an extrapolated table. The checker computes the graph metric by breadth-first search, all faces of the scale-two clique complex, and an independently assembled union of the prescribed octahedra and full simplices. It verifies exact face equality, computes every reduced mod-two Betti number, and calculates signed simplicial Lefschetz traces for pole reversal and a transposition of arms. All tests for two through six arms pass.

The executable checks do **not** independently certify every possible number of arms or every subgroup quotient. Those statements are justified by the uniform graph-distance enumeration and the finite-group CW quotient argument in RESULT.md. Integer orientation is proved by the signed three-coordinate determinant in the same document; the finite signed-chain traces supply a separate consistency check. Independent outside review has not been performed.
