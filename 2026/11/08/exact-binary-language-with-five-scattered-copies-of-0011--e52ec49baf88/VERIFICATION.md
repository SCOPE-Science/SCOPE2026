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

# Reproduction and logical bounds

Run `python3 checker.py` with Python 3 standard library only. The checker verifies exhaustive lengths 0–14, independently computes literal quadruple counts through length 11, checks 4096 parameter words and compares 50 exact coefficient values against a separate capped-subsequence transfer recurrence. It prints PASS when all assertions succeed.

The infinite classification is proven in RESULT.md by unused-symbol deletion and the five-occurrence active-core argument. The finite tests are supporting checks only. No external independent audit has been performed. No formal proof-assistant certificate is claimed.
