# Independent mathematical audit

## correctness

PASS

Q has stationary projector Pi with rows (b/s,a/s) and equals -s(I-Pi). Rational functional calculus gives T_h^n=Pi+r(z)^n(I-Pi). For z>0, |r|<1, so the off-diagonals are strictly positive and it suffices to test the minority diagonal m+(1-m)r^n. The derivative numerator f(z)=z²(z-10)-20z-8 is strictly negative up to z=10, strictly increasing thereafter and unbounded, giving a simple nondegenerate minimum past the sole positive zero z_0 of r. Even powers preserve probability; for odd powers the worst minority diagonal vanishes precisely at m_n=c^n/(1+c^n), with exactly two equality endpoints for m<m_n and a single tangency at equality. The expansion of the endpoint level is -c+c^(1-n)(1+c^n)^2 delta/n+O(delta²); the nondegenerate quadratic minimum gives both endpoint expansions. The determinant is r^n, so positive determinant is necessary; it is sufficient here via exp[log(r^n)(I-Pi)] with nonnegative off-diagonals in the exponent. At z_0 all powers are singular; after it all odd powers fail embeddability regardless of nonnegativity. Exact independent inversion verifies the stated two-rate negative diagonal (-82/3185) with a positive square.

## originality

PASS

The supported distinct contribution is the scheme-specific complete rate/step/odd-iterate frontier, including its sharp extremum and cusp constants, for active Richardson backward Euler. The active stability function, scalar zero, equal-input positivity and embedding criteria, and mechanism of parity recovery are not in themselves new.

## value

PASS

An L-stable integrator can produce a negative probability on a bounded step interval in the minimal irreducible kinetic model. The exact rate-imbalance threshold decides whether that failure can happen at any step; the odd-power classification decides whether it can persist after a chosen number of identical steps. This is a complete sharp diagnostic, and the finite-rate embedding distinction prevents confusing output stochasticity with physical continuous-time evolution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
