# Scientific review: random Gaussian-mixture thermodynamic state for partial-batch resetting

## Correctness — PASS

A common two-sided Poisson clock supplies iid exponential backward gaps. The exact two-label inclusion/exclusion probabilities for uniform size-\(m_N\) reset batches prove \(L^2\) concentration of every fixed last-reset-age class at \(p(1-p)^j\); its unobserved tail is bounded in expectation by \((1-p_N)^{J+1}\). Conditioned on clock and subsets, independent Brownian increments give a conditional empirical law of large numbers. Single-label fourth and eighth moments control truncation of squared displacements, proving first- and second-moment convergence. Tonelli and exponential-sum independence prove the collective-energy transform and cumulants; the next-oldest-gap sum has a moment-generating function beyond the lead exponential rate, yielding the sharp right-tail constant. The standalone checker completed 7,499 algebraic and sampling assertions; finite tests are not treated as proof of an infinite statement.

## Originality — PASS, with explicit priority risks

The closest original paper (de Mauro–Majumdar–Schehr, arXiv:2601.20077, inspected in main and supplementary full text) already establishes the uniform-batch model, finite-particle Fourier recursion, exact pair correlations and large-population pair-covariance scaling. These known facts and the corresponding second-moment identity are not asserted as new. The present statement goes beyond them to a random *entire empirical-measure thermodynamic limit* and the *whole collective-energy distribution with a sharp upper-tail prefactor*. The Biroli–Larralde–Majumdar–Schehr and non-Poisson all-at-once-reset papers apply to the synchronous endpoint, not a fixed strict partial fraction. Indexed research and open-literature queries searched aliases for geometric Poisson ages, random empirical Gaussian mixture, and q-product energy tails; closest indexed items concern coupon reset times or unrelated invariant mixture laws. Search failure is not a proof of novelty. The strongest unresolved risk is a hidden implication in the original all-order Fourier recursion or an unindexed equivalent partial-batch law; a 2026 confinement paper could be assessed only from its abstract.

## Value — PASS

The object is a physically natural partial-fraction Brownian gas whose finite observables are known to be correlated. Determining the sample-dependent macroscopic density, all-order collective-energy law and sharp high-energy fluctuation frequency resolves an interpretable gap between two-point correlation theory and thermodynamic non-self-averaging. The result is not an arbitrary fixed parameter case, a known-table entry or a generic q-product identity presented alone.

## Scope and limitations

One-dimensional independent Brownian particles; Poisson batch clock; instantaneous uniform fixed-size batch resets; \(m_N/N\to p\in(0,1)\); fixed \(D,r>0\). No theorem about interactions, confinement, general renewal clocks, fixed batch sizes, phase transitions or dynamical relaxation. The work has not received an independent audit; source-equivalence risk remains.

Self-review: passed. Independent audit: not yet performed.
