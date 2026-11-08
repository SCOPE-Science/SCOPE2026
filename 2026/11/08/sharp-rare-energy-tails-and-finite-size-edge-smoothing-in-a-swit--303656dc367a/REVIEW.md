# Review of sharp rare-energy tails in a switching harmonic gas

## Correctness — PASS

The assumptions identify a unique stationary Gaussian scale-mixture distribution for the two-rate Markov-switching Ornstein–Uhlenbeck gas. The proof reconstructs its size-biased beta variance law from the stationary phase-flux equations, computes the exact conditional chi-square density, and applies Stirling's formula, one-sided Watson asymptotics, and a Gaussian endpoint scaling. The normalization is the size-biased one, not an ordinary beta law. All rates and edge exponents have their correct directional dependence: the lower edge uses \(p=r_1/(2\mu_1)\), the upper edge \(q=r_2/(2\mu_2)\). The compact-support LDP and one-sided tail probabilities are deduced from the same rate function with explicit boundary slopes. The standalone diagnostic checker supplies independent finite-parameter corroboration; the analytical derivation is essential and does not rest on numerical sampling.

## Originality — PASS, qualified

[1] already proves the full stationary conditional-Gaussian mixture for this **same** switching trap, including extreme/order statistics, the limiting full-counting distribution, and the \(p=1\), \(q=1\) edge-divergence transitions of the *order statistics* (supplementary Eq. (S80)). [2] proves the general conditional-i.i.d. limit for a rescaled sum, implying the interior weak limit for particle squared positions. Neither inspected primary text or its inspected appendix states the new sharp exponential rare-tail law with two switching-sensitive powers of \(N\), the fixed-energy threshold probabilities, or the two complete \(N^{-1/2}\) Gaussian-convolution endpoint profiles for the quadratic-energy statistic. These are genuine asymptotic consequences of the old integral representation, not independent new microscopic dynamics. Search alone cannot establish uniqueness; an unindexed broader Gaussian-scale-mixture saddle theorem could imply the result and remains a documented risk.

## Mathematical value — PASS

The exact long-run stationary joint law leaves open how improbable collective energy measurements behave for large particle number, particularly outside the finite interval of limiting energies where ordinary limit theorems carry no quantitative information. The computed large-deviation rate and sharp polynomial prefactors permit rare-event probability calibration. The two distinct endpoint profiles classify divergent, bounded, and vanishing energy-density peaks at physically meaningful switching thresholds. Their exponents make the two switching intensities separately recoverable from finite-size rare-energy tails even when the exponential rate does not distinguish those intensities. This is more than a direct rephrasing of a weak-limit theorem or a textbook moment calculation.

## Closest literature and limitations

[1] M. Biroli, M. Kulkarni, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570. Inspected main text (stationary integral Eq. (12), weight Eq. (13), extremes) and supplementary asymptotics/counting analysis. The authors provide the starting mixing law, so it is credited, not claimed original.

[2] M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Exact extreme, order and sum statistics in a class of strongly correlated system*, arXiv:2307.15351. Inspected the actual conditional-i.i.d. sum theorem, its proof appendix, and nearby order-statistics formulas. It supplies the generic interior sum limit, not these rare-energy edge constants or sharp out-of-support prefactors.

The asymptotics hold at fixed positive system parameters and fixed positive measurement energy except where the stated \(N^{-1/2}\) edge scaling applies. There is no uniform double-scaling theorem, no temporal-trajectory large-deviation result, and no independent mathematical review.

Self-review: passed. Independent audit: not yet performed.
