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

# Verification of the four-channel pulse theorem

Reproduce by running `python3 checker.py` in the directory extracted from this package. Python standard library only, no internet or prior record dependencies. This program reconstructed and exactly checked the full polynomial identity using signed integer coefficient arrays; directly evaluated the exact three-channel alias in rational arithmetic; and checked 1312 counted cases, including independent quadrature and numerical physical parameters. Replayed at package location with output: `PASS 1312 independent counted checks; factorization symbolic, all interval signs analytic`.

The universal identity is established by polynomial equality (not by enumerating sampled parameter values). Strict positivity of its factors for all physically admissible values gives the sign conclusion. The equality at zero gap follows by pulse merging. The unique intermediate-gap maximum follows analytically from the strictly negative second derivative of the log contrast. The explicit radical alias places both candidate histories in the same finite observation horizon, ruling out a universally successful three-rate classifier.

Independent audit status is not_performed. Real sensors may have uptake-rate uncertainty, non-first-order kinetics, background contamination and noise; this result does not quantify statistical classification error or implement a field measurement. Open full-text access to several closely related historical studies was limited; historical novelty remains provisional.
