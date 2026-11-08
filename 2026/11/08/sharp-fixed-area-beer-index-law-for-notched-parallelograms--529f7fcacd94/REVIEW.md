# Mathematical review

## Correctness

**PASS.** The zero-area boundary conventions are immaterial. An affine map reduces the problem to the unit square. Nonvisibility is possible only between two nonoverlapping arms, where the exact segment criterion is a product inequality in four independent uniform variables. Convolution of gamma densities yields the closed expression. Strict monotonicity proves the fixed-area equality case, strict concavity proves the optimal global stability coefficient, and the positive-area central rectangle proves the strict one-half bound. A standard-library numerical checker independently simulates area-uniform pairs using segment-rectangle clipping and compares the formulas across six configurations, followed by fixed-area optimization tests.

## Originality

**PASS, provisionally.** The source literature provides Beer-index theory and algorithms for polygonal visibility and invariant-line chord statistics. Generic closed-form evaluation is explicitly prior art. The claimed fixed-area extremal theorem and its sharp rigidity coefficient are neither stated in the inspected mathematical sources nor found in the searches made; a mere algorithm to compute each instance does not prove a continuum extremum. Circular-hole and slit-barrier calculations concern distinct obstacle families and do not imply this fixed-area polygonal rigidity theorem. The full text of the 2022 general polygon algorithm was inaccessible and an unindexed special-case formula remains a historical risk.

## Mathematical value

**PASS.** The Beer index is a standard measure of deviation from convexity. The theorem gives an exact two-parameter value and a natural, sharp shape-optimization and stability inequality at every fixed area deficit, with a universal affine-invariant result and a branch crossover at one-quarter of the original area. It avoids arbitrary parameter slices and does not assert that generic visibility integrals are new.

## Limits

No independent audit. The theorem is restricted to single edge-aligned corner notches in parallelograms with area-uniform pair sampling. The literature search does not establish absolute historical uniqueness. The reproducibility simulations do not substitute for proof.

Self-review: passed. Independent audit: not yet performed.
