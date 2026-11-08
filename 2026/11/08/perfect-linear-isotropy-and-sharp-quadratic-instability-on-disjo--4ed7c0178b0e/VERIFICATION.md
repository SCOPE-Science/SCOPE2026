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

The analytical identities and fixed-dimension expansion are given in `RESULT.md`. The package includes `check_axis_caps.py`, an executable checker with a separate numerical-quadruple-moment path and a symbolic path. It returned `AXIS_CAPS_SPECTRUM_CHECKS_PASS 490` when run in this environment. The checks are finite or symbolic checks of specified algebraic identities; independent mathematical validation was not performed. The theorem covers all integer dimensions \(d\ge3\) and all thresholds \(2^{-1/2}\le t<1\), not merely the test cases.
