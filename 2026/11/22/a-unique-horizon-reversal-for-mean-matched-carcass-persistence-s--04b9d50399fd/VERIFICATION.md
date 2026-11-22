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

The theorem is supported by the full analytic derivation in RESULT.md, not by a finite search alone. The accompanying independent-standard-library checker evaluates the detection expectation using separate numerical arrival-time integrals, stresses the unique two-date optimum with a finite grid, verifies mixture-hazard variances, and compares the mean-matched schedules across random parameter samples.

To reproduce: `python3 checker.py`. Expected output: `PASS 60064 supplementary numerical assertions; finite diagnostics are not a proof`.

The scope excludes nonlinear arrival intensity, dependence among observations, unknown lifetime parameters, and realistic travel-time constraints. Numerical random testing is supportive only; neither real-data validation nor independent external mathematical audit has occurred.
