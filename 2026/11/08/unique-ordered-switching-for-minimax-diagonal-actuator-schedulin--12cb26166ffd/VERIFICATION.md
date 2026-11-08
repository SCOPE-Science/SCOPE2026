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

# Verification record

The exact Gramian formula, scalar equal-mass recursion, weighted-exponential upper envelope, global minimax inequality and optimizer uniqueness are proved in `RESULT.md` for all stated dimensions and continuous schedules. They do not depend on numerical enumeration.

Run `python3 verify.py` in this package, using only Python's standard library. The program independently computes monotone scalar bisections and compares interval masses across 60 systems with 2–6 coordinates, checks 401 dual-envelope points per system and evaluates alternative 75-bin one-active-actuator schedules. Actual recorded execution output was:

`VERIFY_OK 25620 equalized entries, dual-envelope optimality, random alternative schedules`

The samples provide bounded spot checks only; they are not an exhaustive search over all measurable schedules. An analytic strict upper-envelope inequality is the global certificate. The exact scalar bisection and limiting interpretation assume strictly ordered positive rates. Numerical examples are not interval-certified. No independent audit has been performed.
