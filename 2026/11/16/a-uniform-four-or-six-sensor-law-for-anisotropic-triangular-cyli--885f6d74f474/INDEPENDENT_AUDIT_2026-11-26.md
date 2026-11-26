# Independent mathematical audit

## correctness

PASS

The operator is the normalized sum of two cyclic shifts and their inverses in each coordinate. The horizontal Fourier dimensions are 1 and 2, the vertical dimensions 1 at zero and 2 elsewhere. Each horizontal branch has strictly descending eigenvalues in the vertical level, so a coincidence uses precisely one level per branch. A coincidence gamma=3/(mu_t-mu_s) has s>t and dimension 2+2 at t=0 and 2+4 otherwise. Equality of two coupling ratios cannot concatenate more than two blocks at any eigenvalue. Any spatial set with fewer sites than the maximal eigenspace dimension has a permanently invisible eigenvector. In an unmixed block, adjacent vertical samples resolve the two Fourier characters (z differs from z^(-1) by oddness) and x=0,1 resolve the two horizontal characters. At t=0, taking differences at the two horizontal sites cancels the y-constant terms; the equations have determinant (z-1)(z^(-1)-1)(z^(-1)-z), nonzero even at N=3. The six-site rectangle separates each horizontal character by the full three-point transform and resolves an adjacent vertical pair for each. The distinct-eigenvalue time Vandermonde needs at most N+1 time samples, starting at zero. Independent physical shift matrix tests (evidence/3/reproduce.py and replay.txt) give full stipulated ranks at ordinary and both collision types, including N=3 at gamma=1 and the six-dimensional N=5 collision at 3/sqrt(5). They are floating-point representative tests, not the justification for all odd N. The guarantee is exact noiseless recovery, not uniform conditioning or a shortest time horizon.

## originality

PASS

The exact operator, infinite odd-cycle family, and universal staggered four sites surviving every benign collision are not covered by the strongest inspected fixed-torus, two-layer ladder, or abstract observability results. The max-eigenspace-dimension lower bound and orbit-frame criterion are not new.

## value

PASS

The exact physical sensor budget over an infinite natural graph family is a motivated design invariant. It separates benign from sensor-costly coincidences and gives one implementable optimal four-site choice for all benign parameters. The stagger matters: the ordinary rectangle fails already at the benign N=3 collision, although the dimension lower bound remains four. This is not just a spectral multiplicity table or a generic rank criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
