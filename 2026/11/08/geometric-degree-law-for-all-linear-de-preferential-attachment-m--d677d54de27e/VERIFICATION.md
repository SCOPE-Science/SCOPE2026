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

Run `python3 verify.py` in the directory containing this standalone script. No external modules or network connection are required. The check enumerates finite exact-rational probabilities, verifies first-proposal rejection and normalizations of the sequential attachment law, checks uniform recursive generating functions, and samples coupled 20,000-vertex graphs for fixed \(m\in\{1,2,3\}\). In the package-generation review, the verifier printed `VERIFY_OK check_count= 156614`. The saved package was extracted and the verifier replayed before delivery.

The almost-sure theorem relies on the mathematical proof in `RESULT.md`: exact rejection probabilities and their independence; the exponential bounds, dyadic Borel--Cantelli, and monotonic interpolation; finite-coordinate concentration in the uniform model; and transfer of total variation. No finite test alone is taken as a proof of an infinite limit. No independent audit has been performed.
