---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The ordered Dirichlet(1,...,1) simplex has spacings Y_k=sum_{j>=k}P_j/j and the quadratic statistic equals sum_{a,b}P_a P_b/max(a,b). Third Dirichlet moments give Cov(P_j,G)=2(H_m-H_(j-1)-1)/[m(m+1)(m+2)], and the harmonic double sum gives (A_k^2+B_k-2A_k)/[m(m+1)(m+2)]. Consecutive numerators differ by 2(A_k-1)/k; endpoint signs and monotonic harmonic tails prove one crossover. For k/m->alpha, the exact variances Var(Y_k)=(mB_k-A_k^2)/[m^2(m+1)] and Var(G)=4(m-1)/[(m+1)^2(m+2)(m+3)] give claimed Pearson limit, with positive limiting denominator for alpha in (0,1). Independently evaluated 27 exact third-moment covariance cases m=2..7; finite checks supplement the all-m algebra.

## originality

FAIL

Earlier published Nov 2 result is the same mathematical theorem for the same uniform simplex, with an identical exact covariance, nonempty initial positive/terminal negative ranks and e^-2 asymptotic threshold. The new Pearson profile is elementary standard-deviation normalization of that exact previously published covariance using classical ranked-spacing variance; the paper does not isolate a mathematically new non-routine remainder. Full prior RESULT.md inspected, not inferred from a title.

## value

FAIL

The important mixed covariance and universal sign-boundary problem was solved by the earlier published theorem, including the complete m,k parameter domain. Normalizing that known covariance by standard Dirichlet variances gives an incremental algebraic Pearson expression without a separate motivated new phenomenon; the submitted claimed contribution therefore lacks distinct mathematical value beyond the earlier result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
