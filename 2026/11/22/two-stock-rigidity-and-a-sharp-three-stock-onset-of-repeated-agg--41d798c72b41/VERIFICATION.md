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

# Verification and limits

Execute `python3 checker.py` with Python 3; no external packages or data are required. The reproducible exact-rational check verifies the three-stock counterexample and Descartes certificate, yielding `EXACT CERTIFICATE PASS 40 assertions`. The step bounding all two-stock cases by one crossing is a symbolic argument in `RESULT.md` using the exact logistic solution, positivity of denominators and Rolle's theorem, and is not inferred from experiments.

The computed polynomial roots are supplementary numerical interpretations. The proof and exact-rational certificate establish the two strict positive roots, not their floating-point rounding. No field data, measurement-noise assessment, independent reviewer, or outside certification is supplied. Full-text priority comparison was unavailable for some historical works; literature priority remains provisional.
