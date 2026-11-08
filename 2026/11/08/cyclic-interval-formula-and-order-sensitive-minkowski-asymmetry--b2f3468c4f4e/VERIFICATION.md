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

A standalone checker reconstructs exact rational barrier values and independently solves the original-support and center/dilation linear programs on finite samples. After installation of NumPy and SciPy, run `python verify_chainlink.py` to see `CHAINLINK_MINKOWSKI_SUPPORT_LP_CHECKS_PASSED`. The proof for every admissible parameter lies in the directed-cycle feasibility reduction, not in finite experiments. No independent mathematical audit has been performed.
