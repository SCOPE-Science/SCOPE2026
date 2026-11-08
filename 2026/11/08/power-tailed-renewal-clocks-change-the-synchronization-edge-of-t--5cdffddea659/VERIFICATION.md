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

# Checks and mathematical limits

Execute `python3 check.py` with Python 3 and no additional packages. The recorded check returned `PASS: 753 numerical diagnostic assertions; three coupling regimes, exact densities, critical exponents and stationary normalization.` It tests both the exact Lomax law and a mixture-clock law having the same leading algebraic survival exponent. The script evaluates the inverse trajectory, flow derivative, exact stationary push-forward formula, normalization, limiting boundary coefficients, and the two-sided near-critical crossover for multiple coupling constants and tail exponents.

The essential verification of the universal claim is the algebraic logistic-flow inversion, the equilibrium-renewal age identity, and the explicit comparison of exponentially versus algebraically relaxing amplitudes, and direct inversion at both near-critical cutoffs. Finite numerical grids cannot establish the asymptotic theorem or originality. The theorem excludes an initial amplitude equal to the supercritical fixed point, for which the stationary law is a delta mass. Originality is qualified by the possibility of broader unindexed renewal-flow results. Independent scientific validation has not been performed.
