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

Run `python3 verify.py` using Python 3 standard library only. The verifier constructs graphs from adjacency definitions, tests the total-visibility full-fiber criterion for every vertex subset of small connected labeled base graphs with uniform and nonuniform clique sizes, and independently computes full-set and maximal-set cardinality counts. A separate geodesic BFS routine checks the distance-two test against the original shortest-path definition for four additional substitution profiles. The cycle cases additionally use mod-two boundary matrices to verify their predicted single reduced Betti numbers. The recorded local run returned `VERIFY_OK direct_geodesic_subsets 5632 profiles 814 tested_subsets 775472 facets 4969` and passed all six cycle tests. The unrestricted result follows from the written proof and the cited abstract composition theorem, not from finite enumeration. Integral torsion preservation is mathematical, not an empirical inference from mod-two ranks.
