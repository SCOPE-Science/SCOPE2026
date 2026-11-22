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

# Reproducibility and verified limits

Run `python check_isotope.py` with Python 3, SymPy, and SciPy installed. The script checks the harmonic inverse discriminant and determinant symbolically, exactly recomputes 513 rational examples, checks a specified explicit example, and numerically solves 24 nonharmonic instances. Observed output:

```text
ISOTOPIC_THREE_TISSUE_OK assertions=540 symbolic=2 rational=513 nonlinear_numeric=24
```

This checker is diagnostic: a finite parameter sample or an optimization success cannot prove an all-rate theorem. The complete-domain uniqueness and two-sensor nonidentifiability arguments are in the proof of `RESULT.md`. No independent mathematical audit or experimental isotope validation has been performed.
