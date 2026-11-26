# Independent mathematical audit

## correctness

PASS

Subtract c/(1-s) and stack all L+1 history layers. The steady state is admissible and unique by the maximum-norm s-contraction on time-constant vectors. At the unique positive root (the product decreases strictly from infinity to s^n), the cycle equations v_i=s H_i(r)v_{i-1} close consistently with v_i>0. The layer values r^{-k}v_i give a strictly positive eigenvector of the actual lifted matrix, including zero lag weights or unused layers. Similarity by the diagonal of this vector produces a nonnegative matrix with row sums r, so the induced infinity norm and spectral radius are both r; a small positive multiple of the eigenvector realizes equality from an admissible history. This checks the worst-case quantifier without assuming primitivity, or a rate for each initial history. At fixed r<1, Jensen gives H_i(r)≥r^{-(1+μ_i)}, with equality only for a deterministic law; monotonicity moves the unit root strictly to the right if any lag law is mixed. Every feasible integer total can be distributed among the bounded integer lags. With fixed individual means, extend the strictly convex lag values by piecewise linear interpolation to obtain the adjacent-integer minimum; the endpoint chord gives the maximum. Strictness on other discrete supports forces the extremizers, with the trivial singleton and two-point degeneracies included. Likewise a strict convex-order change increases the transform: on a finite integer support the discrete second differences of r^{-k} are positive and at least one call expectation changes. The example independently reduces to 8r^5−3r^4−1=0 with root 0.75655233305921373596…, versus 1/√2 for both fixed budgets. This is deterministic weighting of histories, not a stochastic switching model.

## originality

PASS

The standard positive-mode and convex-order mechanisms are not independently new, and closely related transform and fixed-mean optimization already appear in a randomized-solver setting. The supported distinct claim is an exact all-history spectral law for this heterogeneous affine cycle together with equality for every spatial allocation of fixed lag budget and strict loss for temporal mixing of the same budget. No available stronger result implies that conjunction. This is a bounded judgment; the closest delayed-opinion originals were not recovered in full.

## value

PASS

The lag budget is an intrinsic design parameter, and the conclusion says exactly when changing where rather than when memory is applied is free in the sharp relaxation rate. The whole finite support problem has explicit attainable extrema, including noninteger individual means; this is more informative than convergence or a maximum-delay bound. Its scope is deliberately the directed affine cycle, not a general model of empirical beliefs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
