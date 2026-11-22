# Research review: exponential founding-time marks for singular excursion extremes

## Correctness — PASS

The specified model's Itô entrance law gives the exact two-coordinate marked Poisson intensity. The normalized birth-time integral establishes the conditional mark law. The change of variables yields a locally uniformly convergent marked intensity and Poisson Laplace-functional convergence. A further exact bound on points born after a scaled time threshold controls escape of marks above any fixed height; rank tightness then justifies independent exponential founder marks for the leading positions. The asymptotic factor of two comes from \(u_t^2\sim(\log t)/2\). The finite diagnostic checks passed (see `checker.py` and `verification_output.txt`), but the analytical proof is needed for the infinite-time conclusions.

## Originality — PASS relative to inspected sources

Kou's first public version, arXiv:2611.19362v1, specifies this model and proves the **unmarked** maximum Gumbel distribution. Its theorem and full Sections 1, 2, and 5 do not supply a birth-time conditional distribution or a birth-time-marked point-process limit. The closest published genealogical marked-extreme result treats discrete critical geometric clans with polynomial immigration; another treats remote stationary tails under collective resetting. Neither statement implies the exact excursion kernel or its scaling. General Poisson mapping theorems are credited as proof tools. An implicit equivalent in older general excursion literature is a residual priority risk; search coverage is finite.

## Value — PASS

The additional time mark asks a natural genealogical question that an unmarked extremal spatial law cannot answer: when was a particle now at the top of a growing population born? The leading particle's birth time is atypically early by a sharp logarithmic fraction, while every fixed collection of leaders has independent limiting exponential birth-time marks independent of height rank. The exact finite-time regression and marked limit together explain the mechanism and allow conditional founder-time inference within this model.

## Boundaries and remaining checks

The result requires independent standard Brownian excursions attached to homogeneous Poisson immigration, a fixed positive intensity, and one large deterministic observation time. It does not claim multi-time limit theory, general offspring universality, or independent publication priority verification. Existing unmarked extrema and the fundamental Poisson marking theorem remain prior work, not independently new findings.

Self-review: passed. Independent audit: not yet performed.
