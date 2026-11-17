---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS. The equal-facet Dirichlet mixture has barycentric covariance eigenvalue 1/[m(m-1)], giving affine kernel K=m(m-1) sum_i lambda_i(x)lambda_i(y)-(m-2). Convexity of the absolute row integral places its maximum at simplex vertices, and sign conflict on positive-measure facet neighborhoods makes them the only norming evaluations. The beta mixture integrates negative mass to a_m/m q_m^(m-2)-1, where a_m=m^2-2m+2 and q_m=a_m/[m(m-1)]. The resulting norm 2a_m q_m^(m-2)/m-1 is strictly below the full-volume norm; the finite binomial certificate and Taylor expansion give a gap limit 2/e. Independent exact rational integrals m=3..8 and symbolic prior-specialization checks agree. All claims restricted to regular simplices or equal-facet measures, d>=2.

## originality

FAIL

FAIL from decisive full-text older coverage. The published 2026-10-25 result Exact affine least-squares amplification across simplex skeleta proves for every n-vertex simplex and every face rank s the norm 2B_{n,s}(1-nu_{n,s})^s-1, its vertex attainment and sign-kernel positivity defect. Substituting n=m and s=m-1 gives B=m-1, nu=(m-2)/[m(m-1)], hence 2(m-1)q_m^(m-1)-1, IDENTICAL to 2(a_m/m)q_m^(m-2)-1 because (m-1)q_m=a_m/m. The same earlier result includes the solid-volume endpoint s=m. Strict inequality and 2/e gap are elementary inequalities/asymptotic consequences of the previously known two exact formulas. This is statement/implication coverage, not mere title overlap.

## value

FAIL

FAIL for independent contribution: the core norm, vertex norming, negative-mass extremizers and volume comparator are special cases of a stronger published complete skeletal projection profile. The remaining surface-volume inequality and constant 2/e are direct algebraic subtraction and elementary binomial/Taylor analysis of those published formulas; no separate motivated unknown invariant or substantial new structure survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
