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

# Reproducible finite diagnostics

Execute `python verify_cycle.py` from this package with Python 3, NumPy and SciPy installed. The diagnostic independently constructs the signed matrix, inverts rational matrices with exact fraction arithmetic, and checks the continuant determinant, Sherman--Morrison endpoint formula, strict resolvent endpoint ordering, spectral root existence, zero row sums, and endpoint fractional-power maximality for tested lengths/strengths.

The observed result from the actual supplied script was:

```
VERIFICATION_OK rational=1548 spectral=4761 total=6309
```

The exact arithmetic covers integers 3--8 and selected rational shifts/edge strengths. The independent spectral checks cover sizes 3, 4, 5, 8, 12 and 20 at normalized negative strengths 0.1, 0.5 and 0.9. The three-vertex case is a diagnostic only and not included in the new theorem. These finite tests do **not** establish the infinite collection of all sizes, strengths and fractional exponents; the mathematical proof in `RESULT.md` does.

The first public date is taken from the arXiv v1 posting on 2020-09-08, not from a revision or journal issue. The numerical calculator does not provide independent validation of originality.
