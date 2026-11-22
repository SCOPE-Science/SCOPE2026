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

## Reproduction
Run `python3 check_bpl.py` with Python 3 standard library. The certificate evaluates exact rational PMF and formal-log coefficients at a parameter grid, checks the equality boundary, and verifies an explicit overdispersed failure example. It reports 1384 passing finite/formula assertions. The included RESULT.md gives the proof over the infinite support and the first forbidden index asymptotic. No independent audit or complete computer-assisted formal proof is claimed.
