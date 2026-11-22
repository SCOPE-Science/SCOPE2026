# Review of stationary transposition descent fluctuations

## Correctness

**PASS.** The cyclic comparison coefficient is divergence-free and therefore a pointwise eigenfunction of uniform transposition averaging with eigenvalue \((n-5)/(n-1)\). The stationary cyclic variance is exactly \(n/12\); hence the average one-step squared change is \(2n/[3(n-1)]\). The key nonstandard estimate is that changing one underlying independent rank input affects at most \(3(n-1)\) swap increments in the averaged squared-jump function, giving Efron–Stein variance at most \(4608/n\). This proves deterministic predictable-bracket convergence. Bounded martingale jumps and the one-dependent initial CLT yield the functional OU limit. The ordinary-count difference is uniformly at most \(1/(2\sqrt n)\). Independent exact enumeration confirms the finite identities through seven positions. Unproved extensions and the finite-check limitation are stated in RESULT.md.

## Originality

**PASS, with historical-priority uncertainty.** Hultman's identity-start descent expectation identifies two eigenvalues but not stationary temporal fluctuation processes. Garet's descent CLT concerns a size-growing insertion chain. The existing published comparison-vector covariance result only supplies a static second-order decomposition; the published exchangeable partial-permutation shuffle spectrum concerns a different transition kernel; the random-to-top Gaussian theorem uses another shuffle. Querying the relevant published records and primary literature found no functional OU limit for this precise stationary cyclic/ordinary descent pair. This search does not establish absolute priority, and a more general stochastic-process theorem might encompass the claim.

## Value

**PASS.** A natural rapidly changing ranking statistic that is generally not a closed Markovian projection has an explicit, universal stationary Gaussian Markov process limit. The result supplies the temporal covariance, relaxation rate and diffusion coefficient, going strictly beyond one-time descent CLTs or finite expected counts. It also identifies a concrete cyclic eigenfunction and proves concentration of its microscopic quadratic variation, a mechanism suitable for further local-pattern fluctuation analysis. Neither numerical simulation nor the formal existence of a generator alone justifies this value claim.

## Closest literature and limits

The closest read sources are Hultman, arXiv:1301.0430v1, and Garet, arXiv:1906.02980, together with the published comparison-incidence and shuffle-spectrum records linked in RESULT.md. The result is restricted to uniform stationary starting rankings, uniform distinct-position transpositions, and fixed finite \(n\)-scaled time windows. Any broader prior functional theorem remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
