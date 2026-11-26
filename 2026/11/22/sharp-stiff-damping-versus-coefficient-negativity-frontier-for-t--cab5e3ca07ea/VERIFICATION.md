---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The first three order conditions give mean 1/2 and variance 1/12 at two distinct sorted nodes, and c in [0,1] gives u in [1/6,1/2]. Independently, in the B-orthonormal basis (1, sqrt(12)(c-1/2)), the matrix A has first column (1/2,1/sqrt(12)) and upper-right entry -1/sqrt(12) by the remaining order condition. In that basis the algebraic-stability form is diagonal with entries 0 and twice the lower-right entry of A, so that entry is t/6 for arbitrary t>=0. This is reversible and verifies exhaustiveness. The scalar test function in this basis gives the stated numerator and denominator, and residual |1-t|/(1+t) without a degenerate leading denominator. The upper-right Butcher-entry depth is strictly positive and strictly increasing in t at every u; at the least feasible t=(1-rho)/(1+rho) the other entries are positive. The derivative of the remaining depth function in u is strictly increasing for u>1/6, and its boundary signs are (3t-1)/8 and (5+t)/8. This proves attainment, the change at rho=1/2, the root characterization, and uniqueness including the equality case at the transition. Independently checked the exact Radau IIA tableau and sampled depths 1/12, 1/18, 0.04503467712462134 at rho=0,1/2,3/4, and the limit 0.03563906993888331.

## originality

PASS

Best-of-knowledge pass for the profile with 0<=rho<1 and residual constraint sigma<=rho, including saturation and the boundary-to-interior transition. The earlier unconstrained minimum, uniqueness at that endpoint, and the classical Radau tableau are credited rather than counted as new. The closest indexed statements and available comparisons do not exhibit a dominating result for the strict-budget profile. Primary-source access was incomplete.

## value

PASS

Stiff-limit damping and the size of negative Butcher entries are natural, distinct design constraints. The exact Pareto profile supplies a uniquely determined tableau for each budget and a nonobvious change from an endpoint node to two interior nodes at rho=1/2. This information is useful even knowing both the classical zero-residual tableau and the old unconstrained minimum; it is not an SSP or finite-step optimality theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
