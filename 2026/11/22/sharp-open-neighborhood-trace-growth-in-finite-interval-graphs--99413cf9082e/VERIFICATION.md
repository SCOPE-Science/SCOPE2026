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

The assertion is established by the endpoint-prefix proof and the path witness in `RESULT.md`. The standalone `verify.py` enumerates all endpoint matchings for up to seven marked intervals, calculating open traces of marked vertices directly and auxiliary traces from endpoint gaps; it then checks the standard path witnesses for up to twenty marked vertices. These tests are finite and do not prove the bound at arbitrary size. No independent audit is asserted.
