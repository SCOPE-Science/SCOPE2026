# Scientific review: random cylinder-sidewall metric stretch

## Correctness

**PASS.** The geometric model distinguishes the intrinsic shortest path on the uncapped sidewall from the ambient chord. Equation (4) follows from a flat covering strip and independent uniform angular coordinates and triangular axial differences. The threshold inequality is algebraically equivalent to the exact exceedance condition. The sharp maximum follows from the monotonic circular arc/chord ratio. The upper-tail coefficient is the exact area of a parabolic sublevel set multiplied by the limiting joint sampling density. The thin-height critical profile follows from the same local form, with the triangular density retained rather than replaced by its endpoint value. The conditional Dirichlet law follows from the explicit Jacobian. The reported finite numerical tests were replayed from `verify.py` and do not replace the analytic proof.

## Originality

**PASS, subject to historical-priority risk.** The published finite-cylinder intrinsic-distance result treats only the law of \(d_g\); the separate published Euclidean-cylinder moment result treats only ambient \(d_e\) moments. Their marginals do not determine the coupled ratio. All-power intrinsic-moment optimization and invariant random-line chord studies likewise have distinct statistics. The 2005 cylindrical parameterization paper and the 2010 periodic-surface geodesics preprint provide geometric context but not random stretch tails. Searches for cylinder geodesic/chord ratios, aliases, critical heights, and metric embedding distortion did not surface an equivalent statement. This is a scoped priority assessment, not proof of universal novelty.

## Value

**PASS.** The statistic measures the embedding distortion of one of the simplest noncompact-with-boundary flat surface models while retaining its actual three-dimensional embedding. The unexpected shift between exponents \(3/2\) and \(1\), its explicitly nonsmooth crossover, the conditional parabolic/Dirichlet geometry, and one-threshold inverse aspect recovery make the statement more than a textbook cylinder-unrolling calculation or a routine moment increment. It provides a benchmark for geometric distance distortion under collapsing dimensions.

## Boundaries and residual risks

The full exceedance CDF is an exact one-dimensional integral rather than a general elementary closed form. The asymptotic does not cover capped-cylinder paths, nonuniform point distributions, or an unbounded critical parameter. No independent mathematical audit has been conducted, and some older or non-indexed work might imply the result. The 2005 proceedings document is earlier than the precisely timestamped archival seed but its exact first public calendar day could not be verified.

Self-review: passed. Independent audit: not yet performed.
