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

Sum the Ewens weights over the complement of fixed disjoint marked blocks of total size s. Its rising-factorial normalizer cancels all but the last s factors of the original normalizer. Squaring the resulting one-partition probability and counting ordered distinct labels gives the stated factorial moment, including k=0 and k=n. For each fixed k it tends to c^(2k); the next moments control uniform integrability, and Poisson moment determinacy gives the count limit. On the nonnegative integers, convergence at each mass point and tightness give total variation. Conditional on C_n=k the locations are a uniform k-subset. In uniformly random order, sampling without replacement differs from independent discrete uniform sampling by at most the collision probability O(k^2/n); hence the rescaled counting measure tends to that of k independent uniforms. Tightness in k and the Poisson count identify the weak PPP limit, not TV for locations. The whole common two-block expectation is O(1/n) by the marked identity. A common block of size at least three forces any chosen labelled triple from that P_n block to lie together in independent Q_n; consistency gives probability 2/[(theta_n+1)(theta_n+2)], independently of the choice. The sum over P_n blocks is bounded in expectation by this probability times E K(P_n)=O(sqrt(n) log n), so all larger common complete blocks vanish in probability. Finally, restriction to a fixed pair gives probability 1/(theta_n+1) in one partition and independence yields the exact mean of R_n; this statistic counts pair membership in the meet and the frozen quantitative claim is about its expectation. The supplied n<=6 rational checker was inspected, not executed; it does not establish the limit or exclusion estimates.

## originality

PASS

The distinct claim is the law for all exact block agreements of two independent Ewens draws in the square-root concentration regime, including the spatial limit and the exclusion of all larger agreements despite linear expected shared pair membership. The marked Ewens formula, one-draw small-component approximation, elementary rare subset overlaps, and the pair-expectation calculation are not separately new. The closest published and indexed comparisons concern either one draw, or cells in the intersection of independent uniform equivalence relations. In actual checked passages neither covers the joint exact-block law here.

## value

PASS

Independent random partitions can be compared by full-block agreements or by co-memberships, two natural but inequivalent notions. The exact critical law makes their difference quantitative: all complete matches reduce to a spatial Poisson process of singletons, with an explicit no-match probability, while shared pair count has linear expected size. The uniform exclusion of every larger block is essential to that interpretation and not obtained by counting singletons or fixed pairs alone. This provides a useful benchmark for comparing random partitions, not a claim of a new general Poisson approximation method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
