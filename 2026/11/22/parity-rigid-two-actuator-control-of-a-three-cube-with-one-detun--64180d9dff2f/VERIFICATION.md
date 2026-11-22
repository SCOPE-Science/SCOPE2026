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

# Verification

Run `python3 verify.py` from this directory. It requires only the standard library and performs exact rational Gaussian elimination on every two-input Kalman matrix for nine nonunit positive rational conductances. It checks the predicted sixteen controllable pairs and the complete rank distribution, then verifies the homogeneous two-input impossibility and a successful three-input placement. All checks completed successfully prior to packaging. No finite test certifies the all-real-parameter claim; that rests on the explicit proof in RESULT.md.

The scientific literature comparison is provisional. The result has not been independently audited or experimentally validated on a physical network.
