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

Run `python3 verify_band.py` with Python 3. The checker uses exhaustive integer cut enumeration on bounded local windows for bandwidths two, three, and four and counts host cliques on three finite cycles. It reports `LOCAL_CHECKS_PASS 95879`. The published proof is symbolic and proves the fixed-bandwidth asymptotic result; enumeration is neither a substitute for the mixed factorial-moment argument nor a claim of exhaustive coverage for arbitrary bandwidth. In particular, no external certification or independent audit was performed.
