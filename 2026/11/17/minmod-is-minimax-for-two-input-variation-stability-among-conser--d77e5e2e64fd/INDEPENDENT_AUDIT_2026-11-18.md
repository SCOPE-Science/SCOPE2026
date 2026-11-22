# Independent mathematical audit

## correctness

PASS

The exact minmod theorem is recovered from the cubic Hermite basis H=3t^2-2t^3, A=t(1-t)^2, B=t^2(t-1). For a single secant perturbation, minmod partial derivatives are 0 or 1; the central spatial derivative H’+pA’+qB’ is nonnegative for p,q in [0,1] because all four vertices are nonnegative, and has total integral 1. Each adjacent bump has variation 8/27, giving the global two-input upper bound 43/27 by integration and absolute summability. For every conservative affine-exact limiter a 1-to-(1-epsilon) central slope change forces both knot derivatives to decrease by at least epsilon and each neighbour bump to contribute at least 8epsilon/27, while the middle cell contributes at least epsilon; minmod attains equality. Independent exact rational bump and kernel checks corroborate. The classification does not extend to selectors exceeding the smaller secant, other grids or higher degrees.

## originality

PASS

Qualified PASS: Hyman and classical monotone-Hermite work prove individual-curve monotonicity/admissible slopes and qualitative sensitivity, not a minimax two-input variation norm over the precise unit-capped affine-exact selector class. The published harmonic-mean and Steffen sharp 59/27 results are for other selectors; the harmonic selector equals 8/5 at (1,4), violating the unit cap, and the Steffen selector can use 2 times the smaller secant. Neither implies the universal 43/27 lower bound, attainment for minmod or its restricted minimax property. Indexing may miss an earlier equivalent theorem.

## value

PASS

The exact minimax 43/27 gives a precise robustness benchmark for conservative local shape-preserving interpolation, distinguishing one-signal variation from two-signal perturbation sensitivity and furnishing a universal extremal witness; this is a motivated method-level stability fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
