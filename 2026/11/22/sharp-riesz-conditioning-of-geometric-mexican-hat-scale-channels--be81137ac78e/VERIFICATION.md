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

# Verification of the Gaussian heat-derivative scale theorem

The theorem is self-contained modulo classical integral/Fourier identities, the Euler–Weierstrass Gamma product, the Jacobi triple product and Stirling's formula, all explicitly specialized in `RESULT.md`. The normalized Gram coefficient follows from polar Fourier integration with \(\widehat{\Delta H_t}(\xi)=-|\xi|^2e^{-t|\xi|^2}\) and \(\nu=(d+4)/2\). Poisson summation gives a positive Gamma-modulus periodization. The Gamma product yields a positive mixture of wrapped Gaussians; the Jacobi triple product gives strict decrease on the half-period, establishing the global extrema, not merely sampled values. Circular spectral convolution proves strict improvement with dimension, and two nearest Gamma aliases at frequency \(\pi\) determine the sharp dense-scale leading coefficient.

Run the standalone checker using `python CHECK.py` with NumPy and SciPy installed. In the packaging review it printed `PASS: 442 supplementary numerical assertions`. It compared exact overlap series to the Gamma symbol, checked many spectral monotonicity and dimension monotonicity samples, tested finite Toeplitz eigenvalues against the infinite sharp endpoints and verified small-spacing constant ratios. None of these finite tests certifies infinite extrema or asymptotics; their proofs are in `RESULT.md`.

The assertion applies only to positive spatial dimension, positive logarithmic spacing and unshifted normalized heat-Laplacian scale channels. Independent mathematical audit and external reproducibility assessment have not been performed.
