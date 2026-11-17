# Independent mathematical audit

## correctness

PASS

PASS: From f(x)=||x||^2/2 exact symmetric two-point finite difference gives (u dot x)u and P_u=I-uu^T/d. Since P_u is an orthogonal projection, E||P_u x||^2=(1-1/d)||x||^2 and unique mean-square minimizer eta=1/d follows from 1-2eta+d eta^2. When d odd, integer matrices dI-uu^T are congruent mod 2 to I+J, which is an idempotent nonzero on e_i, precluding finite zero in every sign word; at every Hadamard order a prescribed block of d independent orthogonal rows annihilates all starts with positive independent block frequency. A rank drop by 1 at each stage is necessary for a universal length-d zero product and forces orthogonality. Independently computed exact signed projector products for d=2,4,8 and modular invariants for d=3,5,7. Almost sure convergence follows Markov/Borel-Cantelli; probability-one finite termination follows independent block success, not finite enumeration.

## originality

PASS

PASS, best-of-knowledge: mean-square convergence for stochastic gradient/projection schemes and Hadamard orthogonality are classical and expressly not novel. The specific all-sign odd-dimensional exact-arithmetic obstruction together with Hadamard dimension stopping-time dichotomy and iff minimal annihilation word is not supplied by inspected prior bounds or semantic results. Original ZO stability work supplies variance context, not exact finite stopping, although an unindexed linear-algebraic reformulation could cover the essence.

## value

PASS

PASS: Finite termination versus vanishing mean-square error is an important distinction in exact randomized projection algorithms. The modular obstruction and Hadamard universal-word characterization are concise structural results for a natural standard estimator, with dimension-wide positive and negative regimes; value does not depend on speculative applications to floating point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
