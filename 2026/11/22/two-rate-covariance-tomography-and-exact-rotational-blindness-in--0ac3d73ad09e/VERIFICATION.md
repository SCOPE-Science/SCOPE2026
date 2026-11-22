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

The scalar and matrix identities are established analytically in RESULT.md. For reproducible supplemental checks, run `python checker.py` with Python 3 and SymPy. The exact-rational program solves the symmetric matrix Lyapunov equations at two reset rates, reconstructs the inverse when the measured sensitivity is nonzero, checks the strict covariance ordering, and verifies all-rate observational blindness on explicit families. It passed 144 exact-rational scenarios in the development run, including equal and unequal bath diffusivities.

The proof uses the positivity of the integral covariance kernel, one complete skew-matrix parameterization, the diagonal-diffusion constraint, and uniqueness of the stable Lyapunov solution. The all-rate result uses a closed-form unreset Gaussian covariance and the exponential age mixture. These steps are not inferred from finite experiments. Numerical robustness, finite-time convergence of physical measurements, and independent mathematical assessment were not tested.
