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

# Reproducible checks

Run `python CHECK.py` in an environment with SymPy. The observed result was `THREE_LINE_MODALITY_CHECKS_PASSED 93`. The checker verifies exact derivatives, normalization, critical curvature, a sharp-height identity, test values in all modal regimes, and two Gaussian STFT polynomial reductions. The finite tests are not the proof of the all-parameter theorem; see the proof in `RESULT.md`. The source of the density is Gaussian logarithmic potential and Jensen's formula, with all hypotheses stated in the result.

Independent audit has not been performed.
