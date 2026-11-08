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

# Reproducibility

The accompanying `verify.py` is a standalone Python 3 script requiring NumPy. Run `python verify.py` in the directory containing the extracted files. It performs 283 supplementary finite checks.

It implements the weights both from Fourier alias blocks and from a direct Gram-system solve, compares the density Fourier coefficients against fine-grid numerical integration, tests representative parameter families, and confirms the large-parameter negative-weight obstruction on fixed even grids. These checks do not quantify floating-point rounding rigorously or prove the universal asymptotics. The analytic proof, including the alias-tail estimates and the zero-neighborhood count, is in `RESULT.md`.

The mathematical statement is valid for each fixed higher-order parameter and fixed positive kernel scale. No claim is made for the full multidimensional lattice or for the subsampled method. Independent mathematical audit has not been performed.
