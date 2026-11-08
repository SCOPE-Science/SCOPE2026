# Scientific review

## Correctness — PASS

The two-sided stationary reset-Brownian process and its stable linear harmonic filter have finite fourth moments. The Markov generator yields a degree-four stationary recurrence and the exact closed triangular ODE for the three connected polynomial observables. Direct variation of constants produces the entire lag kernel; positivity follows from three positive rational initial covariances and ordered positive exponential convolutions. The large-lag trichotomy follows from strict spectral ordering, with a separately evaluated repeated-rate case and a compact-uniform critical boundary-layer argument. The embedded Python checker independently verifies exact rational moments, differential equations, and selected finite/asymptotic instances. Its finite tests do not certify universal limits; the derivation provides those limits.

## Originality — PASS (with residual priority risk)

The closest primary source, Guéneau–Majumdar–Schehr (arXiv:2306.09453, Sections 4–5 and Appendices E–H), gives one-time moments and linear two-time covariance, rather than the connected mixed-time fourth moment and its exact rate transition. Majumdar–Oshanin (arXiv:1806.03435) concerns reset-noise spectra and Shee (arXiv:2409.06920) concerns a distinct full-state resetting mechanism and one-time moment evolution. A prior exact integrated quadratic covariance would not by itself imply the complete positive lag law or the sharp rate switch. Searches for aliases (squared position, intensity/energy covariance, quartic two-time, reset Brownian forcing), broader semigroup coverage, and exact table forms identified no statement implying this full theorem. Generic polynomial-semigroup methods could yield the result upon fresh calculation; that is acknowledged. Unindexed or implicit stronger results remain possible, and no global uniqueness claim is made.

## Mathematical value — PASS

Quadratic position is proportional to the trap's potential energy, so its stationary temporal correlation is a natural observable of active noise memory. The explicit all-parameter formula reveals a nontrivial change in the dominant relaxation mode at \(r=2\mu\), different from the familiar linear-response crossover, and resolves the collision into a universal uniform boundary layer. Its exact positivity and leading amplitudes are useful for comparing energy-relaxation measurements and numerical approximations. This is not merely a named special value or a recomputation of one-time moments.

## Scope and risk

Scientific interpretation presumes the stated noise normalization, stationary observation, and positive parameters. The general generator approach itself is established; publication priority of the particular full lag-and-critical theorem awaits independent confirmation. Neither numerical checks nor searches certify novelty on their own.

Self-review: passed. Independent audit: not yet performed.
