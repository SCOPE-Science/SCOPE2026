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
# Verification

The explicit kernel numerator formulas were independently reconstructed from Beta monomial moments. Analytic root counting uses coefficient signs, a cubic discriminant and Vieta's product formula, with exact endpoint substitutions. The checks include all real parameters analytically; finite code is only a corroborating arithmetic test.

Reproduce using Python 3 standard library:

`python jacobi_kernel_check.py`

Observed output:

`JACOBI_BERGMAN_KERNEL_PASS exact=432 root_and_threshold=59`

The script checks 432 exact rational coefficient/endpoint assertions and 59 numerical root/threshold assertions. It does not certify uncountably many parameters. No independent mathematical audit has been performed.
