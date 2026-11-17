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

# Verification and limits

The standalone command `python3 verify_antiprism.py` completed with 261044 assertions, using only the standard Python library. It independently reconstructs vertices, both triangular-facet normal orbits, support planes, incidence, adjacent-facet angles, and signed face-pyramid volumes for every order from 3 through 30; it checks the exact optimizer identities and sampled global bounds.

The finite tests are not a proof of statements for all \(n\) or all real aspect ratios. The written analytical proof supplies that argument by a monotone-crossing identity, a factored equality equation, a fixed-circumsphere volume derivative, and elementary asymptotics. No independent audit or external formal certification has been performed.
