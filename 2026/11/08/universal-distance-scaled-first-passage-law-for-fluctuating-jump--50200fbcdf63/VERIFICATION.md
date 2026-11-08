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

# Verification notes

The analytical claim is supported by the proof in RESULT.md. The independent-rate Laplace transform is raised to the number of complete refresh blocks, with an additional residual-block factor; no independence of positions and operational times is assumed beyond the expressly constructed independent unit-rate spatial process and random rate sequence.

Run `python check.py` with SciPy and mpmath. The script checks 37 deterministic cases: gamma-function equivalence with the known first-moment coefficient, finite-site exact sine-kernel quadrature versus the scaling-integral formula at several indices and start distances, positivity and monotonicity of the proposed survival, and the limiting power-tail constant. The deterministic tolerances apply to those specified finite-size numerical cases; passing does not constitute a proof of the infinite-distance theorem.

The limiting moment claim is established only for positive orders strictly below the threshold; the higher-order divergence statement concerns the limiting variable and is not represented as a finite-size asymptotic at the critical exponent. First-public date and category follow the arXiv original version and statistical-mechanics subject classification. Independent audit and independent validation have not been performed.
