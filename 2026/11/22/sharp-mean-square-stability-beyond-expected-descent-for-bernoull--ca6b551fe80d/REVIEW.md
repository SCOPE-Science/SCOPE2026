# Scientific review

## Correctness — PASS
The exact two-dimensional permutation-invariant covariance transfer is algebraically derived and independently verified by complete Bernoulli-mask enumeration on small dimensions. The determinant, first crossing and no-reentry arguments establish a necessary and sufficient criterion for *every deterministic* initial error, including equality. The strict expected-descent separation and monotonicity are supported by exact identities. A standalone verifier checks 72 exact-rational covariance cases and 360 numerical spectral cases. The proof, not these finite checks, handles arbitrary dimensions and continuous parameters.

## Originality — PASS, with residual historical risk
Salzo and Villa (2019, arXiv:1906.07392) establish parallel block-coordinate convergence using sufficient smoothness/ESO conditions. Hanzely and Richtárik (2018, arXiv:1809.09354) treat minibatch coordinate updates with ESO-based rate bounds. Di Giovacchino, Higham and Zygalakis (2023, arXiv:2309.02082) give modified-SDE mean-square conditions for a single-coordinate scheme. The closest searched mathematical records concern averaged two-row Kaczmarz, fixed-size minibatch coupling, or deterministic weighted Jacobi. None of the checked statements proves the exact all-dimensional Bernoulli-mask threshold or its strict stable-but-nondescent gap. A generic covariance spectral-radius criterion is known and is not claimed. The historical search is not exhaustive and independent priority review is outstanding.

## Value — PASS
The independently activated synchronous coordinate method and equicorrelated quadratic form a natural parallel optimization benchmark. The theorem exactly locates the full all-starting-state stability region and shows when a method converges geometrically despite an initial expected objective increase—information unavailable from a one-step sufficient descent rule. The result does not cover unequal activation rates, arbitrary Hessians, memory or noise.

Self-review: passed. Independent audit: not yet performed.
