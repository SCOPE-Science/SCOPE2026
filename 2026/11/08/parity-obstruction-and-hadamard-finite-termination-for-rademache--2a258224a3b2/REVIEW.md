# Self-review

## Correctness (PASS)
The quadratic finite difference gives an exact orthogonal projection at the optimal step. Modulo-two idempotence gives an obstruction for all words in every odd dimension. Hadamard row orthogonality gives a zero word and the independent-block stopping-time bound. Conversely a length-\(d\) zero word requires rank loss at each step and hence mutually orthogonal sign vectors. Exact arithmetic verification: 659 checks. The assertion is exact arithmetic only; finite experiments are not an infinite-dimensional proof.

## Originality (PASS, with risk)
Song et al. (arXiv:2604.14669) treat Gaussian moment stability and the covariance extension to non-Gaussian directions, not the discrete pathwise stopping dichotomy in the inspected text. Strohmer--Vershynin (2009) and Bai--Wu (2023) address randomized Kaczmarz convergence, while Hadamard orthogonal frames are classical. Direct comparison of statements did not show that those results imply the modular obstruction or complete shortest zero-word criterion. Full-text equivalences beyond inspected material remain possible.

## Value (PASS)
It demonstrates an exact finite versus never-finite stopping distinction among discrete stochastic gradient solvers with the *same* expectation contraction, and provides a rigorous dimension-dependent stopping-time benchmark. This is a structural behavior, not merely an isolated numerical constant.

## Boundaries
The result does not address all even non-Hadamard dimensions, floating-point arithmetic, generic Hessians, or general initial points in odd dimension.

Self-review: passed. Independent audit: not yet performed.
