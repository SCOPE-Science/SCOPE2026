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

The theorem is proved symbolically using the two independent coefficient directions in multiplication, Euclidean orthogonality of natural bases, graph joins, and an exact cut minimization. The finite checker provides corroboration only, not an infinite proof.

Run `python3 checks/verify.py` from the artifact root. This standard-library program reconstructs the original and integral transformed natural bases and their full structure matrices for each dimension from 3 through 10. It then exhaustively evaluates every Cheeger cut for both endpoint graphs and every intermediate complete-split graph, comparing against the stated closed formula. The expected output is recorded in `checks/output.txt`.

The realization of all intermediate graph types over the real field and the all-dimension result are mathematical proofs, not tested over all dimensions. Characteristic-positive and nonreal fields are outside the claim. Independent audit: not performed.
