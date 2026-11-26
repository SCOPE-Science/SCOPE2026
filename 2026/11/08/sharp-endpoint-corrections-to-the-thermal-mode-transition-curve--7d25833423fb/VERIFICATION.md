---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The endpoint corrections follow from the endpoint-subtracted beta integral at small shape and a uniform Laplace estimate near shape one. The unique transition and its identification with the curvature zero are prior results cited in `RESULT.md`. The latter also derives the upward root crossing needed for the asymptotic sign brackets.

The unchanged companion `check_phase.py` uses `mpmath`: run `python check_phase.py` in an environment with that dependency. It tests the two endpoint expansions at selected parameters, as well as identities for the previously known phase boundary. These are finite numerical diagnostics, not proofs of the asymptotic error bounds.
