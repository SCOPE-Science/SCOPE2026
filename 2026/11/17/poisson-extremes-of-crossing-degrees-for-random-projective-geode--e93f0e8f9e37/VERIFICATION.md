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

The standalone `verify.py` was run with Python, NumPy and SciPy. It terminated successfully with markers `PROJECTIVE_EXTREME_DEGREE_CHECKS_OK` and `POWER_LAW_EXTREMES_CHECKS_OK`.

Checks include direct three-dimensional projective-arc crossing calculations, comparisons between measured conditional degrees and their geometric binomial expectations, exact integration of the Haar endpoint length distribution, quadrature of the fixed-degree mixture and its asymptotic coefficients, tests for additional power-law length distributions, and exact finite-sample shortest-length survival versus the asymptotic minimum-degree law.

The infinite point-process statement is established analytically by the conditional crossing identity, rare-length Poisson convergence, concentration of local degrees and a Chernoff union bound excluding remote arcs. The numerical tests neither prove historical originality nor amount to independent validation. The model assumes independently sampled isotropic projective arcs and the stated short-length tail.
