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

The independent finite direct-projection checker `CHECK.py` uses deterministic random unit vectors, a self-contained planar monotone-chain hull, and exact branch comparisons across representative heights. Execute with `python CHECK.py`. The proof in `RESULT.md` contains exhaustive symbolic global extrema and local analytic probability asymptotics; finite checker diagnostics do not prove any limiting statement. No independent mathematical audit was performed.
