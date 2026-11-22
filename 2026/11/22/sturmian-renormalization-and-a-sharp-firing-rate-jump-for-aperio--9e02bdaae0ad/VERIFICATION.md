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

The standalone `check_sturmian.py` was executed as a finite diagnostic. It checks 204 exact-rational parameter/phase cases, including four travel-time values and eight start indices, and a high-precision golden-slope approximation with direct word complexities through length twelve. Its expected printed status lines are PASS. The proof's first-return rotation and telescoping identities, not finite computation, establish the all-irrational and all-horizon statements.

The study does not verify any numerical membrane parameters producing a given reset-to-threshold travel time; this parameter is the exact positive input to the previously established post-first-spike projection law. No independent mathematical audit was conducted.
