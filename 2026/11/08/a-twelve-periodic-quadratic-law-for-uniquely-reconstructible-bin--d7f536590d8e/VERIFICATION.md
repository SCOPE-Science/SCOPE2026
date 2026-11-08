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

## Exact checks
Run `python3 verify.py` in this directory. The script regenerates and verifies all 166 reachable states and both bit transitions, checks the integer row vectors at lengths 9, 21, 33 and 45 against the embedded certificate, and verifies their exact coordinatewise recurrence relation. It checks all finite base values and additional lengths up to 65. `python3 independent.py` separately enumerates every binary word of lengths 3 through 16 and compares trigram-profile fiber multiplicities to the closed formula.

The unbounded proof uses the matrix-vector identity, not empirical agreement for finitely many lengths. No external independent review has been performed. A closely related source was accessible in abstract only, leaving historical-priority uncertainty.
