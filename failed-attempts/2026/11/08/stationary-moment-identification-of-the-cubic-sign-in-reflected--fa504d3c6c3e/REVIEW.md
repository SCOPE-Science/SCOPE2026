# Independent mathematical audit

## correctness

PASS

Zero flux and variance rate D (not diffusion coefficient D) give exponent (μx²+sx⁴/2)/D. In the strictly positive stationary exponential family of Y=X², Y² is not affine in Y, so the covariance matrix of (Y,Y²) is positive definite. At fixed β=s/(2D), the derivative of m2 in α=μ/D is Var(Y)>0; the limiting values at α→−∞ and +∞ are 0 and L² by compact-support concentration, since exp(βx⁴) is uniformly bounded above and below for each fixed β. Matching m2 is therefore possible at any β. The fixed-m2 derivative of m4 in β is the strictly positive Schur complement, proving the sign comparison, including equality only for β=0, and showing variance-alone ambiguity for every interior variance. Integrating the derivative of x^(2k+1)(L²−x²)p for k=0,1 removes the endpoint terms and gives the exact two-by-two system, with Δ=A² times the positive variance of X² under the normalized weight x²(L²−x²)p. Cramer's rule gives both displayed ratios, not the scale D. An independent exact uniform-case check at L=1 gives Δ=32/33075 and Q=R=0. Replay RESULT.md:42–83; frozen verifier and dependency were inspected, not executed. The reported quadrature cannot replace these arguments.

## originality

FAIL

The explicit rational reconstruction is covered by a published general boundary-weighted score-matching formula for exponential families, down to its exact sufficient statistics, boundary weight and moment matrix. The profile sign test is a one-step specialization of strict monotonicity of an exponential-family mean map with one coordinate matched; the claimed variance-only obstruction is the elementary endpoint range of the remaining one-dimensional tilt. The reflected stationary model and the temporal data distinction are real, but no nonmechanical remainder survives in the frozen exact claims.

## value

FAIL

Static sign diagnosis under reflection is a sensible motivating problem. In the specified exact model it reduces completely to strict convexity with one moment matched and to an already general boundary-weighted estimator. The record does not add a substantive exact invariant beyond these routine consequences; it also claims no robustness or observation regime in which the general argument requires a new idea. The specialized formulas are useful exposition, not a surviving new scientific result to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
