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

From the package root run `python artifacts/verify.py` with Python 3 and NumPy. The script checks binomial identities and the two characteristic-polynomial sign identities using exact rational arithmetic for 3645 triples, then reconstructs the actual complex Fourier-character matrices on 16 finite examples. It prints `QARY_BALL_FIRST_BAND_VERIFY_OK 3645 16` only if all assertions succeed.

The general proof is mathematical: product-symmetry decomposition, conditional binomial moments, exact two-by-two characteristic polynomial, separate injectivity arguments for the ball and its complement, and fixed-alphabet central/local binomial limit theorems. Direct numerical Fourier eigenvalue comparisons are finite corroboration, not an all-dimensional certificate. The Gaussian limit is pointwise for fixed finite central-limit coordinate and fixed alphabet size; no uniform-in-alphabet error control is claimed.

An independent external mathematical audit was not performed.
