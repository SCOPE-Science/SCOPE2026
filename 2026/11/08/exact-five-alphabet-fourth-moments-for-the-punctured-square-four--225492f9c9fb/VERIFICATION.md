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

# Reproducibility

Use `python3 checker.py` with `optimizer_catalog.json` present in the same directory. All 12,200 normalized eight-coefficient arrays are examined. The two moment implementations compare displacement autocorrelations with independent ordered-pair convolution coefficients for every array. For roots of orders 2, 3, 4, and 6 the arithmetic is exact Gaussian or Eisenstein arithmetic; for fifth roots the value lies in the ordered real quadratic field \(\mathbb Q(\sqrt5)\), compared by exact sign tests. The output concludes `HOLLOW_SQUARE_FOURTH_MOMENT_PASS checked=12200 direct_vs_convolution=all`.

The exhaustive certificate is valid for the five stated discrete phase alphabets only. Continuous-phase and higher-alphabet optimization is not certified. The verified finite-support transfer to rectangular Fourier grids requires both cyclic orders at least five.
