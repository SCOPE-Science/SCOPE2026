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

# Reproducibility

Execute `python3 verification/verify_ladder.py` with Python 3.9+ and no third-party packages. Its independent full-edge union–find enumeration reproduces the exact conditional-crosslink formula in 42 rational cases. The program also checks 70 small-failure optimizer comparisons, 64 threshold cases, and 24 perfect/imperfect/three-link placement conditions; every assertion passes. The checked rail lengths and parameters are finite, and the complete all-length theorem is proved symbolically in `RESULT.md`. The cubic and higher terms at the joint-limit threshold are not established.
