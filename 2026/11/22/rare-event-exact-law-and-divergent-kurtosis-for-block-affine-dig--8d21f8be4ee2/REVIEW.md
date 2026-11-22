# Self-review

## Correctness — PASS

Theorem quantifiers explicitly require integers \(e\ge2\), \(m\ge1\), \(N=2^{em}\), a full dyadic input grid, a common infinite block-affine binary scramble with independent unrestricted off-diagonal rows and shifts, and \(f(x)=x\). The proof directly derives the independent rare-event digit law by uniformity of random binary linear functionals and complete prefix cancellation. Independently summing second/fourth moments gives exact rational constants; geometric activation waiting times plus a uniform deterministic dyadic tail bound prove the exponential logarithmic law. For the comparator, independent nested-permutation subtrees give iid uniform stratification jitter. The standalone exact-rational program passed 96 assertions. Computation does not establish the infinite limiting statements, which follow analytically.

## Originality — PASS (historical priority qualified)

Suzuki's primary paper defines block-affine scrambling and proves gain-coefficient and variance results; it does not state the exact independent-activation series, \(3(N+2)/5\) kurtosis, or exponential logarithmic error scale. Liu's accessible preprint reports heavy-tailed empirical affine-scramble errors and explicitly highlights formal analysis as an open problem, but qualitative rare-event phenomena are acknowledged as prior work, not relabeled as novel. Yue–Hickernell's gain formulas address second moments. Mathematical-record queries for block-affine, linear, one-dimensional Bernoulli-digit laws and kurtosis returned no equivalent claim; closest indexed records concern other quadrature randomizations and their different stochastic structures. Unindexed exact calculations and historical special cases remain risks, so this is not a certified priority determination.

## Value — PASS

One-dimensional integration of the coordinate function is a natural calibration benchmark for randomized digital-net quadrature. The exact calculation reveals a high-impact statistical limitation invisible to the identical mean-square errors: affine and fully nested scrambling have diverging versus bounded kurtosis and exponentially small typical versus asymptotically normal RMS-scaled errors. These distinctions matter to interpretation of replicated randomization error and to benchmarking randomization methods, without claiming one method wins on every loss or function.

## Scope and verification limits

Only the explicitly stated one-dimensional complete-grid case is classified. The result assumes infinitely randomized suffix bits and does not quantify an implementable finite-precision law, replication requirements, or higher-dimensional performance. The source literature includes a subsequently withdrawn preprint, used solely for contextual comparison. The mathematical proof is self-reviewed only; no independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
