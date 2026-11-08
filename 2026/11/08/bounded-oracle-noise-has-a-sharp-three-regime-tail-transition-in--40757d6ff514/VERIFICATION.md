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

The one-step identity was independently checked with rational arithmetic. The `verify.py` program checks critical exact tail values, asymptotic supercritical tail coefficients by one-dimensional quadrature, the critical symmetric bounded case, and the near-critical finite moment integral. Its stdout is included as `verification_output.txt`. Exact mathematical assertions and their assumptions are proved in `RESULT.md`; tests of finite cases alone do not certify infinite limiting claims. The result is not a statement about the iteration at later times, or about arbitrary noise laws.
