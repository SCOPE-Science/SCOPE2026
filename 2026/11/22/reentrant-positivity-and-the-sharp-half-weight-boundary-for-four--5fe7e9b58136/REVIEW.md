# Review: four-node Gaussian quadrature sign reentrance

## Correctness — PASS
The full Gram matrix of the Gaussian kernel is strictly positive definite at all distinct sites, giving a positive even-block determinant. Exact paired-equation inversion establishes the numerator formulas. Direct Taylor expansions prove strictly positive limits near zero, and Gaussian concentration proves eventual positivity. At inverse squared lengthscale two, the bundled standard-library rational-interval certificate (order 80, with rigorous Taylor remainders) proves two negative outer weights, two positive inner weights and a positive determinant. Continuous dependence in shape and node radii proves two separated sign crossings and persistence on an open parameter set. Neither scans nor printed floating-point approximations serve as a proof.

## Originality — PASS, with residual publication-priority risk
The Bayesian quadrature linear system and examples of negative weights are already in Huszár–Duvenaud (2012). Karvonen–Kanagawa–Särkkä (2019), Theorem 1, proves a general half-positive lower bound, and their local-optimal-node corollary is inapplicable to our nonoptimal fixed sites. Karvonen–Särkkä (2020) gives the flat polynomial limit. None of the examined mathematical statements establishes a fixed four-site design with strict positivity at both shape extremes but exactly two negative weights at an intermediate shape, robust under perturbation. Related historical dissertation material was inspected in the sections concerned with kernel cubature, not exhaustively. An unindexed or unexamined equivalent example is possible; the claim does not assert publication priority as settled.

## Value — PASS
This is a robust example of a practical numerical stability boundary: a node set whose Gaussian Bayesian-quadrature weights are positive in both the flat and sharply localized regimes can nevertheless lose positivity at an intermediate bandwidth. It also realizes the best possible lower guarantee on the number of positive weights for an even four-node totally positive kernel, with strict inequalities and a reusable rational certificate. It is more informative than a single isolated negative coefficient because the same topology of signs persists on an open set of quadrature geometries.

## Scientific limitations
At least two crossing shapes are proved, not uniqueness of each crossing. The method applies to the stated unconstrained quadrature rule with no nugget. Neither improved integration accuracy nor an optimal selection of points is claimed. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
