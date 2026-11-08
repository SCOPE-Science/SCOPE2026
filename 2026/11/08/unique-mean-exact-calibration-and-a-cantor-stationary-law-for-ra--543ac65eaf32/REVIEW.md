# Review of Unique mean-exact calibration and a Cantor stationary law for randomized two-state generator splitting

## Correctness
PASS. Exact subflow matrices reduce to a one-dimensional affine random recursion; the unique invariant law follows from strict contraction. The invariant mean equation has a unique solution because an exponential integral is strictly monotone. At that solution, Bernoulli-sum moments yield exact mean/variance at every discrete time, and the separated cylinder argument proves the Cantor support, dimensions and first-level gap. A standalone standard-library verifier supports the exact arithmetic through 6,557 assertions, without replacing the infinite proofs.

## Originality
PASS, subject to publication-precedence risk. Veldman and Zuazua, *A framework for randomized time-splitting in linear-quadratic optimal control* (arXiv:2109.13798), establish importance-scaled random exact subflows and general finite-horizon error bounds. Eisenmann and Stillfjord (arXiv:2210.05375) analyze a related randomized implicit evolution scheme. The exact self-similar measure technology of Hutchinson (1981) and Bernoulli convolutions is preexisting and explicitly credited, and Chakraborty (2023) studies a different random-matrix-entry distribution. None of the inspected statements covers the exact rate-proportional mean semigroup identity coupled to the finite-time error constant and invariant equilibrium gap for these two-state one-way flows. The specialist 2023 article was not completely retrieved, so an equivalent unpublished or specialized result cannot be ruled out.

## Value
PASS. Two-state continuous-time Markov generators give a minimal but natural test of randomized time-splitting. The result identifies a unique mean-unbiased configuration while showing that for coarse steps every numerical realization is uniformly separated from the target equilibrium. It gives a precise design and diagnostic boundary with exact, reproducible error constants rather than a generic variance warning.

## Scientific limits
The proof does not extend to arbitrary state counts or inexact subsolvers, and does not classify the overlapping Bernoulli-convolution range. An invariant law of randomized probability-vector propagation is different from the underlying CTMC equilibrium or an exact CTMC sample path. Specialist publication precedence remains an open risk.

Self-review: passed. Independent audit: not yet performed.
