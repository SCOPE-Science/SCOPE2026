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

The attached `verify.py` uses only the Python standard library and is run as `python verify.py`. It checks a bracketed solution of the exact stationarity polynomial, the derivative balance, the analytical inequality endpoints, numerical values of the sharp two-step distance, direct independent Simpson integration against the Haar scalar density at sampled angles, and nonattainment at a separate spectral-angle parameter. The exact global theorem and uniqueness follow analytically from the proof in `RESULT.md`, not from numerical sampling. No independent mathematical audit was performed.
