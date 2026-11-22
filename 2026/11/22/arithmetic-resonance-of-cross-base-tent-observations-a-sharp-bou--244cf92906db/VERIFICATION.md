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

# Reproducibility and scope

Run `python3 tent_cross_cov_check.py`. All 784 exact rational comparisons over ordered pairs of dilation integers from 1 to 28 were successful. The standard-library checker also prints finite Birkhoff-sum covariance examples, which agree with the convergence patterns. Formula (1) for all integer dilations is established by a convergent Fourier identity, and the infinite time-sum dichotomy is established by prime-exponent norm estimates and an exact lattice-point count. Finite enumeration is not an exhaustive proof of these infinite statements.

No external independent audit has been performed.
