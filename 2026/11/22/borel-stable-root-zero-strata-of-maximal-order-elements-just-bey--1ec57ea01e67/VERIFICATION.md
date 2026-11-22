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

Run \(\texttt{python3 ut_exponent_profile_verify.py}\) with Python's standard library. It enumerates the entire strictly upper-triangular matrix space, computes powers independently of the path-count proof, and checks exact conditional counts for all zero patterns. Verified cases are \((q,r,n)=(2,2,4),(2,3,5),(2,4,6),(3,3,5)\); the second is a test of the underlying matrix-power identity rather than a prime-power exponent boundary. The packaged output \(\texttt{verification_output.txt}\) shows exact totals and the ending sentinel \(\texttt{UT_EXPONENT_ROOT_PATTERN_VERIFIED}\). The universal hyperplane/field theorem is proved algebraically, not certified by finite enumeration. No independent audit has been performed.
