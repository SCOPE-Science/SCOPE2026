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

The all-order proof is the five-case analysis in RESULT.md. It establishes all off-band independence statements, computes the three possible adjacent joint probabilities exactly, and telescopes the column sums. Run `python verify_record_peak.py` to independently enumerate all uniform permutations of sizes three through eight. The program passed 160 exact rational assertions; finite enumeration is not a substitute for the analytic all-order argument. No external validation or independent audit was performed.
