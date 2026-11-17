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

# Verification of the octagonal conic-spline modulus

The exact proof is given in `RESULT.md`. To reproduce its independent finite-rational checks, run `python3 CHECKER.py`. The program uses only Python's standard library and exact `fractions.Fraction` arithmetic. It computes convex hulls directly from the radial vertices, intersects every hull edge with each prescribed ray and compares the resulting radial maxima against the twelve-expression closed form.

On the current package, the checker returned:

```
PASS: octagonal exact-rational hull comparisons: 4096
PASS: twelve individually essential ratio branches: 12
PASS: independent six-ray control comparisons: 1728
```

The first test ranges over \((a,b,c,d)\in\{1,\ldots,8\}^4\). The second tests each listed witness against every competing ratio, including the constant \(1\). The third tests all \((a,b,c)\in\{1,\ldots,12\}^3\) for a separate six-ray fan. Each comparison is exact rational arithmetic without rounding or tolerances.

These finite computations are not a certificate for every positive real parameter. The universal result follows from the planar supporting-segment argument, the exact conic interpolation, the complete crossing-pair table, and the strict rational witness substitutions in `RESULT.md`. No external or independent mathematical review was performed.
