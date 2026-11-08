# Scientific review

## Correctness — PASS

For a stationary symmetric rate-\(\gamma\) telegraph forcing shared by the two stable unit-gain filters, the generator recurrence is triangular in total polynomial degree and determines every moment through degree four exactly. The fourth cumulant factorizes as a strictly positive prefactor times a quartic with positive constant and four strictly negative higher coefficients, so the positive sign, unique zero, and negative sign are proved globally for all unequal positive relaxation rates. Stationary existence and all needed moment bounds follow directly from the causal exponential convolutions. `check.py` independently reproduces the exact factorization and solves eight full rational moment systems. The checks support the proof but do not replace it.

## Originality — PASS with residual risk

Inspected full texts arXiv:2210.09035 and arXiv:2207.10445 discuss telegraph-driven harmonic systems and higher moments, but do not present the unequal-rate, same-drive **difference** and its unique quartic crossover. The established all-nonnegative-response fourth-cumulant sign result is stronger for positive observables yet does not imply the sign of the signed difference, whose response kernel changes sign. Targeted searches for common telegraph forcing, differential relaxation filters, kurtosis transition and equivalent formulations did not return the same all-parameter sign classification. This is a best-knowledge originality judgment, not proof of absence from all literature; earlier general telegraph moment calculus could implicitly yield the rational formula.

## Value — PASS

The effect is a meaningful observable distinction: each individual harmonic response is strictly negatively kurtotic while subtracting the same two signals produces a strictly positively kurtotic contrast at slow switching. The exact boundary for all pairs of rates resolves whether a two-channel differential measurement can be interpreted using the componentwise negative-kurtosis rule. The limiting extreme-rate slope adds a parameter-free asymptotic diagnostic. This is not merely a recomputed marginal moment or an arbitrary finite numeric example.

## Closest literature and limitations

Sarkar, Santra and Basu, arXiv:2210.09035, compare non-Gaussian active and Gaussian colored boundary reservoirs in harmonic chains; Smith et al., arXiv:2207.10445, derive confined RTP laws and treat interacting particles with independent propulsion noises. Neither inspected source states the signed common-drive crossover. General sign-rigidity applies to nonnegative transfer kernels, whereas the contrasting kernel has opposite-signed lobes. The result concerns a particular difference of unit-gain overdamped filters and an equal-time fourth cumulant; it makes no statement about arbitrary filter shapes or finite-time moments. Broader published analysis may include this as an implicit special case.

Self-review: passed. Independent audit: not yet performed.
