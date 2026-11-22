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

Run the complete standalone checker with `python3 check_parabolic_acuteness.py`. Its printed success marker is `PARABOLIC_ARC_ACUTENESS_CHECKS_OK`.

The checker independently performs numerical quadrature of the two planar rectangle integrals, confirms the factored inequalities with actual planar Euclidean dot products, and compares an exact closed expression with fixed-seed sampling. It tests parameters on both sides of \(a=1\) and \(a=\sqrt2\), the \(5/2\) coefficients, and the large-arc behavior. Numerical checks do not establish global quantified correctness; the exact proof provides the all-parameter statement and the dominated-convergence limit. No external proof certificate or independent specialist audit is claimed.
