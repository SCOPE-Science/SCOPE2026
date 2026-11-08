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

The theorem is proved by identifying a middle-first triple, showing a universal one-envy construction, characterizing forbidden rankings by endpoint deletion, and summing the exact factorial tails of the first-success stock size. No infinitary assertion relies on numerical experiments.

Run `python3 check.py` to exhaustively enumerate third-agent rankings and three-house assignments for each inventory size from three through eight. Independently computed envy objectives agree with the endpoint-deletion theorem, and the observed obstruction and first-success counts match their formulas. Limitations: the finite checker does not validate unbounded cases, sampling models outside independent atomless utilities, or any claimed uniqueness in the literature.
