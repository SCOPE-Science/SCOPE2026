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

## Direct computation

The standalone `checker.py` constructs basis products in each finite incidence algebra, rather than substituting the theorem's orbit formula into its own verification. It enumerates candidate involutions by their actual square equation, then tests multiplication and pairwise commutativity of each ordered tuple. It separately enumerates graph colorings and all spanning edge subsets. The results are recorded in `checker_output.txt` and end with `INCIDENCE_TUPLE_POTTS_DIRECT_PASS`.

The tests include a three-element chain and a four-element diamond, both of which have nonzero products of off-diagonal radical elements, so the evidence does not apply only to radical-square-zero algebras. Cases over fields of size three and five and tuple lengths one, two, and three pass. Computation is finite evidence; the all-poset theorem rests on the orthogonal-idempotent conjugation and orbit-stabilizer proof in `RESULT.md`.

## Limits

The checker handles prime fields via integer residue arithmetic; the paper's proof, which uses only field algebra and counting cardinalities, covers all odd prime powers. The checker is independent of the orbit proof but is not an independent mathematical audit. No external proof certification was performed.
