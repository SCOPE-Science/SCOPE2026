# Review of the entropy-rate dichotomy

## Correctness

PASS. The doubling map sends binary digits to the left shift under Lebesgue measure. Joint entropy of finite GF(2)-linear forms of unbiased independent bits equals their row rank. The two-protocol classification follows from the rank of two polynomial generators over the even-shift ring versus the one-generator span for repeated-per-state sampling. Degenerate cases have a bounded-degree syzygy, supplying a uniform \(N+O(1)\) rank estimate, not merely a computation. Both explicitly pairwise-independent examples have proved exact finite-block entropies. The included exact-rank program provides independent finite consistency checks of the claimed algebra, without replacing the proof.

## Originality

PASS within the inspected literature and indexed descriptions. The 2024 source derives autocorrelations for the identical two sampling schedules, not exact Shannon entropy, finite-filter determinant/square criteria, or hidden triple-XOR dependencies. The 2019 paper treats single Walsh observation streams and cross-orthogonality, not their alternating joint entropy. The 2021 paper treats correlations of combined multi-bit outputs, not the two-protocol parity-alternation dichotomy. The nearest indexed descriptions involve binary observation statistics or different dynamical maps and do not imply the claimed classification. A general polyphase-filter/linear-code formulation could subsume the proof and remains an explicit priority risk.

## Mathematical value

PASS. The criterion is a complete yes/no classification for all finite parity sensor pairs, not a selected numerical example. It exposes an exact loss of half the output entropy that cannot be detected by *any* pairwise-correlation test, even when each constituent stream is individually iid; the contrast between the two sampling schedules is mathematically intrinsic to their information flow. The explicit polynomial test and sharp finite-block examples are directly useful when choosing observables for statistical experiments on chaotic maps. No claims of cryptographic strength are made.

## Boundaries of the assessment

The result assumes nonzero finite GF(2) parity observables and Lebesgue initial data. General nonlinear sensors, biased digits, and finite-precision implementations are outside scope. Known general entropy and polyphase rank principles provide ingredients; equivalence of this precise classification to uninspected versions is an unresolved bibliographic risk. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
