# Scientific review

## Correctness — PASS

The claim is for \(n\ge4\), two window orders at most \(\lfloor n/2\rfloor\), fully specified continuous nulls, and non-circular overlapping gaps. The exact statistic is \(2n^2D^{\mathsf T}A_rD/(N_r-1)\). The crucial nonstandard step is the exact quadratic-form fourth moment under the Dirichlet gap law: using independent exponential coordinates centered to variance one and fourth cumulant six yields the three traces with coefficients one, two and six. The long-run mixed covariance follows independently from the overlap-count sum and from normalization corrections. For fixed orders the finite-dependence CLT proves joint Gaussianity. The two-order asymptotic ratio profile takes the sample-size limit first; simultaneous window growth is deliberately excluded. An embedded standard-library checker passed 989 assertions, including exact monomial integration, exact matrix checks and independent simulation. No numerical check is used as an infinite proof.

## Originality — PASS with residual historical risk

The source statistic and marginal normal limit were already given by Singh and Misra (2021), and no novelty is assigned to these. The mixed-order covariance is a different observable: its two arguments are different window sizes evaluated on the same sample. Rao and Kuo (1984, pp. 229, 231, 233, 235) calculate asymptotic single-order efficiency and joint dependence between offset subsamples of a fixed order, but not the stated unwrapped mixed-order kernel. Guttorp–Lockhart (1989, Sections 1–2) give exact single-order moments and a circularized, rather than unwrapped, higher-order statistic. Mirakhmedov (2025, Sections 1–2) compares individual-order tests via asymptotic efficacy, not the covariance of tests on the same uniform sample. Searches of published mathematical-research records by overlapping-spacing statistics, aliases (generalized Greenwood / squared Gini), and mixed-order correlation did not reveal a dominating exact result. This absence is not a proof of novelty; earlier general Dirichlet quadratic-form calculations or less-indexed spacing literature remain possible routes and are residual risks.

## Value — PASS

The precise joint null dependence is needed when combining two spacing lengths into a multiscale uniformity diagnostic: treating their test statistics as independent can materially miscalibrate aggregated scores. The finite exact covariance gives an implementable calibration at moderate sample sizes; the universal profile \(\sqrt u(3-u)/2\) quantifies nontrivial redundancy at different resolutions, approaching zero for well-separated scales and one for matched scales. This is a natural parameter-dependent classification motivated by the original goodness-of-fit family, not an arbitrary numerical sample or a renaming of a known table. No exact multiscale critical values or improvements in power are claimed.

## Restrictions and sources

Primary source: Singh–Misra (2021), https://arxiv.org/abs/2110.10737, original equations (5)–(6), Theorem 1 and optimality theorem. Closest additional papers: Rao–Kuo (1984), https://doi.org/10.1111/j.2517-6161.1984.tb01292.x; Guttorp–Lockhart (1989), https://www.sfu.ca/~lockhart/Research/Papers/GuttorpLockhartCJS89.pdf; and Mirakhmedov (2025), https://arxiv.org/abs/2508.18965. Residual limitations include potential unlocated equivalent general quadratic-form formulations and no simultaneous growing-window limit.

Self-review: passed. Independent audit: not yet performed.
