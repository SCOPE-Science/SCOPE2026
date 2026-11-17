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

# Reproducibility

Run `python3 theta_allperiod_check.py` using Python 3 standard library only. The program constructs labelled simple theta graphs independently for phase-weight enumeration and full bounded-state chip-firing checks, compares both outputs against the claimed exact formula, and prints a success marker. It tests 35 phase instances and 32 independent microscopic instances, encompassing 868,608 bounded microscopic configurations.

The bounded microscopic state range is sufficient for period-\(p\) states with exactly one firing per vertex because a vertex is below degree at some time and gains at most its degree in one update, implying a universal height bound of twice its degree minus one. Finite experiments provide reproducibility checks, not proof of all parameters. Mathematical generality is provided by the functional-orientation argument in RESULT.md.

No independent audit has been performed.
