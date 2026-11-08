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

# Reproduction and verification

The standalone `VERIFY.py` uses only Python's standard library, including exact rational arithmetic and exhaustive enumeration of small ordered-sample spaces. Run `python3 VERIFY.py` in the extracted artifact folder. The checker performs 166 assertions covering sample-space moments, uniform-law identities and signs, the core-tail rational example, a convergence pattern, sufficient finite-size bounds, and Poissonized covariance signs. The exact infinite-family claims follow from the indicator identities and collision coupling proved in `RESULT.md`, not from any finite enumeration. The Poissonized result follows independently from mutually exclusive per-category zero/singleton indicators and Poisson independence. Independent audit: not performed.
