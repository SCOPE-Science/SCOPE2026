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

The analytic derivation is in RESULT.md, sections Proof and Assumptions and scope. The included `verify_uniform_ritz.py` uses a deterministic NumPy random generator, a scipy incomplete-beta evaluation and direct quadratic-form calculations, and completed 11,209 elementary checks. These tests include negative-direction equivalence in the exact two-by-two sketch setup, the real-range identity under undersampling, the scalar exception, the arcsine specialization, and simulations compared with theoretically predicted beta probabilities using conservative tolerance bounds. No numerical finite experiment is a proof of almost-sure surjectivity or asymptotic normalizations; those are established symbolically in RESULT.md. No independent audit has been performed.
