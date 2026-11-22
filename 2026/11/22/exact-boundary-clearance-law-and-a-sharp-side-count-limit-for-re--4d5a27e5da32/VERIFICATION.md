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

# Reproducible scientific verification

The independent computational check `checks/regular_ideal_clearance.py` uses Python 3 with SciPy, and was run after copy into the packaged file path. It returned `ALL_CHECKS_PASSED 810`. Tests integrate the actual hyperbolic polar area independently of the Fermi/coarea derivation, check density normalization at seven side counts, the CDF and support at five interior fractions, the unique density crossing, the exact total variation formula by numerical integration, strict CDF order on a finite grid, and upper-endpoint and high-side-count asymptotic coefficients.

Analytic verification is supplied in `RESULT.md`: right-triangle/facet normal formulas, coarea and antiderivative, strict derivative sign, unique density crossing, exact TV and endpoint expansions. Finite numerical checks cannot establish infinite quantification, uniqueness of priority, or independent audit. Source comparisons are limited to identified relevant accessible material; any previously unlocated stronger formula is a historical priority risk.
