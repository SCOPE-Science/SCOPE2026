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

# Verification instructions

The exact numerical claim and its strict-inequality convention are defined in `RESULT.md`. Compile and run the independent programs with the commands in `RESULT.md` and compare the emitted table and extremizer list with `CENSUS.txt`. The expected C++ diagnostic is `SYNC_TERNARY_CXX_VERIFY_OK`; the expected Python final line is `SYNC_TERNARY_PY_VERIFY_OK`. Both verifiers enumerate all canonical square-free ternary words through length 28, and compute exact rational worst adjacent-interval LCS values independently. `CENSUS.txt` stores every row and all canonical extremizers at the transition lengths. These computations certify the finite exhaustive scope; the prefix argument supplies the stated unbounded-length cutoff, not further minimax values. Unindexed historical priority and external mathematical audit remain unverified.
