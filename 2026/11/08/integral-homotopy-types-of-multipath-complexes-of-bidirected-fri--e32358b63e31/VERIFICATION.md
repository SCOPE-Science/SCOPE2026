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

# Verification

Run `python3 verify_friendship.py` in a clean directory with Python 3. It independently enumerates every directed-acyclic indegree/outdegree-at-most-one face, builds the prescribed hub-fiber matching, verifies all reversed Hasse arrows yield an acyclic directed graph, checks the simplicial retraction on every face, and computes reduced mod-two chain ranks for the smaller cases. The output is reproduced in `verification_output.txt`.

The program checks the finite cases with one through six petals, including 295128 incidence relations for six petals. The mathematical proof uses a hub-pattern fiber classification, the standard poset patchwork lemma, a simplicial retraction onto the peripheral join of zero-spheres, and the identification of degree-zero sphere self-maps as nullhomotopic. The computation corroborates those local formulas but is not substituted for the infinite-dimensional induction/argument.

No independent external mathematical validation has been performed.
