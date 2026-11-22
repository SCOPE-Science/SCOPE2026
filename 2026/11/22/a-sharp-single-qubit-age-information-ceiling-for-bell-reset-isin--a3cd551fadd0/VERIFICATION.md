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

# Mathematical verification

The analytic proof in `RESULT.md` establishes the exact infinite reset-age sum and global optimization. The separate `verify.py` script evaluates the actual four-dimensional Ising unitary with the Bell reset state, partial traces the propagated states, and directly calculates the Holevo gap. It then compares this result with the reduced-state formula and the derived bound at thirty positive parameter sets, and checks twenty explicit equality cases.

Observed output:

```
PASS: 30 direct 4x4 matrix vs conditional-state comparisons, 20 exact optimizer cases
largest direct-matrix discrepancy 7.83484388477973e-13
p=0.1 sharp bound in bits 0.3051585985360449
limiting absolute cap in bits 0.31127812445913283
```

Finite numerical evaluations cannot prove an all-parameter inequality or global uniqueness; these conclusions follow from strict analytic inequalities in the proof. The matrix tests use convergent geometric-tail truncation and are diagnostics, not an external scientific audit. Requires Python with NumPy and SciPy; run `python verify.py` in the directory containing this file.
