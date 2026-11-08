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

The local symbolic certificate is `verify.py`, which reconstructs the finite-state generator, performs exact rational stationary perturbation, and checks both current coefficients and the polynomial's sign pattern. The sign theorem additionally uses Descartes' rule and continuity, so numerical root-finding does not substitute for uniqueness. The proof applies only to the explicitly normalized birth/death and site-departure hopping rates. No full-bias cancellation or asymptotic large-system claim is certified.
