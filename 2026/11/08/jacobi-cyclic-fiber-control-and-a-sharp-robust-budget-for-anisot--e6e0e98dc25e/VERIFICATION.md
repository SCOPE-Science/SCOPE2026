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

The reproducibility program is `verify.py`. Run `python verify.py` from the directory containing this document; it requires only the Python standard library.

Exact rational Gaussian elimination of the Kalman matrices passed for \(n=3,4,5\) on square grids at four positive couplings each, with boundary sets of size \(n-1\), and rejected the \(n-2\) boundary set at isotropic coupling. It also passed for products involving the weighted triangle with spectrum \(\{0,3,5\}\), and for a nonuniform weighted path factor. Actual execution output: `VERIFY_OK exact_fraction_cases= 25`.

The general theorem is proved by an exact polynomial Vandermonde determinant, not by extrapolating the finite tests. The proof covers all factor sizes and all positive couplings under the cyclic-root and Jacobi hypotheses. No external independent validation has been performed.
