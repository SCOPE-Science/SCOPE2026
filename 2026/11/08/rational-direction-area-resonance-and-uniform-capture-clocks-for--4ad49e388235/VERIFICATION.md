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

The universal proof is in `RESULT.md`. Exact rational replay: run `python3 checker.py` without external packages. The script partitions the phase circle at all translated barrier endpoints, selects an exact rational midpoint of every stratum, and checks that the phase orbit and sheet-label dynamics reproduce the predicted periodic-sheet count, first-coalescence time, and rational-grid area. It tests reduced positive rational slopes, translated barrier intervals, both overlap regimes, and denominators at most \(18\). Actual output:

```
PASS: 2444 rational-angle/barrier tests; 57908 exact phase strata
Validated rational phase classification, finite-time coalescence, area law, and uniform hitting clocks in non-overlap regime.
```

Finite checks are not a universal certificate; the exact proof relies on coalescence of two sheet trajectories and the order-\(q\) circle rotation. The tested script does not certify any irrational-direction assertion: that comparison is cited to the primary source. Endpoints and nonhorizontal time normalizations are outside the classification where indicated.
