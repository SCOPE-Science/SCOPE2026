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

# Mathematical verification

A standalone exact symbolic verifier (`verify.py`) evaluates discriminants of \((u+1)^d+(u-1)^d+s\) and resultants of the associated degree-\(m\) polynomial for \(d=4,6,8,10\), tests the identity with multiplicities and signs, tests squarefreeness and distinctness from \(s=-2\), and checks the expected number of critical-value factors. A successful replay prints `VERIFY_OK`. No floating-point threshold or probabilistic check is used.

The all-even-degree theorem is proved by the derivative factorization, the distinct critical-value argument, local analytic geometry and regular base-change of splitting fields. Finite exact symbolic cases are independent consistency tests, not exhaustive evidence of an infinite claim. Historical priority is provisional; the full companion preprint arXiv:2610.09331 could not be inspected and independent mathematical audit has not been performed.
