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

The analytic derivation is in `RESULT.md`, Steps 1–5. The reproducer `check.py` independently evaluates the scalar minimum density and its entropy in SciPy quadrature, checks the exponential marginal transform algebra numerically, tests the mixture identity and all stated error bounds at several dimensions, and checks the reported benchmark values.

Run: `python check.py` (Python 3, SciPy required). The test output is finite-sample numerical evidence only. The statement for all dimensions and the limiting expansion depend on the entropy identities and classifier proof, not on any finite computation. The present package has no independent mathematical audit.
