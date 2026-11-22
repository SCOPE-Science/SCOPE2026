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

The complete analytic proof in RESULT.md establishes all quantified claims. A finite independent diagnostic checker `verify_width.py` runs on Python 3 with NumPy and SciPy:

```
python verify_width.py
```

It completed with `WIDTH_DIAGNOSTICS_PASSED 1071`. It compares the exact support-maximum calculation against the closed width formula at randomly chosen directions, checks all four minima, integrates exact unexpanded angular width sublevel sets against the predicted fixed-separation and crossover coefficients, and independently evaluates the crossover domain area numerically. These are deterministic numerical tests, not exhaustive proof of the limiting asymptotics or historical novelty. The analytic proof relies on an exact support expression, a local uniform Taylor expansion, compactness of rescaled sublevel sets, and integration of a bounded limiting domain. No independent external audit has been performed.
