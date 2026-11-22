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

The embedded `verify_turan.py` enumerates each balanced complete multipartite labelled graph exactly once for the documented finite range, checks all pairwise exchange budgets, the sharp connectivity threshold, and the degree formula. The embedded `verify_visibility_turan.py` independently enumerates all root-edge graphs through six root vertices, checks the forbidden-four-clique condition and the first exchange threshold. Both run on Python 3 without nonstandard dependencies. See the proof for the unbounded argument; bounded enumerations are not proof for all parameters.

Scientific boundary: the known Turán equality characterization and the 2024 visibility correspondence are used as already established inputs. No independent audit is asserted.
