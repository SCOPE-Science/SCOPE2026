# Scientific review of the positive-lag Pascal-column covariance density

## Correctness — PASS

The prime-power Kummer reduction makes the binomial column a repeated integer valuation sequence. Two-point moments follow from compatible prime-power congruences, yielding the exact covariance with the correct carry-over boundary weights. The strictly positive sign count handles the two disjoint adjacent integer multiples of \(p\); equality is eliminated by a valuation obstruction. Summing the exact frequencies of integer valuation strata establishes a natural density (the infinite-tail frequency tends to zero). The floor values stabilize past depth \(a\); replacing them by their real arguments produces the Lambert series with a rigorously bounded error of \(p^{-a-1}\). The checker passed all declared finite tests, which are corroborative only.

## Originality — PASS on the inspected literature, subject to priority risks

The exact two-point valuation formula is **already accessible from general simple-root joint-valuation intersection methods** and is not the originality claim. The final claim is the density of lag *signs* for every prime and every prime-power Pascal column, followed by a uniform depth limit. Snyder (2023, arXiv:2308.11718) characterizes local valuation trees, without providing the two-stage lag sign-frequency law. Spiegelhofer–Wallner (2016, arXiv:1604.07089) concerns valuation counts within Pascal rows. The relevant prime-power Pascal-column literature discusses one-point densities, not positive-lag sign densities. No equivalent all-parameter formula or stronger explicit lag-density theorem was found in the inspected sources. Unindexed literature and short unstated derivations from the existing local covariance theory are meaningful residual priority risks.

## Mathematical value — PASS

A fixed Pascal-column valuation sequence has unbounded spikes and nontrivial arithmetic long-range dependence. The sign of its lag covariance is a natural dynamical/arithmetic invariant that cannot be inferred from its one-point valuation histogram; the new result counts every positive shift, yields a finite exact formula instead of casework at selected lags, and quantifies a nontrivial high-depth limit by a convergent Lambert series. This is a complete two-parameter classification of an intrinsically defined arithmetic statistic, not a sample-size computation.

## Scope and limitations

All primes and all integer exponents \(a\ge1\) are included, and shifts are positive. The result concerns Cesàro index covariance followed by natural density in the shift variable, not finite-window Pearson correlations. Numerical tests do not replace the proof. The full earlier 2001 Barat–Grabner text was not available for inspection, and an equivalent result in broader digit-correlation literature remains possible.

Self-review: passed. Independent audit: not yet performed.
