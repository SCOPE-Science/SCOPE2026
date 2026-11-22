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

Analytical proof checks: verified conservation \(V+S_4+\sum O_t=12+z\); substituted the four-step recurrence for every permutation type; checked endpoint membership \(z=1\) (incompatibility) and \(z=2\) (compatibility); checked three-day optimizer values \(12\) and \(11+z\) in \(1\le z<2\); verified \(4\) full days are impossible as total inflow is at most \(15\).

Executable check: `python3 check.py`, Python standard library only, yields `PASS exact rational checks: 554`; exact fractions rather than floating-point tests. Fourteen parameter samples include both thresholds. Samples corroborate but do not prove all real \(z\) values.

Scientific limitations: no testing for other reservoir capacities, demand timing conventions, rainfall calendars longer than four days, or real hydrological calibration. Literature comparison remains provisional where historic full text was unavailable. No independent audit has been performed.
