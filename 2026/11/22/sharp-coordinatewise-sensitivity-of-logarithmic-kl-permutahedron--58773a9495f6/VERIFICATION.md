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

The closed-form norm computation and sharpness proof are written in `RESULT.md`. Run `python check_projection.py` using Python 3 with NumPy and SciPy to reproduce the deterministic PAV-based stress tests and finite-difference sharpness approaches. The script tests 7,000 pairs and seven near-vertex constructions; these finite experiments cannot certify the theorem for all real inputs, dimensions or weights. No independent audit or formal infinite-domain verification has been performed.
