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

The proof is analytical. The package's `verify.py` checks the finite beta law using exact binomial sums, the survival-product identities, direct Gaussian QR simulations of the stated algorithm, and finite-dimensional moderate-deviation numerical evaluations. Python 3, NumPy and SciPy are required. Execute `python verify.py` from the directory containing this file. These independent numerical computations do not establish the limiting result without the mathematical argument in RESULT.md.

Limits: the code samples only specified finite ranks and uses a seeded pseudorandom generator; the actual theorem's almost-sure rank increments and limiting claim are proved, not empirically certified. No external independent mathematical audit has been conducted.
