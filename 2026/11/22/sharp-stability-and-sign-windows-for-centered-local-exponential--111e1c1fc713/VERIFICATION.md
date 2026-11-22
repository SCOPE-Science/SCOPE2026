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

# Reproducibility and bounds

Run `python verify.py` in an environment with Python 3, SymPy, and NumPy. The script has no inputs and reconstructs the local second-differentiation matrices on equally spaced dimensionless nodes. It uses exact symbolic matrix powers and Lagrange polynomial derivatives to check the displayed convolution coefficients, row-sum identities, Fourier symbols, seven-point derivative factorization, algebraic stability root and endpoint positivity identities. It separately compares circulant eigenvalues to Fourier symbols at several rational parameters; those latter computations are finite floating-point diagnostics only.

The executed packaged script returned `VERIFY_OK 90 algebraic and matrix checks; seven-point spectral root 0.841360228011148`. Direct floating-point matrix-exponential comparisons on the five- and seven-node local matrices at diffusion ratios \(0.1\), \(0.25\), \(0.5\), and \(0.8\) agreed with the exact polynomial weights at around machine precision.

**Proved limits.** The analytic coefficient identities and sign arguments hold for all the quantified step ratios and stencil sizes. The exact \(\ell^2\) threshold is uniform over all admissible periodic grid sizes. For a fixed odd periodic grid, the set of Fourier frequencies is smaller and a larger contraction interval may result. The general higher-order theorem proves only short- and long-step positivity failure; it does not classify intermediate timesteps. The findings do not establish nonlinear, nonuniform, or nonperiodic positivity.

No external independent audit has been performed.
