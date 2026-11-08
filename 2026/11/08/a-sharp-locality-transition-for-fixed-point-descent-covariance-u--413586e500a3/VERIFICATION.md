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

Run `python3 verify.py` using Python's standard library only. The actual packaged checker was executed and returned `VERIFY_OK 225302 exact assertions`.

The program computes exact permutation weights by counting directed cycles for every permutation of sizes three through seven, tests six positive integer weights and four fractional positive weights, and checks individual mixed covariance entries as well as total covariance. It separately verifies formula summation, zero loci, and remote signs for sizes up to 39. Thus the checker is a reproducibility check for finite instances; it is not an infinite proof. The theorem's full domain is established in RESULT.md by forced-arrow enumeration and exact algebra. The conclusions concern covariance, not probabilistic independence, and novelty priority is subject to the limitations noted in REVIEW.md.
