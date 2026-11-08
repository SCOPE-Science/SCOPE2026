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

## Actual reproducibility checks

`python verify_p4.py` with Python 3 and SymPy returned `VERIFY_OK 196` after the final proof formulas were established. The script verifies general-weight Green entries by exact matrix inverse, the four positive rational response entries on the tuned ray, signs and row sums at positive rational steps, the uniform counterexample, and sampled exact Green-sign implications. The independent mathematical audit has not been performed. The continuum claim and eventual negativity rely on the proved rational factorization and spectral asymptotic, not on finite checks.
