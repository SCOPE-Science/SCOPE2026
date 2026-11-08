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

# Verification of the mathematical claim

The proof uses the stationary age density, tensor-product state overlaps, an exact Fourier/binomial identity, dominated convergence on central-binomial ratios, Fourier Parseval, an equality condition for complex unit expectations, and a two-point interarrival approximation at fixed mean. No finite numerical experiment is used to infer an infinite theorem.

Reproduce finite diagnostics with `python3 verify.py` from the extracted package directory. The reference run reported `PASS 51 deterministic checks; no infinite proof inferred`. Tests include a deterministic-clock double integral independent of the Fourier sum, several full-period optimizer cases, exponential-clock Poisson coefficients, large finite populations, and explicit convergence of nonattaining two-point laws. Any finite numerical tolerances are diagnostic only. Analytical statements for every interarrival law and every population are established in `RESULT.md`.

Known limits: equilibrium renewal initialization is essential for lattice clocks; a hardware-imposed positive lower waiting-time bound changes optimization; independent external scientific validation has not been performed.
