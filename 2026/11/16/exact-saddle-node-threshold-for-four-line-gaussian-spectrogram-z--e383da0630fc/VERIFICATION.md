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

# Verification

The analytic proof is in `RESULT.md`. `CHECK.py` independently calculates the exact cubic derivative and discriminant, compares the covariance-based profile with the rational representation, checks critical factoring and fold derivatives, and performs finite numerical cross-checks. Install with `pip install -r requirements.txt` and run `python CHECK.py` in the extracted package. The observed successful output was `FOUR_LINE_INTENSITY_CHECKS_PASSED 317`.

These checks do not replace the proof of the all-parameter root count. A single representative interior sign value, discriminant signs, positive endpoints, and connectedness without root collisions or boundary crossings establish that count for the entire positive parameter range. The analytic zero-count intensity is for complex transform zeros, not measured spectrogram local maxima. Independent audit has not been performed.
