# Scientific review: sharp two-step oscillation coefficient of Bernstein–Kantorovich averaging

## Correctness — PASS

The exact norm identity follows from the finite Markov cell decomposition, total positivity of the binomial kernel and its binwise integral, preservation of ordered tails, and the endpoint overlap identity. The maximizing upper-half cell indicator establishes attainability. The parity formulas follow by reflection and single crossing. The integral substitution and elementary upper-tail ratio bound give both stated first-order asymptotics. The accompanying exact-rational checker verifies transition masses, normalization and endpoint overlap for degrees 1 through 14; it is supplemental evidence, not an infinite proof.

## Originality — PASS, with stated priority risk

The nearest documented results address distinct norms or different operators. Cooper–Waldron (2000), Section 7, compute Kantorovich eigenstructure, not the two-step oscillation norm. Czudek (2016), Theorem 2, establishes single-input generalized-variation contraction, without the sharp second-iterate oscillation coefficient. Heilmann–Raşa (2016 online), Theorem 1 and Example 1, describe qualitative iterates and derivative-based convergence, not the total-variation overlap between their endpoint transition distributions. The sharp one-step Bernstein–Durrmeyer oscillation result concerns another integral kernel and does not imply this super-exponentially small *two-step* Kantorovich overlap. The claimed novelty is the exact coefficient, extremizing input and parity-resolved super-exponential asymptotic, not general total positivity or the known eigenstructure.

Relevant comparison material: Czudek https://arxiv.org/abs/1609.00973; Cooper–Waldron https://doi.org/10.1006/jath.2000.3464; Heilmann–Raşa https://doi.org/10.1007/s11117-016-0441-1; Kivinukk–Metsmägi https://doi.org/10.3176/proc.2011.4.01. The original full text of Kivinukk–Metsmägi (2011) was inspected: Theorems 1–2 give variation-approximation estimates for smooth data, not the sharp two-step oscillation coefficient. A historically unindexed equivalent calculation remains possible. Independent publication-priority validation has not been undertaken.

## Mathematical value — PASS

The oscillation seminorm is the worst-case deviation between two output evaluations of a Markov averaging operator. Determining the first genuinely contracting power and its *exact* contraction deficit is a natural stability and mixing problem. The result sharply contrasts one-step noncontraction and strict two-step contraction, explains the extremely slow worst-case onset of mixing as degree grows, and supplies explicit finite rational benchmarks with an all-degree asymptotic. It is not merely a variation-diminishing inequality or a generic spectral estimate.

## Scope and residual limits

Real bounded measurable functions on one unit interval, the classical unweighted Bernstein–Kantorovich formula, and exactly two applications. The result does not calculate norms for later powers, nonuniform cells or weighted kernels. Numerical checks of finite degrees and point grids are not substitutes for the analytical total-positivity and asymptotic arguments.

Self-review: passed. Independent audit: not yet performed.
