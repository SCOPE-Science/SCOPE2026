# Review of nonanalytic weak-return mobility on a random comb

## Correctness — PASS

The finite-tooth stationary balance recurrence has two positive characteristic roots, and its reflecting boundary yields the exact occupation ratio in the result. Summing the branch master equations gives uniform backbone occupancy and an exact finite-ring velocity, consistent with the source's stationary normalization. A bounded return-rate branch occupancy permits an ordinary quenched strong law; at zero return rate the positive infinite-mean strong law identifies the trapped regime. Shifting the geometric sum by the logarithmic cutoff gives a two-sided geometrically dominated series uniformly in the phase, and its nonzero first Fourier coefficient proves that the amplitude is not constant. At criticality, splitting the regularized series at its logarithmic cutoff yields the inverse-logarithmic coefficient. The standalone checker passed 36 assertions, including exact rational finite-volume stationarity. No finite experiment is treated as an infinite proof.

## Originality — PASS, with residual priority risk

The original Sarkar–Gupta paper (arXiv:2205.15232, first posted 2022-05-30) establishes the exact random-comb stationary distribution, speed identity and trap boundary and examines a fixed-length small-return expansion. Those known claims are excluded from the claimed contribution. Its full accessible main text and relevant supplement were compared to the present assertion; no uniform infinite-volume geometric-disorder weak-return scaling, log-periodic prefactor or critical inverse-log law was identified. Kotak–Barma (arXiv:2204.05357) investigates unreset comb transit-time fluctuations and does not introduce returns. A related comb-resetting article in *Entropy* 25 (2023), 1529, has a different CTRW-finger model; its complete text could not be retrieved and is a residual source-access risk. The precise theorem is not inferred novel merely from a failed indexed search. An unindexed equivalent asymptotic derivation remains possible.

## Mathematical value — PASS

At the natural trapping/transport threshold of a biased random comb, the exact speed is positive at every positive return rate but zero in the unreset thermodynamic limit. The theorem determines **how** this restored current vanishes: a continuum of fractional exponents and nontrivial lattice-scale modulation in the trapped regime, turning into an explicit inverse logarithm at criticality. This distinguishes fixed-tooth perturbation theory from an infinite disorder ensemble and makes the noncommuting limits of disorder averaging and weak regularization quantitative. The phase function cannot be replaced by an arbitrary fitted constant. This is a natural transport singularity, not an arbitrary finite-parameter computation.

## Closest literature and limits

- Sarkar and Gupta, arXiv:2205.15232; known exact finite-rate speed and stationary weight, but not the asserted nonuniform weak-return asymptotic.
- Kotak and Barma, arXiv:2204.05357; finite/infinite random-comb trapping and transit fluctuations without resetting.
- Masó-Puigdellosas, Sandev and Méndez, DOI 10.3390/e25111529; related comb resetting with nonidentical dynamics, abstract/excerpts accessible but complete text not retrieved.
- The zero-return and positive-return limits are ordered, and the integer-geometric assumption matters to the periodic amplitude. The numerical checker supports diagnostics only; independent scientific validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
