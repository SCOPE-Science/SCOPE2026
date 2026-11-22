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

Run `python verify.py` with Python 3 and mpmath. In the evaluated environment, the checker returned `VERIFY_OK 113 checks A= 0.0445757926701356342`.

It independently reconstructs a truncated Fourier series for the kernel and its mean and checks the Bernoulli closed form, mean at zero, and high-precision Gram solves at seven resolutions. It verifies finite-resolution trends for the two- and three-site weights and leading noise coefficients. All numerical checks have explicit absolute tolerances to account for Fourier truncation, and are not used as proof of an infinite limit.

The actual proof uses analytically exact Fourier identities and the leading Taylor orders of a two-by-two Gram subsystem determinant; in particular the denominator is `8*k0*a*h**3+O(h**4)`, while the numerator is `(k0*b2/2+a*b0)*h**2+O(h**3)`. The variance conclusion further requires independent, centered, equal finite-variance observation errors.

No physical hardware performance, randomized subset probability, high-dimensional conclusion, or independently audited scientific certificate is asserted.
