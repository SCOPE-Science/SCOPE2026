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

# Reproducibility

Run `python3 verify_examples.py` with Python 3.9 or later (standard library only). Observed output: `COMPONENTWISE_MARKOV_RATIONAL_CHECK_OK 4265`.

The exact-rational checks use three-component degree profiles, rational mass grids, connected-cover specializations, and the unbounded-price family. They test closed-form arithmetic identities and constraints. They do not search an infinite class of continuous maps or independently establish the topological two-map coverage lemma. That lemma and both distance equalities are proved analytically in RESULT.md.

The checked literature establishes the original connected-cover theorem. The originality comparison is best-knowledge rather than a certified priority search; Kim (1972) was not available in full text.
