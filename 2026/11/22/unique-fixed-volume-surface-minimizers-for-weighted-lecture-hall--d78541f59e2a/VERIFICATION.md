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

The simplex has volume ∏s_i/n!, and each facet has area nV times the norm of the gradient of the vanishing barycentric coordinate. This gives precisely the two end terms and the adjacent-pair norms in the stated objective. Normalize the product, and use t_i=log(1/s_i) with ∑t_i=0. Weighted Cauchy–Schwarz bounds the second directional derivative of each edge norm below by (e^{2u}h²+e^{2v}k²)/sqrt(e^{2u}+e^{2v}), so the full Hessian is positive definite. The objective dominates exp(max t_i), and max t_i≥||t||∞/(n−1) on the constraint, proving coercivity. Equating derivatives and summing gives the Euler system with multiplier M_n/n; strict convexity gives its unique positive normalized solution. Reversal preserves the objective. If y_1≥y_2, for n≥3 the difference of the first two derivatives is positive because the subtracted term y_2²/sqrt(y_2²+y_3²) is strictly smaller than y_2≤y_1 and the shared-edge contribution is nonnegative. For n=2 reversal yields equality; for n=3 the reduced equation 2r²−1=sqrt(1+r²) selects r=√5/2, giving M_3=5(2/√5)^{1/3}. Scaling proves the ratio and its exact equality condition at every prescribed positive volume. The finite Gram and numerical KKT checks in VERIFICATION.md were inspected, not rerun; they are not needed for the proof.

## originality

PASS

The known exact area formula and standard convex optimization tools are not the contribution. The distinct supported finding is the all-dimensional fixed-volume optimizer with shape, sharp ratio and equality conditions. No inspected antecedent states or already implies that classification.

## value

PASS

Weighted chain simplices are a natural Euclidean family with a known general surface formula. That formula alone does not distinguish the standard equal-weight shape from its competitors at fixed volume. The uniqueness and strict end-weight comparison resolve this for every dimension, and the Euler characterization determines the sharp scale-free constant even without radicals for n≥4.

The dated certificate retains the supplied scientific assessment, sources and limitations.
