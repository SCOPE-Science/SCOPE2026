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

# Exact checks and limits

The files `states.json` (120 explicit records) and `verify.py` (Python 3 standard library only) reproduce the complete finite-state certificate. Execute `python3 verify.py` from any directory; it locates the table beside the script.

The checker verifies 120 distinct and reachable records, the seed, both transitions at every state (240 exact integer edges), the histogram of coordinate spreads `0:10, 1:100, 2:10`, and 31 distinct first coordinates. Because both transformations preserve the finite set and every integer index descends by binary division to the seed, closure proves the unrestricted theorem without an index cutoff.

The separate direct polynomial recurrence check examines all indices from 0 through 12000, asserts five-class discrepancy at most two, and checks the exact polynomial and sharp vector at index ten. That secondary numerical check is corroborating evidence, not the proof of the infinite statement.

Expected successful output:

```
EXACT_120_STATE_CLOSURE_AND_REACHABILITY_PASS 120
ALL_240_TRANSITIONS_CLOSED_PASS
FIFTH_RESIDUE_SPREAD_HISTOGRAM_PASS {0: 10, 1: 100, 2: 10}
INDEPENDENT_COEFFICIENT_RECURSION_PASS 12001
SHARPNESS_AT_TEN_PASS
VERIFY_OK
```

The mathematical proof also uses a previously published hyperbinary/fence ideal correspondence; this verifier does not independently derive that literature result. The bounds do not classify all equality indices or assert behavior for other moduli. Self-review was completed, with historical-priority uncertainty recorded; independent external validation was not performed.
