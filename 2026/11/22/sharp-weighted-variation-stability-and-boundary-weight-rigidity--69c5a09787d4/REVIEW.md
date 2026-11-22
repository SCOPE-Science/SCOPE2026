# Scientific review of the sharp midrange variation coefficient

## Correctness

**PASS.** Every local affine chamber is the half-sum of its minimum and maximum selectors, is constant-preserving, and hence has an exact induced weighted-variation norm determined by the images of single step perturbations. At each interior cut, the two mixed output values are independently constrained to \(\{0,1/2\}\) and \(\{1/2,1\}\), producing exactly four realized weighted variations; at each boundary, the half-jump may occur on either adjacent edge. Piecewise-affine integration proves the global bound for all pairs, and strict chamber witnesses prove equality. Contractive-weight rigidity follows directly from necessary neighboring-weight inequalities. The standalone finite-rational checker corroborates every combinatorial branch through eight vertices, but the all-size claim rests on the explicit analytical proof.

## Originality

**PASS with priority qualification.** The inspected full text of Schulze–Pearce's 1993 midrange paper develops bias correction and filtering behavior, not the two-input weighted variation norm. Anguelov–Rohwer's 2007 LULU study treats one-input variation preservation of different compositions. The closest public finite-window morphology theorem gives exact norms of erosion and dilation separately; those estimates do not imply the sharp coefficient for their average, and are strictly loose on the example with four vertices and variation weights \((1/2,1,1/2)\). The separate published median theorem is not a stronger or equivalent midrange statement. Earlier unindexed or inaccessible results might contain equivalent stability inequalities; this work does not assert exhaustive historical priority.

## Value

**PASS.** Exact two-input variation stability is useful for error propagation in nonlinear signal preprocessing, and cannot be read off from the familiar one-input variation-diminution of morphological operators. The sharp formula identifies the full admissible family of nonuniform variation weights, including a rigid constant-weight interior and an independent factor-of-two boundary taper. The structural cancellation is quantified by a natural counterpoint: constituent erosion and dilation maps are expansive under such tapering while their symmetric mean remains nonexpansive. The fact is complete for its natural radius-one setting and yields actual norming perturbations, rather than a numerically observed bound.

## Limitations and nearest literature

The result is limited to real finite paths with clipped endpoint windows and positive edge weights; it does not cover larger stencils, cyclic boundaries, general graphs, or statistical risk. The closest inspected papers are Schulze–Pearce (1993), Anguelov–Rohwer (2007), the public finite-window morphology result (2026), and the public three-point-median variation result (2026). Archival texts not exhaustively inspected and a year-only 1993 bibliographic date leave genuine historical-priority risk; no independent expert review has been performed.

Self-review: passed. Independent audit: not yet performed.
