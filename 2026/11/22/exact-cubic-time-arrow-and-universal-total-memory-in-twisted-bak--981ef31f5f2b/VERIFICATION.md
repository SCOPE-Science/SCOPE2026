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

# Reproducibility and limits

Execute `python3 CHECK.py` in the same directory as this file. The code uses Python 3 standard library `fractions` only and directly calculates the transfer on centered quadratic and affine functions in dimensions 2 through 14. It checks 637 exact rational coefficient and identity comparisons, the first non-universal wrap correction, and the integrated \(-2/9\) value.

The general proof resides in `RESULT.md`. Finite exact tests corroborate the algebra but cannot prove the statement for arbitrary dimension or all time lags. Scientific originality is assessed from the literature listed in `RESULT.md`; independent mathematical audit has not been performed.
