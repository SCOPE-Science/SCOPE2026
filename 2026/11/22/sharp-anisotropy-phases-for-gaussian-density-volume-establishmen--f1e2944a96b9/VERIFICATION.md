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

## Reproduction
Run `python verify_gaussian_footprint.py` using Python with NumPy and SciPy. The deterministic checker enumerates finite spectral-vertex candidates for dimension 2 through 9, compares the resulting determinant bound against randomly generated admissible covariance spectra, reoptimizes the one-dimensional exact founder requirement with `scipy.optimize.minimize_scalar`, and confirms that threshold inversion gives the required ellipsoidal volume. The original replay returned `CHECKS 24692`, with no exception.

Illustrative parameters: dimension 2, trace 2, condition-number ceiling 9, local density cutoff 1, and required volume \(\pi\). The checker returns optimal determinant square root 0.6, founder mass 8.674474745899, isotropic mass 10.359221263698, and fractional reduction 0.162632545. The covariance eigenvalues are 0.2 and 1.8.

## Analytical verification and boundaries
The proof is independently reconstructible from the Gaussian superlevel ellipsoid, the full feasible spectral trace polytope, and a single sign-changing derivative. Numerical tests are **supplementary** finite consistency checks, not an infinite proof. In particular, they cannot certify the absence of stronger published results. This work does **not** establish long-term ecological persistence, field calibration, or an actual risk reduction for any managed population.
