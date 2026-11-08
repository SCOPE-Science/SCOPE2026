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

# Verification record

Exact geometric derivation and endpoint analysis appear in `RESULT.md`. All computations use the standalone program `check_spheroid_cusp.py` from this package, not a cached or external script. Execute with Python 3, NumPy and SciPy.

The checker sampled 130,000 invariant hitting planes for each aspect ratio \(r=1.3,2,4\), cross-checked direct quadratic-form ellipse area against the closed geometric formula, and compared Monte Carlo survival at five thresholds per aspect ratio against independent numerical integration. It verified the exact first moment, compared the PDF to a finite difference of the survival function, and checked monotone convergence of the left-cusp normalized deficit to the analytic coefficient. The final stdout marker was `PROLATE_CROFTON_SECTION_AREA_CUSP_OK`.

Sampling, numerical quadrature, and code checks do not establish universal correctness, exact analyticity, or historical novelty. Those are addressed respectively by the displayed proof and the separate literature comparison; no external independent mathematical audit has been performed.
