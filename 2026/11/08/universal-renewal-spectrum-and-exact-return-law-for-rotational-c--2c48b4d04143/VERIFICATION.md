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

# Reproducible verification

Run `python3 check.py` in an ordinary Python 3 environment. No external packages or internet are required. The self-contained checker constructs exact integer covering matrices for each admissible \(n\) and coprime step, confirms the characteristic determinant coefficient-by-coefficient via Newton identities, and checks trace recurrences. For smaller cases it enumerates closed paths, computes the unique physical fixed points by exact rational arithmetic and independently checks the admissibility and nonduplication of every point.

The completed run reports `VERIFIED exact checks: 35766`; covering matrices for \(3\le n\le16\); and physical periodic points for \(3\le n\le8\) and \(1\le k\le9\). These finite checks neither certify the universal theorem nor address possible literature priority; those rely on the proof and documented source comparisons. No independent audit was performed.
