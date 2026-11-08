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

# Verification
The standalone `verify.py` script uses Python's standard library. Its direct orbit and independent running-minimum expressions agree across 1680 finite cases for two irrational rotations, three forcings (including the critical value), four initial phases, seven initial deviations and ten iteration counts. It separately constructs 18 angular covering-radius witnesses and compares those with the critical finite-time maximum.

Run `python verify.py`. Observed output:

`VERIFY_OK exact_running_min_cases=1680 covering_radius_cases=18 critical_rotations=2 source_slope=-1`

The exact cohomological identity, scalar minimum recurrence, phase-density limit, and both continued-fraction implications must be checked algebraically as in `RESULT.md`. This numerical script does not prove irrational equidistribution, convergence for all initial conditions, the Diophantine dichotomy, or historical originality. Independent audit is not performed.
