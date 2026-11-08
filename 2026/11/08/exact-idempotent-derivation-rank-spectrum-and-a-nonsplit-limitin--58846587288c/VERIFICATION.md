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

# Reproducibility checks

Execute `python verify.py` from the directory containing this file and `verify.py` (Python 3, standard library only). The script exhaustively enumerates scalar-normalized \(n\times n\) generators for \((n,q)=(2,2),(3,2),(4,2),(2,4)\), directly evaluates the induced adjoint maps and their squares on all matrix units, and compares exact rank histograms to the closed formula. The run produced:

```text
EXHAUSTIVE_OK 2 2 {0: 1, 2: 4}
EXHAUSTIVE_OK 3 2 {0: 1, 4: 28}
EXHAUSTIVE_OK 4 2 {0: 1, 6: 120, 8: 336}
EXHAUSTIVE_OK 2 4 {0: 1, 2: 16}
VERIFY_OK
```

The code does not check every matrix size or every field. The general proof uses matrix-unit innerness, quadratic generators, centralizer calculations and a dominated-convergence argument as detailed in `RESULT.md`. The numerical asymptotic examples can be recomputed from the infinite products and absolutely convergent theta series. No independent mathematical audit or external certificate has been performed.
