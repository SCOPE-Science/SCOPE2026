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

# Reproducible verification and limitations

Run `python3 verify.py` using Python 3 standard libraries only. The program enumerates every permissible addition among up to three fixed labelled new vertices for the nine stated test inputs; no edges between old vertices may be added. It independently extracts coefficients by a degree-vector dynamic program and checks both the minimum new-vertex count and exact number of labelled optima. Successful execution prints `ALL_CHECKS_OK`.

The mathematical proof in `RESULT.md` establishes the theorem for every finite member of the age. The finite tests have no claim to prove the infinite range by exhaustion. No independent external audit or validation has been performed.
