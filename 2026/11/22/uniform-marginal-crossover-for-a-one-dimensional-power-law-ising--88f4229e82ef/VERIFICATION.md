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

# Reproducibility and scope

Execute `python check.py` with Python 3 and the `mpmath` package (tested with 60 decimal-digit arithmetic). The test constructs energies independently as finite sums plus convergent Hurwitz-zeta tails, locates the discrete maximizer by monotone increments, compares closed-form energies against direct sums, and checks the asymptotic crossover on both sides of the marginal exponent. Its 159 deterministic assertions passed. The logarithmic scaling limit and uniform remainder are established analytically in RESULT.md, not by finite numerical evidence.

The verified claim concerns finite contiguous spin droplets in an infinite chain. Neither finite-volume spin-flip metastability nor finite-temperature transition times are assessed here. Independent review remains unperformed.
