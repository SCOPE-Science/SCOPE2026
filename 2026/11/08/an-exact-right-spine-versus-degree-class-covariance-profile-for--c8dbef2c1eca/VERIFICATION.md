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

# Verification record

`python verify.py` completed with: `PASS: 159 exact recursion covariance checks, 27 exhaustive mixed degree-covariance checks; permutations through n=9.` The recursion values were compared exactly as fractions at each size 2 through 160. The independent exhaustive constructor counted all 409,113 insertion orders through nine keys and checked all three covariance entries at each size. The proof is an exact formal-generating-function derivation for every integer order, not an extrapolation from enumerated data. Independent audit has not been performed. Historical priority risk is described in REVIEW.md.
