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

# Reproduction

Use Python 3, without third-party packages:

```
python3 CONSTRUCTION_CHECK.py
```

The expected output is:

```
PASS: 60438 direct constructive cases, 16900 independent determinant coefficients, two certified lower bounds
```

The finite test ranges are \(3\le M,N\le25\) for the explicit per-site construction and \(3\le M,N\le15\) for independently evaluated signed-detector coefficients. All positive and boundary slopes in the stated ranges are checked, including their physical line counts and whole-torus permutation property. The polynomial comparison uses Newton identities and an exact integer recurrence, not floating-point determinants. Both lower bounds are independently compared to the resulting exact coefficients.

The all-size proof is the modular residue predecessor argument in `RESULT.md`. Finite checks alone cannot establish the infinite family. The quadratic-period range and exact arithmetic do not imply external validation, which has not been performed.
