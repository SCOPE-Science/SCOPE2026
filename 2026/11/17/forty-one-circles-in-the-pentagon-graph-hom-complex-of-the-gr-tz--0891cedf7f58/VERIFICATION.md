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

# Exact finite verification

The standard graph-Hom polyhedral cell model is encoded as five tuples of nonempty 11-bit integers. The supplied `verify_hom.py` is standard-library-only Python 3 and `collapse_pairs.json` is a complete ordered list of 150 candidate free-edge/square removals.

Execute `python3 verify_hom.py collapse_pairs.json`. The script independently enumerates the 310 graph homomorphisms, checks that the fifth adjacency-matrix trace agrees, and enlarges all admissible coordinate subsets to reconstruct the entire finite face poset. Exhaustiveness follows because every valid box contains a singleton assignment, and one-coordinate-at-a-time additions inside that box are admissible. The script checks the full cell vector, the dimension upper bound, every square's four edges, and that each proposed removed edge is free in the *current* remaining complex. It then checks the entire remaining graph, its connectivity and cycle rank.

Expected reproduced outcome: 310 vertices, 500 edges and 150 square faces before collapses; 150 verified elementary collapses; connected residual graph with 310 vertices and 350 edges; cycle rank 41. A captured successful replay is included as `verification_output.txt`.

The finite certificate supplies a complete proof for this particular graph pair, not a sampling argument. Its correctness depends on the stated graph-Hom definition, the explicit enumeration and verification code, and the integrity of the supplied certificate. This is not an independent audit of the result.
