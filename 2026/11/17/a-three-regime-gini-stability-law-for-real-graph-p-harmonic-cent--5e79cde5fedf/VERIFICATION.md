---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Directly reconstructed the first-order force-balance equation, uniqueness from strict convexity, and translation/coordinate monotonicity. For any nonnegative barycentric weights w summing to one, a nested layer-cut decomposition yields an exact Gini norm: 1+max_{nontrivial S} [k+(m-2k)w(S)]/[k(m-k)], k=|S|. At p=2 the uniform weights give 1+2/m. For p>2, implicit differentiation at nonconstant input and the force balance with exponent q=p-1, concavity of t^((p-2)/(p-1)), imply every derivative mass <=1/2; the cut formula then bounds the Jacobian by 1+m/[2(m-1)], integrated along data segments. At (1,-1,0,...), its Jacobian has masses (1/2,1/2,0,...) and a singleton perturbation attains this constant locally. For 1<p<2, monotonicity places centre differences between min/max input differences, giving global factor <=2. Taking a=(0,1,-t,...,-t), t=(m-2)^(-1/(p-1)), centre zero, perturbing the zero leaf by h yields c_h/h->1 and Gini ratio->2. At m=2 the p-centre is the midpoint and ratio equals 2. Independently enumerated exact rational cut norms for m=3,...,8 including uniform and two-extreme masses; these finite checks support, but do not substitute for, the analytic unbounded proof.

## originality

PASS

Best-of-knowledge priority PASS for the exact three-branch metric-specific sharp coefficient. Closely related variational p-star and Gini results were read at statement/proof level, but measure different normed operators; no domination or change of normalization implies these constants. Unindexed barycentre inequalities remain a priority risk.

## value

PASS

The exact three-exponent regime discontinuity under the natural complete-pair dispersion metric exposes different nonlinear sensitivity geometry on a one-hub graph; superquadratic derivative mass cap and subquadratic singular concentration are distinct, nontrivial mechanisms, not a renamed extension-operator norm. The coefficient sharpness across all leaf counts and all exponents is a useful stability classification. Exact p=2 and p≠2 transition is not implied by classical coordinatewise Lipschitz bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
