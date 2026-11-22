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

The analytic proof uses the exact Jacobian formula (4), binary sign-vector norm identity (5), and an equality-attaining description of all subset odds under positive score diameter (6). Convex-segment integration and interior directional derivatives turn the local norm into the sharp global coefficient. The binary-encoded integer-partition reduction uses an explicit strict gap, not numerical equality testing.

Reproduce supplementary computations with `python3 checker.py` using only Python's standard library. This executes 10,099 assertions: exhaustive small integer-weight and sign-vector tests, random finite-pair bounds, near-boundary approximations and finite partition-gap comparisons. The checker is finite evidence only; it does not establish universal quantifiers, independent mathematical validation, or historical originality.
