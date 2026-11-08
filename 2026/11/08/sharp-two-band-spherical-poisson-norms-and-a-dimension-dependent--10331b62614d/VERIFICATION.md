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

# Reproduction and limits

The standalone Python 3 program `scripts/check_spherical_two_band.py` requires no external modules. Execute it from the package root using `python3 scripts/check_spherical_two_band.py`. It evaluates exact rational even moments of the first spherical coordinate through degree eight, the corresponding first and second zonal harmonic moments, and the claimed norm formulas in 138 rational sample cases. It also checks dimension monotonicity in a finite test range and rigorous rational brackets for three contractivity radii and the Gaussian limit.

Expected terminal line: `ALL_TWO_BAND_SPHERICAL_POISSON_CHECKS_PASSED`.

The proof of the universal parameter and dimension statements is analytical and appears in `RESULT.md`; neither the script nor the numerical root approximations constitute exhaustive infinite-dimensional certification. No independent audit has been performed. The signed mixed terms in the fourth-moment expansion vanish by antipodal symmetry, while the surviving mixed term is nonnegative, an important normalization check.
