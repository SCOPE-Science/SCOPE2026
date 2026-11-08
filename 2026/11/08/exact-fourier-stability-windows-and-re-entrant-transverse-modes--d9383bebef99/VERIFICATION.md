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
The theorem is established by block diagonalization of the real-space Jacobian and strict Schur inequalities for the mode characteristic polynomial. The boundary checks are algebraic, not inferred from samples.

Run `python verify_modes.py` from the same directory, with Python 3 standard library; expected stdout is `VERIFY_OK mode_samples=29804 finite_difference_modes=4 exact_window=(16/27,62/63)`.

The test calculates quadratic roots independently of the Schur interval, includes modes from periodic lattices with differing dimensions and diffusion strengths, and compares centered derivatives of the *nonlinear* spatial update to analytic Fourier blocks for four wave numbers. The tests are finite, and all nonhyperbolic boundaries remain outside claims of nonlinear attraction or repulsion. No external verification was conducted.
