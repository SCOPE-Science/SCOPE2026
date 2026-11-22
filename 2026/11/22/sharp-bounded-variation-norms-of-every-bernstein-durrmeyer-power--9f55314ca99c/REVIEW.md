# Mathematical assessment

## Correctness — PASS
The argument derives TP2 from the Bernstein kernel, proves persistence under composition, and uses reflection and strict likelihood-ratio ordering to locate the unique endpoint-row crossing at the midpoint. Each BV input decomposes into jumps; the unique maximizing jump yields the all-power sharp norm and equality cases. The known shifted-Legendre spectrum then yields the finite alternating formula and long-power asymptotics. The independent Gram-matrix coefficient computation agrees exactly at 96 integer pairs, and checks the strict power inequality in those finite cases. The general proof does not rely on enumeration.

## Originality — PASS, with historical limits
The 2016 BV paper has a qualitative contraction and approximation-in-variation result, not sharp power coefficients. The full accessible indexed 2026 Jacobi-weighted result covers one-step oscillation and explicitly excludes arbitrary iterations. The 2025 all-power kernel representation and the 2016 eigenstructure/ergodicity work give prior spectral ingredients, not the unique sharp midpoint BV extremizer or the exact power norm. The proposed statement therefore adds an all-power endpoint functional bound not implied as a corollary without new positivity/crossing analysis. Historical priority beyond inspected searchable and accessible materials is not certified.

## Value — PASS
Iterating the one-step sharp BV bound gives only \((1-2^{-n})^r\), which may be near unity for large degree. The exact all-power law shows instead the eventual optimal rate \((n/(n+2))^r\) with universal factor \(3/2\), gives sharp extremizers and exact strict submultiplicativity, and provides a benchmark for stability under repeated integral-polynomial smoothing. This is a natural operator-norm question, not an arbitrary finite slice.

## Closest literature and limitations
The closest indexed finding is `ff055fe1e2d7` (unweighted one-step coefficient within a Jacobi-weighted oscillation theorem). Öksüzer et al. (2016) show variation diminution; Abel et al. (2025) prove composition-kernel expansions; Heilmann and Raşa (2016) derive spectral and iterate convergence properties in a different norm. Unweighted real BV and fixed degree are essential; asymmetric weights, mixed degrees, and vector-valued data are not treated. An independently checked historical-priority search remains desirable.

Self-review: passed. Independent audit: not yet performed.
