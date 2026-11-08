# Research review: sharp collision-tail law for noisy two-node Hermite interpolation

## Correctness — PASS
For each integer \(m\ge1\), the explicit endpoint value cardinal \(R_m\) and its highest coefficient \((-1)^{m-1}\binom{2m-2}{m-1}\) are established algebraically. The uniform collision expansion of the polynomial, the classical bounded Hermite remainder, the compact-dominated change of variable \(u=T^{1/(2m-1)}(Y-X)\), and the layer-cake moment identity together prove the exact positive Pareto coefficient and the strict moment cutoff. Exact-rational computations counted 281 checks for \(m=1,\dots,6\), and cardinal endpoint checks extended through \(m=8\); the proof does not rely on finite sampling.

## Originality — PASS (qualified)
The claim differs from deterministic singular-value/minimax bounds for Fourier confluent matrices in Batenkov–Diab (arXiv:2203.11923), stable Arnoldi Hermite polynomial evaluation in Niu–Zhang–Zhou (arXiv:2207.01852), and multivariate least-squares work (arXiv:2404.09266). The historical inversion survey (arXiv:2407.15696) and classical Gautschi inverse-norm bounds (DOI 10.1007/BF01432880) are close in conditioning but not known to give the stated unconditional random-node \(L^2\) tail constant. The Gautschi full text was not available; its abstract alone cannot exclude an equivalent result. A stratified-node Lagrange comparison has a different node geometry and does not imply the all-order two-node Hermite result. Database searches found no matching claim but are not novelty certificates; older specialized probability/interpolation results remain a credible precedence risk.

## Value — PASS
The explicit coefficient and the sharp \(p<1/(2m-1)\) moment condition quantify a practical failure of exact Hermite reconstruction from randomly colliding noisy knots. They show that every multiplicity has infinite mean global-error size, and that added derivative matching amplifies collision tails even when all jet errors are bounded. This addresses numerical uncertainty for a natural interpolation model; it is not a new floating-point implementation or a claim for separated nodes.

## Boundaries and scientific integrity
Assumes independent uniform knot locations on the same interval, fixed finite interpolation order, exact polynomial reconstruction, bounded jet noise independent of knots, a nonzero value-error discrepancy, and global \(L^2(0,1)\) error. Does not classify identical value noises, nonuniform/dependent knots, regularized recovery or alternative error norms. There is no independent scientific validation or publication-priority guarantee.

Self-review: passed. Independent audit: not yet performed.
