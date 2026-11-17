---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

PASS: For a>0, g != 0, 0<=delta<1, equal sampling probabilities and t=eta*a in 0<t<2/(1+delta^2), the affine two-step laws give p=1-2t+(1-delta^2)t^2 and offsets t^2(delta+/-1); independent-index SGD gives S=1-2t+(1+delta^2)t^2. Solving the means and variances yields M_WR=t^2/(1-S) and M_RR=t^4[delta^2/(1-p)^2+1/(1-p^2)]. Independently simplified their rational ratio to 2P_z(t)/([2-(1-z)t]^2[2-2t+(1-z)t^2]) by exact SymPy arithmetic and re-counted roots at z=1/4 (2) and 1/3 (0). The transformed Descartes-sign bound, exact degree-7 resultant and Sturm intervals isolate the unique active z*=0.315146953...; both boundaries have P<0 and z=0 factorization is separate. Finite root computations check critical algebra, not replace the analytic all-z proof.

## originality

PASS

PASS best-of-knowledge: the exact stationary two-root reentrant risk comparison and algebraic curvature threshold for two unequal-curvature scalar quadratics are not supplied by the inspected common-Hessian stationary analyses, one-epoch reshuffling reversals, or order-policy optimization theorems. Qualitative reshuffling disadvantage was already known. Novelty concerns the full last-iterate stationary phase frontier, not the existence of a reversal.

## value

PASS

PASS: A dimensionless exact two-root phase classification identifies when sampling without replacement is strictly worse than independent sampling even for two individually contractive scalar gradients. The sharp curvature-ratio threshold gives a quantitative structural boundary relevant to claims of uniform reshuffling superiority; not merely an isolated numerical witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
