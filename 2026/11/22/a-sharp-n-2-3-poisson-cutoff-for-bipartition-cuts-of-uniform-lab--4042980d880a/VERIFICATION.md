---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

On the weighted complete graph the two within-class zero-sum subspaces have eigenvalues a+bz and b+az with multiplicities a−1 and b−1, and the remaining nonconstant classwise-constant direction has eigenvalue nz. Kirchhoff's theorem and Cayley normalization give the exact polynomial, hence the independent signed-binomial representation and the printed moments. With p=a/n, replace the positive binomial by its mean-matched Poisson at TV cost at most p (the binomial Stein–Chen bound) and split this Poisson into independent terms of means lambda=a(1−2a/n) and (a−1)p. The latter minus the negative binomial is an independent mean-zero shift of variance at most 2(a−1)p. TV of a unit shift of a unimodal Poisson is its maximum mass; telescope, bound that mass by min(1,lambda^−1/2), and apply Cauchy–Schwarz. This gives the quantitative bound and uniform convergence for a=o(n), even along bounded or oscillating sizes. For the uncorrected comparison the mean gap is Delta=2a²/n; Pinsker with D(Poi(a−Delta)||Poi(a))≤Delta²/a covers the subcritical regime, and Chebyshev at the midpoint covers the supercritical regime. In the critical regime the maximizing upper-tail event is k>Delta/log(a/(a−Delta)), with equality at an integer immaterial. The real cutoff is a−Delta/2+O(Delta²/a), the correction is o(sqrt(a)), and the two standardized cutoffs converge to −c^(3/2) and +c^(3/2). The ordinary Poisson CLT yields the claimed profile and the corrected TV error transfers it to the cut law. The exact law applies to any nonempty deterministic bipartition; the approximation is restricted to a=o(n) and does not use a sampled tree's proper coloring. Replay RESULT.md Proof headings Exact factorization through Uncorrected approximation. The Prüfer checker and VERIFICATION.md were inspected, not executed; the finite enumeration is not evidence for asymptotic coverage.

## originality

PASS

The exact cut PGF is directly covered by a specialization of an earlier weighted enumerator. The supported distinct contribution is instead the explicit TV error for the shifted bias-corrected Poisson throughout the sparse-side regime and the full Gaussian-CDF profile for failure of the uncorrected reference law. The inspected sources do not state or provide this combined approximation; the same exponent in the closest other indexed result refers to a different law and mechanism.

## value

PASS

The cut size is a natural boundary statistic of a uniform labelled tree for a predetermined sparse group. Exact enumeration alone does not tell when an easy distributional surrogate is trustworthy. The bias correction remains accurate beyond the entire failure region of the naive law, and the explicit critical TV profile quantifies that failure rather than reporting a qualitative change of means or only a CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
