# Independent mathematical audit

## correctness

PASS

Strongly convex objective has KKT multipliers and continuous piecewise-affine proximal map. Because second-difference D is surjective, every zero-curvature active-row subset F occurs on an open strictly complementary stratum (choose z0 with prescribed zero/nonzero D z0, multipliers 0 on F and sign 1 elsewhere). Jacobian is the constant-preserving orthogonal projector P_F. Any input difference decomposes into a constant plus one-jump vectors; the V seminorm operator norm of P_F is max_j V(P_F c^j). Integrate local derivatives along line segments to bound globally and realize each maximizing norm locally, proving equality for all n and lambda>0. Rational exhaustive enumeration for all faces and jumps at n=2..8 reproduced independently in a SymPy implementation, including 4-site exact 6/5 KKT witness; affine least-squares step slope 6j(n-j)/(n(n^2-1)) analytically gives universal bound and asymptotic >=3/2.

## originality

PASS

Best-of-knowledge: the known generalized-lasso active-set geometry is not claimed as new. The sharp induced two-input adjacent variation modulus, threshold 4, exact fractions and all-n amplification are distinct from prior l2 nonexpansivity and statistical spline/rate theory.

## value

PASS

Sharp failure of a natural perturbation stability property at the minimum feasible path length n=4, complete low-n constants, and an exact all-length active-face formula have clear numerical-analysis relevance. A global >=1.5 limiting lower amplification shows this is not a negligible toy counterexample; unknown general exact coefficients are openly limited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
