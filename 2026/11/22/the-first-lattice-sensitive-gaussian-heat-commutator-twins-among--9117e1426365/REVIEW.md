# Independent mathematical audit

## correctness

PASS

For the stated normalized torus, the Fourier basis gives a sum of (exp(-t|Ak|²)−exp(-t|k|²))². Since A permutes the integer lattice, this is twice the theta sum of 2I minus twice that of Q=I+AᵀA. Here det Q=T+2, where T is squared Frobenius norm. Poisson summation gives π/t times (1−2/√(T+2)) plus dual terms. The two matrices have determinant 1, trace −4 and T=18; the AᵀA eigenvalues are 9±4√5. Their reciprocal numerators over 10 reduce by integer changes of variables to x²+5y² and 2x²−2xy+3y². The latter is 2(x−y/2)²+5y²/2, so the first two positive coefficients are 2 and 3; the former has first two 1 and 4. Both first lengths occur twice. Subtracting the Poisson expressions gives the stated −2π/(√5 t) times the difference of the two exponentials. The remaining series are bounded by factoring out exp(−3π²/(10t)) and dominating the rest by shifted positive-definite Gaussian sums at t=1. This proves the common algebraic asymptotic and strict inequality for sufficiently small t, not an all-t inequality. An independent exhaustive integer census over [-4,4]^4 gives absolute-trace/cost groups (3,7),(3,11),(4,15),(4,18). For all 32 lower-cost matrices the census finds explicit unimodular equivalences to the indicated one form per group, which proves equality of the full theta sums, not just their initial coefficients.

## originality

PASS

The supported distinct claim is the first separation of the fixed-metric Gaussian commutator energy for hyperbolic determinant-one integer matrices of equal trace and squared Frobenius norm, including the exact leading exponential splitting. This does not credit the Fourier reduction, Poisson summation, or binary quadratic-form methods as new. The strongest available comparisons show background or a different kernel, not coverage of the constrained first separation.

## value

PASS

The calculation gives a sharp counterexample to recovering a natural Hilbert–Schmidt heat-defect invariant from dynamical eigenvalues and Euclidean singular values. It shows exactly how equality to all algebraic orders can hide a metric-lattice difference, and the minimum squared cost makes the pair a reusable small test case for toral smoothing calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
