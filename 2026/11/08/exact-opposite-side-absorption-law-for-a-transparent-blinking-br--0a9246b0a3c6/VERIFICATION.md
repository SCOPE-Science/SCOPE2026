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

# Reproducibility and verified scope

Extract `verify_splitting.py` and run it with Python 3 and installed NumPy, SymPy and SciPy. The complete run printed:

```
symbolic: 12 exact identities verified
numerical: 714 finite-grid numerical comparisons, inequalities and monotonicity steps verified
All reproducibility checks passed; continuous assertions follow from proof.
```

The checks cover the matching constants and endpoint formulas, derivatives of the monotonicity factor, convergence of a separately formulated two-half-line finite-difference system, and substantial positive-parameter grids. The exact mathematical proof is in `RESULT.md`; this finite program does not certify all real parameters and does not establish publication priority. No external independent mathematical audit has been performed. The underlying continuous-time model should not be replaced by discrete Euler crossing conventions without separate analysis.
