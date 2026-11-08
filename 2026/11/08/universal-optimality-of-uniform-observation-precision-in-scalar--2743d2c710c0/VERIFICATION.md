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

# Reproducible checks

Use Python 3 standard library only: `python3 check.py`.

The recorded `check_output.txt` contains `PASS 7609 exact-algebraic and numerical assertions` and the exact period-two example's numerically evaluated values. The code checks rational algebra and local convexity signs, telescoping identities, and broad randomized periodic recursions. Strict global claims for all dimensions/parameters/schedules are established by the written proof, not by exhaustive finite checks or the assertion count. No independent scientific audit has yet been performed.
