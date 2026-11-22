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

The theorem is proved algebraically in `RESULT.md`. The checker `verify.py` enumerates all feasible cyclic subsets, generates moves from the definition, computes every directed shortest-path distance by breadth-first search and separately calculates the prefix-flow formula, then compares them. It checks the state formula, directed diameter, and exactly one diametral ordered pair per cyclic rotation. On the tested range it completed 73 parameter cases and 1,896,844 ordered-pair comparisons (see `verification_output.txt`).

Finite testing cannot establish the unbounded theorem, rule out unpublished priority, or independently certify publication suitability. No external independent mathematical audit was performed.
