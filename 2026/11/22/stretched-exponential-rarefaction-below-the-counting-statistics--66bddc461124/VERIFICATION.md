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

The proof uses exact image-kernel integrals and standard Chernoff and Gaussian-tail inequalities; the theorem is not dependent on a numerical certificate. Execute `python verify.py` with NumPy and SciPy installed to evaluate the exact finite-population equilibrium-age mixture numerically and contrast it with the stated asymptotic exponent for a sequence of population sizes. The numerical routine is deterministic. The integral truncation and quadrature discretization introduce numerical error, so the output is used only as an independent consistency check.

The mathematical domain requires integer population greater than two, positive diffusion and reset threshold, fixed positive central-interval scale, and a fixed fraction strictly below the known limiting lower support edge. It does not cover the shrinking-distance-to-edge crossover or a multiplicative probability prefactor. Independent audit has not been performed.
