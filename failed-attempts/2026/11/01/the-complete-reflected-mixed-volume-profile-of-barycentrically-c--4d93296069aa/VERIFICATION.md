---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The ratios are affine invariants; near the centroid the body has positive volume exactly for t>1/4. Independently, inclusion-exclusion in the barycentric affine hyperplane gives the normalized volume of the slice a≤lambda_i≤b as F(a,b)=sum_j (-1)^j binom(4,j)[1-4a-j(b-a)]_+^3. Its derivatives are the sums of the supporting facet area times altitude, with the lower sign negative. Center at barycentric (1/4,...,1/4); reflection moves the lower and upper support planes of K_t at rates 1/4-max(lambda_i) and 1/4-min(lambda_i), respectively. Differentiating F in that direction at (0,t) therefore gives 3M_t/V_T by first variation; inactive planes contribute zero. In the first simplex chamber min(lambda_i)=1-3t, max=t; in the two middle chambers min=0, max=t; in the final simplex chamber min=0, max=1. The resulting V and M polynomials match the frozen formulas in all open chambers, and extend to the common endpoints by continuity. In particular t=1/2 is the centrally symmetric affine octahedron. For rho=M/V, the sign of the two derivative factors is settled by expanding at 1/3 and at 1 (the latter has positive lower bound 1+6s-8s^2 for s in [0,1/2]). This gives strict decrease then increase with unique minimum 1, ratio 3 on the two simplex branches. Minkowski expansion gives difference-body ratio 2+6rho. The exact left/right series around t=1/2 have common quadratic coefficient 32 and cubic coefficients -32 and -224; distinct slopes of rho'' give no third derivative there and jump -1152. For t<1/4 there is no feasible point, at equality only the centroid, so the normalized ratio is undefined there. Independent symbolic replay with SymPy: python -B /workspace/review_evidence/2_slice.py; output 2_slice.txt. No submitted script executed; sampled tests do not prove the real-parameter assertion.

## originality

FAIL

The exact four-branch profile is mechanically implied by Postnikov's prior explicit P4 volume polynomial, not just by the sharp mixed-volume bounds cited in the frozen result. The monotonicity and differentiability assertions are not stated there; they are elementary one-variable derivative tests and local expansions of precisely those polynomials, not an independently distinct theorem about caps. No evidence of a prior printed equal-cap table is required for this decision.

## value

FAIL

This is a natural deformation between simplices and an octahedron, and the elementary facet proof is correct. But the proposed scientific invariant is an exact prior P4 polynomial specialization. Reexpressing it, checking the sign of the derivative, and reporting a cubic coefficient jump for this one rational function do not yield a distinct mathematical remainder warranting repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
