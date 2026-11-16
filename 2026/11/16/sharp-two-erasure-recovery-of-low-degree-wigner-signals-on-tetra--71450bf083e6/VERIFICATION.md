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

# Reproducibility and verification

Run `python3 tetra_wigner_check.py` using a standard Python installation. This file has no third-party dependencies.

Actual output from replay:

```
PASS: 12 tetrahedral rotations, exact rank 10 projector
PASS: all 66 double-erasure patterns: 18 singular, 48 invertible
PASS: singular spectra [0, 1/3, 1 x8] or [1/12, 1/4, 1 x8]
PASS: one-deletion spectrum [1/6, 1 x9]
PASS: all 36 ordered half-turn witness pairs by explicit trace formula
```

The code uses exact rational arithmetic throughout. It enumerates the even permutations of four vertices, checks the three-dimensional character, exact projector multiplication, ranks by trace, each pair's relative rotation order, and every half-turn invisible witness, including an explicit continuous trace-formula realization. The full analytical proof is in `RESULT.md`; the enumerator is a finite cross-check, not a replacement for its exact group-theoretic deductions. No claim of independent validation is made.
