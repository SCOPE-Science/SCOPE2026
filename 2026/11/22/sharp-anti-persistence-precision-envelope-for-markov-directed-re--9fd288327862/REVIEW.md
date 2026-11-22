# Review of the Markov-directed renewal transport result

## Correctness — PASS

The statement specifies bounded positive renewal durations, bounded nonnegative rewards, full independence between marks and the stationary two-state sign chain, and nonzero mean sign. Conditional variance gives a convergent covariance series. Bounded renewal overshoots and a stopped-martingale second-moment identity establish the unsigned reward variance rate; the Markov stationarity constraints give the exact minimizing eigenvalue and an attainable aperiodic optimizer. The exact-rational checker independently verifies finite-horizon sign moments, a random-duration tilted-kernel calculation, and the explicit precision comparison. No finite run is claimed to prove the infinite-time theorem.

## Originality — PASS (priority qualified)

Karimi–Jafarpour's 2026 formula explicitly takes i.i.d. signs; correlation within one run's rewards is a separate issue. The present theorem addresses *inter-cycle* directional correlation and adds an optimal fixed-marginal transition matrix. Shreshtha–Harris's 2019 renewal-reward framework, general Markov-renewal CLTs, and antithetic Markov-chain variance theory cover parts of the background, not a directly located statement of the complete sharp marked-cycle envelope and the marginal-boundary example. Published indexed results on independent-sign bias optimization and binary Markov occupation spectra are particularly close but concern different optimization variables and/or unit rewards. Full text for some general and early sources was not accessible; this remains a priority risk, not positive evidence of novelty.

## Value — PASS

Temporal directional memory can change current precision without changing the one-time directional law or the distribution of cycle lengths and rewards. The exact sharp envelope quantifies the maximal improvement achievable with one-step binary memory; the explicit bound failure identifies which independence condition is essential when interpreting marginal-sign precision constraints for run–rest or active-particle transport. This is a motivated and falsifiable model-boundary result rather than an arbitrary parameter exercise.

## Limits and verification status

The statement is limited to first-order two-state Markov signs, bounded cycle marks, and completion-time current. The stationary sign chain is reversible; marginal reversal-information is not equated with full dynamical entropy production. General Markov-additive variance methods are known, and related full texts require further priority checks.

Self-review: passed. Independent audit: not yet performed.
