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

Run `python verify.py` with Python 3 and its standard library from the directory containing the seven files. The checker verifies the exact rational example roots and strict interior sign, the equilibrium parameter identities, illustrative domain-length Fourier signs, five normalized Gaussian parameter families and four subcritical diffusion offsets, consecutive-mode interval counts, and near-fold numerical ratios. Its output was inspected and returned `PASS`. The full infinity-of-lengths result is established analytically in RESULT.md from the exact spectrum, strict concavity, interval arithmetic, and fold Taylor expansion—not inferred from the finite tests.

No independent mathematical audit or third-party validation was performed. Generic historical-priority uncertainty and the limitations of linearization remain.
