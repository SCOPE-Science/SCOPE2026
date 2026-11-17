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

# Verification and scope
The analytical proof in `RESULT.md` is the evidence for the all-positive-initial-condition and all-real-parameter quantifiers. The standard-library checker `checks/check.py` was run on its actual packaged source before delivery and returned `VERIFY_OK positive_parameter_cases=5 iterations_per_case=1000 unstable_diagonal_fixed_point=1`. It directly checks five finite trajectories, mass ceilings, contraction after the first iterate, and the unstable longitudinal fixed-point witness. Neither the finite runs nor rounding can certify the infinite-time assertion; the proof's exact log-ratio recursion, absorbing mass interval, and strict multiplier bound do so.

The inequality \((1-c)e^{h-1}<2\) is sufficient and unproved to be necessary. The convergence rate is permitted to depend on the initial condition. No independent audit has been performed.
