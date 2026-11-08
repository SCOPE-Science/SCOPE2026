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

# Reproducible verification

The claim is proved in `RESULT.md`, including the exact column-weight identity, the rare-pair Poisson limit, singleton Gaussian limit, and the bounded finite-core tilt. This report concerns only direct reproducibility checks.

Execute `python3 verify.py` from the directory containing the delivered files. The script enumerates exact rational configurations for \(K_{3,n}\) for \(n\in\{1,2,3\}\) and \(q\in\{2,3/2,3/4\}\), comparing the original FK partition and rooted connectivity weights against the independent-column representation. It separately checks the limiting triangle FK conditional laws for four cluster weights and three intensities.

Observed local result:

```
PASS: 66 assertions, exact finite-state partition/connectivity and limiting triangle tests
```

This is not a computer-assisted proof for arbitrary \(n\): the all-size conclusion depends on the analytic probabilistic argument in `RESULT.md`. The high-order multi-hub and nonfixed-parameter regimes are not covered.
