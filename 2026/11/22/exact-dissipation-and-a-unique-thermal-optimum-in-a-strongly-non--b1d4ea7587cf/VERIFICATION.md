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

# Reproduction

Run `python check.py` with Python 3 standard library. The script constructs each small finite-state generator independently from the stated flip rates, checks stationarity by full incoming/outgoing flow, and compares its forward/reverse path entropy sum with the transfer-matrix formula and the first directional-lag slope. It also tests the monotone root for several coupling ratios and compares limiting roots.

This check covers only finite enumerations and sampled parameters. The universal statements for every ring size and coupling, and the sharp optimum, rest on the analytic proofs in `RESULT.md`. No independent mathematical audit has been performed.
