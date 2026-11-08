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

# Reproducible mathematical checks

Run `python verify_two_tier_hardy.py` in the directory containing `requirements.txt` after installing NumPy, SciPy and SymPy. The executable performs eight exact symbolic secular-determinant factorizations, eight independent conforming finite-element low-eigenspectrum computations on the original unit-edge trees, and direct arithmetic tests of spectral collision/reconstruction.

Observed run output:

```
EXACT_SECULAR_DETERMINANTS_OK 8
INDEPENDENT_CONFORMING_FE_LOW_SPECTRUM_OK 8
BRANCH_PRODUCT_COLLISIONS_AND_TWO_VALUE_INVERSION_OK
ALL_TWO_TIER_HARDY_CHECKS_OK
```

The all-integer-parameter theorem is proved analytically in `RESULT.md` by exhaustively solving the Kirchhoff boundary-value equations below the terminal-edge threshold \(\pi/2\); the numerical and finite symbolic tests are only corroboration. No computation of the full infinite singular sequence or independent external audit is claimed.
