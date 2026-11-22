# Scientific review: minmod reconstruction variation

## Correctness — PASS

The exact distributional variation counts both cell interiors and interfaces; cancellation proves one-input variation preservation for all real arrays and every \(0\le\lambda\le1\). A secant of the minmod median has nonnegative two-gradient coefficients summing to at most one. Step-vector decomposition bounds the difference-variation norm by one plus \(\lambda\) times at most two adjacent slope coefficients. Actual nondegenerate finite input pairs attain each dimension-dependent upper bound. Rational checks independently corroborate the formulas. The theorem does not rely on finite enumeration to establish a statement for all dimensions.

## Originality — PASS, with residual historical-priority risk

The principal source Dubois (arXiv:1006.3921v1, full text Sections 2 and 6) treats nonlinear interpolation, minmod, and variation-diminishing schemes, not the exact two-input variation of the reconstructed-function difference. Harten's 1982 full report examines TVNI time evolution and \(\ell^1\) contraction, neither equivalent to the present BV seminorm bound on reconstruction outputs. The closest full published three-point median-filter theorem bounds a median of sample levels, not a minmod median of adjacent differences followed by a piecewise-linear reconstruction. A shared numerical factor at full slope is insufficient for implication or coverage. Older lesser-indexed nonlinear interpolation literature may contain equivalent special cases.

## Mathematical value — PASS

The sharp parameter law determines how variation-preserving reconstruction responds to perturbations, which the standard individual-signal TVD statement cannot control. It distinguishes no expansion with two cells, first expansion with three, and the full factor with four; it provides an attained coefficient for every slope-scaling strength. These are structural robustness facts about a fundamental conservative reconstruction rather than arbitrary table entries.

## Limitations

Real uniform-cell signals, zero endpoint slopes, minmod of nearest differences, scaling parameter in the closed unit interval, and total variation including all internal jumps. No claim for arbitrary mesh weights, larger stencils, or finite-volume time updates. Historical priority remains qualified; independent scientific audit is not performed.

Self-review: passed. Independent audit: not yet performed.
