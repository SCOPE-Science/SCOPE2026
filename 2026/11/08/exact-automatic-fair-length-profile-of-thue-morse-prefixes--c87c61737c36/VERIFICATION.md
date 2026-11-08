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

# Reproducibility

Run `python3 verify_tm_fair_prefix.py` with Python 3.8 or later. No third-party Python packages are needed. Expected final output:

`TM_FAIR_PREFIX_VERIFY_OK 2048 independent_dynamic_program pair_count_crosscheck`

The verification program constructs the word from bit-count parity (independent of the four-block proof), computes exact fair factorization DP for all prefixes up to length \(2048\), checks the theorem casewise, independently counts ordered pairs for smaller substrings, and checks the exact signed subsequence-difference formula through \(2048\). It uses exhaustive finite tests only to validate the code and catch mistakes; the proof in RESULT.md is all-length and self-contained. The scientific review is not an independent audit.
