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

The self-contained `verify.py` reconstructs all labeled Cayley trees using Prüfer words, assigns all independent edge orientations, and checks exact rational mean, total source–sink covariance, source variance, diagonal marked joint probability, and off-diagonal marked joint probability for each integer size from two through six. Its output includes `EXACT_PRUFER_AND_ORIENTATION_CASES 43614` and `VERIFY_OK`. The 199 additional finite sign checks are diagnostic only. The infinite-sample validity, strict signs and limiting correlation follow from the displayed analytic identities and their proofs, not from computational extrapolation.

Run `python verify.py` beside `RESULT.md` with Python 3, without external packages or data files. No independent audit has been conducted. Historical novelty beyond inspected source materials remains unverified.
