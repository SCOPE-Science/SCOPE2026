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

# Verification evidence and limitations

A self-contained symbolic proof appears in RESULT.md. The critical steps are (i) a monotone shift of any extremal circular window to a one-run boundary, (ii) an interval-wise comparison of the two candidate starts, yielding an exact defect, (iii) the longest-one-run restriction for possible normal phases, and (iv) a rotation-quotiented count of all four-run parameter quadruples.

Run `python verify.py` from the package directory (Python 3.9+; standard library only). The verifier computes maximum one-counts of all length-up-to-period circular factors directly using doubled strings and prefix sums, then independently checks the candidate defect and every cyclic starting phase. Verified in the current computation:

```
VERIFY_OK: exhaustive quadruples 2401 ; larger seeded quadruples 650 ; all 32 length-specific necklace counts
```

Coverage: all four-tuples with entries between 1 and 7, 650 reproducibly seeded positive quadruples with entries at most 50, and each length 4 through 35 for count coefficients. This is not an exhaustive check of the infinite domains. The mathematical completeness of the claim rests on the displayed exact proof, not on extrapolating empirical checks. The known OEIS coefficient sequence is expressly credited rather than treated as newly found.
