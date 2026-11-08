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
Direct exhaustive computation over the complete rank-stratified isotone monoid was run through n=6. The script constructs all functions and checks both sandwich equations, then separately computes the kernel-block and image-gap degree product. It also tests power moments k=0,1,2,3 via the generating polynomial coefficient expressions and verifies the sharp minima and maxima. A fixed-seed 5,000-sample computation at n=120,r=60 checks numerical behavior compatible with the logarithmic Gaussian limit; it is only a diagnostic.

Reproduce using `python3 CHECK_DEGREE.py`. Expected terminal markers: `DEGREE_VERIFY_OK` and `ASYMPTOTIC_DIAGNOSTIC_OK`. The proof of the infinite-dimensional-index statement uses a conditional Fourier/local-limit argument independent of the finite checks.
