# Scientific review

## Correctness
**PASS.** The conditional residual mean is zero, yielding an exact cross-moment identity and a closed two-by-two second-moment recursion after the first update. Exact symbolic expansion produces the three Schur–Jury expressions. Their signs prove the sufficient regime. In the excluded regime, positivity of the moment matrix and the first-step moment vector, together with Perron–Frobenius, proves failure of decay from the specified initialization, not just from an unspecified initial state. The deterministic \(p=1\) boundary and the memoryless reference are treated separately. The executable verifier replays symbolic identities and finite-prefix rational checks; only the analytic proof establishes the infinite-time result.

## Originality
**PASS with residual precedence risk.** The 2020 Horváth–Richtárik analysis directly motivates comparing error feedback with unbiased compression; that qualitative comparison is prior art. The 2025 and 2026 tight-analysis papers address optimized worst-case Lyapunov guarantees for contractive compressors, not the exact all-stepsize characterization of this specific amplified Bernoulli compressor, notably the region where its squared relative compression error is at least one. The closest published Bernoulli error-feedback classification is for the distinct biased, unamplified operator and has a different threshold. Targeted record and literature searches found no earlier explicit statement of the half-retention impossibility frontier, but an earlier specialist equivalence remains possible.

## Value
**PASS.** The result exactly separates the safe and unsafe regions of a canonical, practically motivated unbiased dropout operator under classical residual compensation. The half-retention threshold means that below a concrete compression density, *no fixed learning rate* rescues mean-square convergence, whereas removing the memory restores a nontrivial stable range. This is an exact algorithm-design boundary with a natural uncompressed comparator, rather than an arbitrary numeric example or merely a check that a known sufficient bound fails.

## Limitations
The claim covers a scalar homogeneous quadratic with exact gradients, independent identically distributed compressor calls and fixed stepsize. It does not establish instability for every compressor or other error-feedback algorithm. Independent validation and a comprehensive scholarly precedence review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
