# Self-review

## Correctness — PASS

Strict convexity of the inverse-square spectral trace on the positive-definite disagreement space makes the unrestricted conductance allocation unique and automorphism-invariant. An eigenvalue decomposition gives exact reciprocal-moment formulas, and a one-sign-change cubic has a unique positive root defining the global solution. The asymptotic loss follows from controlled positive-root scaling and direct term expansion. A self-contained standard-library verifier checks 60 exact-rational/numerical assertions. Risks: finite checks do not prove universal formulas; normalized noise/gain constants are excluded from the reported trace ratio and cancel in comparison.

## Originality — PASS on inspected sources; residual priority risk

The unrestricted tree first-order optimizer is expressly **prior**: Ghosh–Boyd–Saberi (2008, Section 5.1). Lin (2021, Theorem 5.1) already covers the *unweighted* biharmonic index on double stars. Patterson–Bamieh (2013) supplies both coherence definitions and investigates different graph asymptotics. Summers et al. (2014) instead select new edges for first-order coherence. Indexed related work addresses second-order **stars** and double-star **spectral-gap** design, neither of which implies the independently optimized inverse-square-trace double-star bridge allocation or the 5/4 first-versus-second-order regret. Search is not a mathematical proof of novelty; unindexed equivalents remain a risk.

## Value — PASS

The second-order optimal noise-robust edge budget is qualitatively different from a fully solved first-order benchmark, with distinct bridge-budget exponents and a nonvanishing asymptotic 25 percent performance loss. The network is a minimal two-community tree bottleneck, and the result supplies a reproducible all-size exact benchmark for coherence-oriented budget design. This is not a generic graph design algorithm, nor a guarantee under other noise models.

Self-review: passed. Independent audit: not yet performed.
