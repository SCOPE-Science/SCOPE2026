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

The complete analytic proof appears in `RESULT.md`. The standalone `verify.py` uses NumPy and SciPy linear programming to check two logically separate conditions for a finite collection of ordered planar unit-normal configurations. For each omitted inequality it minimizes its linear functional subject to the reduced inequalities and bounded coordinates; an optimum not below zero tests joint implication. For each retained inequality it instead omits that one condition and obtains a strictly negative optimum, testing irredundancy.

Executed with `python verify.py`. The observed output was:

```
PASS: 378 normal configurations; 15514 independent bounded LPs; 4748 nonredundancy witnesses; 10766 simultaneous implication checks
```

The suite includes regular arrangements, exact opposing/semicircular arrangements, nonuniform manually prescribed arrays, and fixed-seed random samples for \(3\le N\le10\). Tests use floating-point numerical tolerances and do not establish the theorem for infinitely many normal directions. A symbolic proof gives the unrestricted statements, including boundary equality, lineality and actual facets. No independent audit was performed.
