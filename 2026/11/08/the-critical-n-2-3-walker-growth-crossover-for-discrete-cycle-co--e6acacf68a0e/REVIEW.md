# Scientific review

## Correctness — PASS

For the exact model of parallel independent simple symmetric walks started at vertex zero on \(C_n\), the union of lifted paths is an integer interval, so coverage at integer time \(t\) is precisely the two-sided range condition \(M_t^++M_t^-\ge n-1\). For one walk the reflection formula is exact. Stirling's binomial mass approximation plus a local geometric tail uniformly yields \(q_t(a)\sim\sqrt{2/\pi}\,(\sqrt t/a)e^{-tI(a/t)}\) when \(a/\sqrt t\to\infty\) and \(a/t\to0\). Expansion of \(I(u)=u^2/2+u^4/12+O(u^6)\) at \(\log k_n\asymp n^{2/3}\) produces \(\delta=8c^3/3\) in each directional Gumbel maximum. An exponentially small same-walk double excursion proves asymptotic independence. Exact inversion gives the stated \(2\delta=16c^3/3\) time shift. For larger sublinear \(\log k_n\), the positive quartic correction diverges and forces the uncorrected window rightward. The first-order bound is independently checked with fixed-relative-time binomial tails. No unproved moment convergence is asserted.

The standalone integer/rational verification script passed 3,242 exact reflection, path-range, and finite-cover-distribution comparisons. These are finite consistency checks and not substitutes for the full asymptotic argument. Limits require \(n\to\infty\), \(k_n\to\infty\); at criticality \(\log k_n/n^{2/3}\to c\in[0,\infty)\). The integer-time rounding errors vanish on the displayed scale.

## Originality — PASS, with priority qualifications

The strongest overlap is Majumdar–Sabhapandit–Schehr (arXiv:1609.06325, §§IV–V), where the periodic **Brownian** multiwalker span and its limiting two-Gumbel convolution are already treated. Kundu–Majumdar–Schehr (arXiv:1302.2452) supply the Brownian range distribution, including extreme-value structure. Neither of those continuum/iterated limits controls the joint discrete parameter regime \(\log k_n\asymp n^{2/3}\), where one walker makes exponentially rare excursions and a quartic Cramér-rate term changes the limiting location. The Brownian limiting shape is expressly attributed to that literature, not presented as an original discovery.

Rivera–Sauerwald–Sylvester (arXiv:2011.07893, first public November 16, 2020, §5.1) treat finite-cycle multiwalk cover time up to order of growth for \(k\le n\), rather than exponentially many synchronous walkers and their distribution. Alon et al. (arXiv:0705.0467) also give speedup bounds only. Kim–Lawley (arXiv:2310.07905) analyze a many-searcher limit at fixed network size in continuous time. Relevant published mathematical claims were searched using the exact cycle-walker crossover, quartic Cramér correction, joint limits, Gumbel convolution, and aliases; no source claiming the critical coefficient or sharp crossover was found. Priority still requires independent specialist verification, especially for unindexed finite-lattice rare-excursion asymptotics.

## Value — PASS

The discrete correction is not a rephrased continuum limit: for \(\log k_n\) below the critical \(n^{2/3}\) scale it vanishes, at that scale it survives as an explicit nonzero location shift, and above it the previously natural second-order normalization ceases to be tight. This identifies a sharp threshold for using a Brownian approximation to estimate extremely fast parallel coverage on finite cycles. It also supplies a complete non-Gumbel limiting CDF and exact coefficient for the critical boundary. The result answers a natural precision gap behind known order-of-growth cycle results, without a claim of a general theorem for all networks.

## Closest literature and residual limitations

Full or substantive sections were inspected from the relevant 2016 Brownian covering paper, the 2020 graph multiwalker study, the 2013 range paper, and the 2023 fixed-network many-searcher paper. The chief residual priority risk is an earlier unindexed uniform lattice moderate-deviation treatment already implying this crossover. The analytic proof uses a standard local Stirling/tail ratio estimate, derived in the result, whose asymptotic uniformity is limited to the specified regime. No independent audit has yet been performed.

Self-review: passed. Independent audit: not yet performed.
