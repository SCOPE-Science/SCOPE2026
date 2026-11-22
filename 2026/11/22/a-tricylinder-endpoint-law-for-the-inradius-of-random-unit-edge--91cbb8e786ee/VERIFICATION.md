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

# Reproducibility and boundaries

The proof's exact ingredients are the face-altitude identity \(2R=\sqrt{\Delta/(1-m)}\), the normalized Gram density \((4\pi\sqrt\Delta)^{-1}\), localization of the three correlations to scale \(\sqrt\varepsilon\), and the independently integrated tricylinder volume \(8(2-\sqrt2)\). These yield the asserted asymptotic and conditional total-variation theorem without finite enumeration.

Run `python3 verify.py` beside the other extracted files. The checker requires only the Python standard library. It validates a quadrature of the tricylinder integral; compares independently computed facet distances and Gram expressions on 2,000 generated frames; estimates three probabilities by 1,500,000 independent spherical-coordinate samples; and checks the relative deficit's one-half threshold ratio. The reported seeded run returned `ALL_CHECKS_PASSED`. The stochastic tolerances are intentionally broad and are diagnostic, not a substitute for analytic proof.

The statement makes no claim of finite-sample error bars, second-order endpoint terms, or independent expert certification. The historical-priority comparison and remaining full-text access risk are set out separately in REVIEW.md.
