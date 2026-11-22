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

The included `verify.py` requires Python 3 and only its standard library. Run `python verify.py` in the directory containing this file. The program compares the exact minimum relative deletion fraction computed by enumerating all overlapped lax splits with the independently calculated canonical row-column expression. It checks all 848 teams on four small product domains, eight rational decision thresholds per team, and the predicted worst-case geometries. Expected terminal line: `SEMANTIC_AND_EXTREMAL_CHECKS_OK 848`.

This computation is finite and does not establish the general theorem independently; the all-size proof is in `RESULT.md`. No independent audit or historical-priority certification has been performed.
