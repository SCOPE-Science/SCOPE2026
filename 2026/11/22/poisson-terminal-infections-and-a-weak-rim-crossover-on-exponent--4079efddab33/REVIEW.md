# Independent mathematical audit

## correctness

PASS

Both the frozen and repaired mathematics handle the specified wheel, not a static percolation model. The exact target time is the minimum over independent spoke delays plus weighted rim distance. On the line, the exponential edge sums on the two disjoint rays are Poisson arrival epochs. The Laplace functional gives J_beta(t)=exp(-beta*t+(beta/alpha)(1-exp(-alpha*t))) per ray, and the root seed contributes exp(-alpha*t), giving the stated marginal. At R=ceil(log^2 n), omission of a successful path requires at least R consecutive rim steps by time t, with superpolynomially small probability since beta_n*t=O(log n) in each window. For sites at distance at most 2R the two outward rays of length R in the complementary arc and the root seeds are disjoint; requiring protection from these independent sources bounds pair survival by exp(-2 alpha t)(J_beta(t)+epsilon_n)^2. Together with the 4R dependency degree this gives vanishing Chen–Stein pair terms O(R n^(-alpha/(alpha+2 beta))) at fixed beta and O(R/n) in the weak window, plus O(R/n) single-site terms. Substitution gives the means e^(-x) and e^(-x-2c/alpha). The zero-count event gives the completion cdf, with the signs of both Gumbel centering constants checked; the reverse implication is not asserted in the repair. The star boundary is an independent maximum, and in the supercritical weak regime the union bound at t=(log n-K)/alpha gives escape left since the expected survivor count tends to zero. The finite checker was inspected, not executed; the Poisson and Gumbel convergence are analytic.

## originality

PASS

The repair credits a materially stronger and closer source than the frozen comparison: the identical rim process is the two-sided discrete Bass circle, whose exact finite-circle marginal and survival identities are established. The infinite-line marginal follows from the known finite marginal recursion, so it is not credited as distinct. The surviving independent contribution is the Poisson law of the terminal survivor count and the resulting fixed-rate completion limit and weak-rim crossover. No inspected stronger theorem covered these joint and moving-window assertions.

## value

PASS

Mean diffusion on the same ring was already tractable, but the statistics of the last nonadopters depend on possible clustering. Proving a Poisson survivor law on the logarithmic time window resolves that issue for this geometry and identifies a sharp, natural weak-interaction scale and explicit completion-time shifts relative to the exact star boundary. This is more than renaming the model or rederiving its expected adoption curve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
