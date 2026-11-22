# Scientific review: exact record dynamics of planar random-section optimization

## Correctness — PASS

The boundary chord reflection is obtained by solving a quadratic intersection equation and its angle-doubling identity. Conditional angular uniformity holds **for every current boundary point**, which proves independence of all chord proposals even when the iterates themselves depend on earlier directions. The exact minimum-law CDF, moment integral, first-passage distribution, conditional drift, and record-indicator law follow without approximation. The \(N^{-2}\) mean constant uses a stated exponential dominating bound; dyadic Borel--Cantelli and a Bernoulli concentration argument support the two almost-sure limits. The standalone diagnostic checker passes geometry, combinatorial record, integral-consistency, and asymptotic checks. No finite experiment substitutes for these analytic arguments.

## Originality — PASS, with historical-priority uncertainty

The leading 2026 preprint [1] analyzes independently sampled random affine sections and gives general expected/high-probability guarantees, but not an exact *full-step, one-dimensional planar linear-objective* process. The strongest directly related published result [3] already proves that the sharp worst-direction expected one-dimensional section-oracle fraction is zero. That established zero infimum is not presented as novel here. Its all-dimensional one-step norm comparison does not determine a complete trajectory law, the uniform conditional chord coupling, \(\pi^2\) mean constant, geometric hitting-time law, or the accepted-move record process. Older Random Pursuit [2] instead solves unconstrained one-dimensional searches. Classical record identities are acknowledged as known after the algorithm-to-record coupling. Search-index coverage is incomplete and an unidentified identical full-step disk model could predate this presentation.

## Value — PASS

The exact natural boundary model solves a genuine performance question at the one-dimensional section size where uniform oracle-efficiency guarantees vanish: it gives finite-sample confidence, the sharp \(N^{-2}\) expected objective rate, the precise \(\varepsilon^{-1/2}\) query complexity constant, an almost-sure rate, and the logarithmic number of accepted updates. This highlights why a zero uniform one-step progress coefficient does not imply slow realized sample-path convergence, while explicitly distinguishing the full-step linear problem from the source's damped method. The law is a tractable algorithmic benchmark, not a claim to general faster convergence.

## Closest literature and limits

[1] Poirion, Pokutta, Takeda, *Random-Subspace Frank--Wolfe over Strongly Convex Sets*, arXiv:2605.24819v1 (2026-05-24), complete preprint text reviewed for algorithm, assumptions and Section 3 bounds.

[2] Stich, Müller, Gärtner, *Optimization of Convex Functions with Random Pursuit*, arXiv:1111.0194, preprint Introduction and line-search algorithm read.

[3] *Exact Haar-section efficiency and the two-dimensional Frank--Wolfe threshold*, 2026-10-13, publicly available RESULT.md and complete proof at https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-exact-haar-section-efficiency-and-the-two-dimensional-frank-wolf--4928d0ff7055/RESULT.md . The zero uniform one-dimensional efficiency constant is already covered there.

**Scope:** Exact arithmetic, unit disk, nonconstant affine objective, boundary start, independent Haar directions and exact full steps. No extension to damped schedules, nonlinear objectives, other shapes or higher dimensions is proved.

Self-review: passed. Independent audit: not yet performed.
