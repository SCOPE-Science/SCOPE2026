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

Run `python3 verify_square_index_patterns.py`. It independently computes all 373 prime masks below 2579 using Euler's criterion and an explicit nonzero-square set, checks the exact twenty-four exceptional primes and their missing-word counts, and verifies the last missing word at 193 and universality at 197. Successful output prints `PASS` and the fingerprint `ae46170c708cc49792a01577a3ce855d0f2c54dda0f6a570596d42045a6d44aa`. The analytic character-sum inequality proves universality for every remaining prime. No independent audit has been performed.
