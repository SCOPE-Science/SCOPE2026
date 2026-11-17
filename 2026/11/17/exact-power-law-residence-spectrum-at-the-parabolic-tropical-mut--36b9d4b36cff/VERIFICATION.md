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

The theorem is established by the exact affine reduction on the critical switching wedge and a two-dimensional area integral. The pointwise exit condition, finite-horizon survivor polygons, and all conditional distributions are included in `RESULT.md`.

The accompanying `check.py` was run with the standard Python interpreter and printed `PARABOLIC_TROPICAL_RESIDENCE_EXACT_OK`. It checks multiple rational parameter settings, exact branch iterates and first-exit times, finite-horizon area identities and the truncated harmonic expectation, all with rational arithmetic. Finite checks do not independently establish the universal theorem.

A separate independent audit has not been performed. The statement does not assert anything about trajectories after their first exit from the parabolic sector.
