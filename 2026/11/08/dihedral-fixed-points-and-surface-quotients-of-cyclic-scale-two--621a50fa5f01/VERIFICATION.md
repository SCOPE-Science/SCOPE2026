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

The standalone `verify.py` rebuilds cyclic scale-two clique complexes for 7 through 30 vertices and tests the full invariant-simplex posets for all reflections and all nontrivial rotations, as recorded in `verify_output.txt`. It checks 864 transformations without relying on a precomputed face table. The infinite-family statement is proved in `RESULT.md`; finite tests are only corroboration. The homeomorphism classification additionally uses the standard compact-surface theorem and the Burnside Euler formula. Full text of the motivating preprint was not accessible.
