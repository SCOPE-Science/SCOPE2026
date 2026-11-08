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

The theorem is proved in RESULT.md for all integers \(r\ge3\) and all positive integers in the stated counting interval. No independent audit has been performed.

Run `python verify.py` (standard library only); compare to `verification_output.txt`. The checker tests 10,000 exact small inputs and exact arithmetic for \(3\le r\le50\) but cannot by itself certify the asymptotic conclusion; the proof uses a uniform Hoeffding inequality and a length-tail estimate.
