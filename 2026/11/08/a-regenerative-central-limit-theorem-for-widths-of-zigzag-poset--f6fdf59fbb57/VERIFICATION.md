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

# Reproducibility and verification

Execute `python check.py` with Python 3 and NumPy/SciPy in the same directory. The checker enumerates every independent-set vertex of path graphs through ten vertices and compares the resulting maximum with the dynamic recursion on seeded Gaussian samples. It separately tests the coordinate-complement order/chain isometry on all binary patterns through eight vertices, uses a positive quadrature scheme to approximate the stationary fixed-point distribution, simulates 16,000 spherical widths in 512 dimensions, and numerically checks the exact Gaussian Stein covariance identity.

The successfully executed checker emitted:

`ZIGZAG_WIDTH_CHECKS_PASSED c= 0.307510818 n= 512 sample_width_mean= 13.928111 sample_width_var= 0.062792 gaussian_stein_ratio= 0.9976`

This marker is a reproducibility observation, not an external proof certificate. The theorem's infinite-dimensional statements depend on the explicit stationary coupling, finite-mean regeneration, Gaussian integration by parts and deterministic radial-variance identity given in RESULT.md. The approximate variance \(0.0627\) was explored by Monte Carlo; it is not a rigorously enclosed constant. Independent audit has not been performed.
