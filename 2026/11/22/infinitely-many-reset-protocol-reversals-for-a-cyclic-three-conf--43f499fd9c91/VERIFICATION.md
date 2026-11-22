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
# Verification and reproducibility

The companion standalone `verify.py` requires Python 3, NumPy, and SciPy. Run it from the directory containing this file using `python verify.py`. It checks the exact formulas against two separate mathematical representations: (1) a real matrix-square-root solution of the coupled backward equations with phase-specific boundary conditions, and (2) an independent spatial finite-difference solution with separate reset operators. It reports 1,221 passing assertions and prints finite-difference comparisons at distances one and five for unit diffusion, switching and reset rates.

All analytic claims about infinitely many crossings are proved from the derived exact cosine, its nonzero amplitude, and its strictly positive spatial frequency. Spatial discretization does not constitute an infinite-distance proof. The matrix tests are numerical consistency checks, not independent formal certification. The stated theorem requires all rates and the initial/reset distance strictly positive; it does not address finite-sample inference or classify more general gates.
