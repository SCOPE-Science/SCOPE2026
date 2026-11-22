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

# Reproducibility and verification

Execute `python verify.py` in the same directory as this document, using a standard Python 3 installation (no external dependencies). The full numerical checker printed `VERIFY_OK parameter_cases=1170 regimes={'equal': 59, 'two_latitudes': 266, 'pole': 845} boundary_checks=4 equal_lens=1`. It evaluates global maxima of the actual ball-containment quadratics, not merely a discrete boundary mesh; checks both contact conditions, positivity and the universal isotropic moment identities, and checks regime endpoints and the known equal-ball case. The proof of uniqueness, root monotonicity and the full continuous parameter-domain inequalities is in RESULT.md; finite diagnostics alone cannot certify those universal claims. The declared formulas do not cover nested balls, exterior tangency, dimensions other than three, or noisy-data inverse problems. Independent audit has not been performed.
