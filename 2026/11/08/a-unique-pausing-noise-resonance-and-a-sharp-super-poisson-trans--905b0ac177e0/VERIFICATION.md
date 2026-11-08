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

# Analytical and computational checks

Run `python verify.py` in the directory containing this file. Python 3, SymPy and NumPy are required. It reconstructs every transition from the specified model, computes stationary and tilted counting equations, compares the closed-form rational current/Fano expressions, verifies all claimed derivative coefficient signs and ordered positive-zero isolators exactly, counts positive roots of the super-Poisson threshold polynomial by an exact Sturm algorithm, verifies both rational limiting functions and the one-site formula, and checks 16 independent tilted-eigenvalue second derivatives numerically.

The proof of existence/uniqueness on continuous infinite parameter ranges uses the exact symbolic identities plus Descartes' rule, rational root isolation, Sturm count and derivative-sign trapping. The 16 spectral finite differences are cross-checks only. No independent audit has been performed. The result is restricted to two sites and equal unit entry, hop and exit rates, with strictly positive pausing/unpausing rates.
