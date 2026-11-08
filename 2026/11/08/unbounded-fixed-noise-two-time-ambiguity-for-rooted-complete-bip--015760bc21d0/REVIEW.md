# Self-review

## Correctness — PASS

The proof derives the exact stationary equal-time pair-covariance equations for the *synchronous* fair-noise voter process. It establishes that opposite-part covariance is zero, solves the two within-part equations, and uses the complete-bipartite two-step kernel to obtain every temporal autocorrelation at the root. At refresh probability \(1/2\), the exact identity \((5a-4n-1)b=n(a-1)\) characterizes equality with the balanced graph's lag-two correlation. The proposed integer construction satisfies it identically. The lcm choice guarantees integrality and at least two vertices in each part; increasing larger part sizes guarantee nonisomorphism. The independent full-pair rational solver checks two small collisions and all lags through 12; the bundled checker printed `VERIFY_OK 560 exact-rational assertions`.

Scientific risk: computations are finite consistency checks; universality depends on the displayed algebraic and Markov arguments, which are fully included. The claim does not extend to nonstationary starting laws.

## Originality — PASS (priority qualified)

The closest primary source is Benjamini–Helman Tov–Zhukovskii, arXiv:2207.01224, Theorem 6.1 and Section 6. It already proves pairs of complete-bipartite structures that cannot be separated by any repetition-frequency statistic, for carefully selected noise levels; pairwise second-order nonidentifiability is therefore **prior work**. The reviewed new assertion is stronger and logically distinct: for *every* prescribed cardinality \(k\), one can produce a *single common* collision class containing \(k\) nonisomorphic rooted connected nonstar graphs while keeping the same fixed refresh rate \(1/2\). Prior pair-existence assertions do not imply unbounded simultaneous multiplicity or fixed-rate existence. The exact lcm construction establishes both. The source's four-time separation results are consistent with the stated two-time-only claim. Pymar–Rivera, arXiv:2112.01478, has a different update rule and global-density observables. Primary literature and indexed mathematical findings yielded no stronger implication.

Residual originality risks: natural number-theoretic parametrization might be known outside indexed literature; a negative search is not proof of priority. The original paper supplies the covariance framework; no novelty is attributed to it.

## Value — PASS

The result proves a qualitative, unbounded ambiguity phenomenon, not merely another isolated pair or a narrow numerical table. Even infinite-precision access to *every* two-time statistic at a known ordinary noise level cannot limit candidate rooted complete bipartite graph structures to any universal finite count. This gives a motivated boundary for local graph reconstruction and underscores why higher-order observations are mathematically necessary in some settings. No full-stream indistinguishability or finite-sample estimator is asserted.

Self-review: passed. Independent audit: not yet performed.
