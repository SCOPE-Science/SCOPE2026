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

The theorem follows from the projected tangent-vector dot-product identity and an exact change of variables on the circular-spacing simplex. The independent numerical program `latitude_acute_verify.py` compares direct spherical-angle tests for 300,000 longitude triples with the one-dimensional integral and checks five near-threshold ratios. The code is a reproducibility aid, not an exhaustive or independent mathematical certification. There is no claim of formal proof, published priority, or independent audit.

To reproduce: install the two packages listed in `requirements.txt` with Python 3.10 or newer, then run `python latitude_acute_verify.py`. The program should report `LATITUDE_ACUTE_CHECK_OK`; these calculations do not certify historical novelty.
