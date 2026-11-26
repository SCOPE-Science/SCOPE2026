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

Attaching one extra vertex to the roots identifies root-marked forests with spanning trees of an augmented complete graph. Incident edge weight z gives reduced Laplacian (n+z)I-J and determinant z(n+z)^(n-1); extracting coefficients gives R_(n,k). In both ensembles, a tagged size s gives a factor binom(n-1,s-1) times the relevant tree count on s vertices times the forest count on n-s vertices with k-1 components. In the rooted law the adjacent ratio therefore equals kn/((k-1)(n-k)) times (1-(k-1)/(n-s)), strictly decreasing on the claimed common support. The upper boundary has ratio zero, and the deterministic laws at k=1 and k=n give the remaining cross inequalities. Single crossing gives stochastic order and shared inverse quantiles give the simultaneous coupling. In the unrooted law the two-forest count follows by Lagrange extraction of (T^2-T^3+T^4/4)/2 with T=ze^T, or directly from the earlier exact table formula. The quotient H_m=(m-1)(m+6)/(2m^2) satisfies H_m-H_(m+1)=(m-2)(5m+3)/(2m^2(m+1)^2). The three-versus-two tagged mass ratio on common support is proportional to H_(n-s). It increases from s=1 to s=2 at every n>=5, while the larger support of the two-component law forces a drop to zero at s=n-1. The latter also disproves the opposite LR order. At n=4 the ratio is constant on the common support (H_2=H_3), then zero, and at n=3 the three-component size is deterministically one. Thus five is exactly minimal; none of this disproves ordinary stochastic order in the unrooted model. Independent replay of all 1024 edge subsets at n=5 recovered unrooted tagged count vectors (16,12,18,64,0) and (15,12,18,0,0) and checked the LR cross-products for both ensembles (/workspace/review_checks.py, forests). This is bounded corroboration; supplied code was inspected but not executed.

## originality

FAIL

The explicit order statements are not asserted in the prior sources inspected, but both are mechanically implied by verified prior exact formulas for the same laws. Pitman's rooted tagged distribution determines the rooted comparison by division. The unrooted boundary is a direct calculation from the exact fixed-component count formula attributed to Rényi and documented before this record in OEIS A105599, combined with the same elementary tagged-component decomposition already used for that triangle. The decision does not rely on a later indexed result or a missing full text.

## value

FAIL

The rooted-versus-unrooted contrast is well motivated and the boundary is exact. For this narrow claim, however, both sides reduce to adjacent ratios of existing exact counts and a support comparison. The frozen scope adds no independent structural principle or order result beyond this routine consequence of the known laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
