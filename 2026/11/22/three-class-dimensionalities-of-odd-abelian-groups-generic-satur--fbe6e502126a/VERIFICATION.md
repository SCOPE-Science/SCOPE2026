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

`check.py` contains no external dependencies; invoke `python3 check.py`. This checks complete group addition tables, 15 explicit masks by direct quantified D2 and full sumset coverage, 1,536 candidate colourings for the three small groups, and exact rational evaluation and finite initial monotonicity checks for the tail. The unbounded tail itself is justified by the analytic monotonicity proof in `RESULT.md`, not by the finite loop. No independent audit or validation is claimed.
