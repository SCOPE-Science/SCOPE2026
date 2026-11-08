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

Reproduce the standalone checks using `python verify_lollipop_spread.py`. Exact arithmetic checks enumerate all extreme clique assignments and unit path steps for 47 finite parameter pairs, then verify the integer quadratic optimizer for 35,920 parameter pairs and the first two-pattern tie at 17 threshold parameters. The finite computations support the calculation but the proof for all integer parameters is in the analytical argument. No external independent audit has been performed.
