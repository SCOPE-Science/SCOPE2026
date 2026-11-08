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

Finite verification was carried out with the accompanying `verify.py` (Python 3 standard library only). It independently enumerates all offered subsets and collection histories for selected small systems, compares their exact rational completion-time distributions with the independent geometric-stage calculation, checks all stage-level inequalities over finite ranges, and evaluates the limiting Euler products, moments, and the no-delay first-order correction at high precision.

The checker passed 598 finite assertions. The identities for independent phases, coupling domination, total-variation bound and positive sharpness coefficient are proved in `RESULT.md`. No finite numerical test certifies an infinite-dimensional or asymptotic theorem; no independent mathematical audit has been performed. The focus is the regime where the offer size is a fixed positive fraction of the alphabet size.
