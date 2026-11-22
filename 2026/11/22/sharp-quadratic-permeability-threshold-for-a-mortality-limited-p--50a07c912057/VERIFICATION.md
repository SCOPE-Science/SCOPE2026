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

# Verification and limits

The analytic proof is in `RESULT.md`. To replay its auxiliary tests, execute `python3 verify_corridor.py` with Python 3; the script uses only the standard library. It computes exact rational solutions of killed Dirichlet systems, rechecks the gateway identity on a finite parameter grid, verifies the explicit reflecting-path formula and adverse example, and compares numerical roots against the analytic critical-rate asymptotic. A successful run reports 380 checks. All infinity-size, universal-parameter and strict-monotonicity claims rest on the explicit argument, **not** finite sampling.

The independent audit has not been performed. The ecology model omits calibration, heterogeneous death and transient behavioral effects. Bibliographic comparisons cannot certify historical priority.
