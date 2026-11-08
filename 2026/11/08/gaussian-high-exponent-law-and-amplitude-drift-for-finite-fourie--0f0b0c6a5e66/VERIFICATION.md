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

Run `python artifacts/check_fourier_high_p.py` in an ordinary Python 3 environment; the checker uses only the standard library and no external paper, network service, or unbundled data. A successful local replay printed `FINITE_FOURIER_HIGH_P_CHECKS_PASS 216`. The checks compare exact finite Fourier convolutions with independent circular quadrature for even exponents and test the even-moment majorant for random complex coefficients. Numerical amplitude maximization for three fixed apertures and several even exponents is compared against the predicted frequency-variance drift and sharp norm asymptotic.

The universal claim is analytical, based on Parseval/convolution positivity, exact integer relation lattices, the strong peak geometry of positive frequency sums, uniform parameter-dependent Laplace asymptotics, and strict tangent concavity. Finite sampled exponents cannot prove all-exponent uniqueness, exclude other spectral profiles, or independently establish historical novelty.

Self-review: passed. Independent audit: not yet performed.
