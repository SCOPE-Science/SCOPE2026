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

# Reproduction

Run `python verify_exact.py` and `python verify_numeric.py` from this directory. No network access or external input file is used. Both programs were executed on the present contents.

`verify_exact.py` constructs the ten-dimensional full Gram determinant in the original monomial coordinates with rational arithmetic, for a three-dimensional ball and half-width \(1/2\), and checks exact factorization against the claimed sectors.

`verify_numeric.py` tests 24 complete monomial Gram spectra, dimensions \(2,3,4,5,8,10\), slab half-widths \(0.07,0.23,0.51,0.8\), against a separately evaluated reduced beta-block expression. Its absolute threshold is \(2\times10^{-10}\). It additionally checks the thin-width constant using 80-digit arithmetic for dimensions \(2,3,8\).

The symbolic, quadrature and high-precision checks all passed. The infinite families in the claim rest on the analytic conditional-moment, stochastic-order, and determinant proof, not on finite numerical evidence. This is not an independent audit.
