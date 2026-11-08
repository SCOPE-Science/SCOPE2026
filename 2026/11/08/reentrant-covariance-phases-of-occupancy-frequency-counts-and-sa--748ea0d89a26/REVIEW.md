# Scientific review: reentrant occupancy-frequency/collision covariance

## Correctness — PASS

The object is a fixed-size sample of independent uniform box choices. For every integer \(m,n\ge2\) and \(0\le r\le n\), conditioning on a specified box's occupancy gives a binomial probability and an exact expectation for the remaining pair collisions. Summing over the \(m\) labeled boxes gives the claimed covariance quadratic. Its positive leading coefficient and discriminants in the frequency and sample-size variables establish the two separate phase diagrams. The conservation identity \(\sum_r F_r=m\) forces an actually occupied negative-covariance integer frequency; endpoint positivity alone would not establish this. The singleton factorization, the high-sample limit, and the infinite integral-root family follow by explicit arithmetic. The included checker independently enumerates uniform allocations and passes 174,349 exact assertions. Computational checks are supplementary, not a substitute for the universal proof.

## Originality — PASS, with historical-priority limitations

The most relevant primary sources are Gnedin, Hansen and Pitman (2007), Barbour and Gnedin (2008), Barbour (2009), and Källberg, Leonenko and Seleznjev (2011). The sections examined establish frequency counts, general moment methods, limiting distributions and collision estimators, rather than the finite \(\operatorname{Cov}(F_r,C)\) two-wing sign theorem and reentrant sample-size thresholds. A public 2026 result determines \(\operatorname{Cov}(K,F_r)\) and its one-switch spectrum; another gives \(\operatorname{Cov}(K,\widehat G)\), a factor explicitly used in the new singleton identity. Neither result states or implies the individual \(F_r\)-collision covariance from its own displayed relationship alone. More general classical occupancy moment machinery can recover the underlying raw covariance, so novelty is restricted to the exact sign and zero classification, its reentrant regime and the infinite double-orthogonality family. The Kolchin–Sevastyanov–Chistyakov monograph was identifiable bibliographically but its full treatment was not accessible; an unlocated equivalent remains a risk.

## Value — PASS

The size-frequency spectrum and unbiased pair-collision statistic are standard, independently motivated summaries of a categorical sample. The two-wing sign shape gives a complete finite-sample dependence classification rather than a single isolated covariance. The sample-size phase gives a qualitative reentrance for every positive fixed frequency above one, with an exact arithmetic zero set, and distinguishes the singleton Good–Turing component from total richness at the particularly natural sampling ratio \(n/m=2\). These facts address whether frequency-based coverage estimates and pair-based concentration move in the same direction under the simplest multinomial null. The results do not assert stronger dependence or heterogeneous sampling, and historical priority is not independently certified.

## Literature and scope limits

Primary identifiers: arXiv:math/0701718, arXiv:0809.4387, arXiv:0902.0879, arXiv:1103.4977. Relevant public research records: `SCOPE-20261004-93dddb2be813` and `SCOPE-20261004-e84114bd4ba0`. Older general urn-moment references may encode the quadratic implicitly; exact priority remains subject to further review. All scientific statements are conditional on independent equal-probability allocation.

Self-review: passed. Independent audit: not yet performed.
