# Independent mathematical audit

## correctness

PASS

Gauss collocation has R_s(z)=P_s(z)/P_s(-z); integral representation makes |R_s(-x)|<1 and even-stage R_s(-x)>0. Walsh diagonalization gives Krawtchouk kernel coefficients. Odd s→-1 on positive modes, giving negative diagonal for d>=2 at large h. Even s has R_s(-x)=1-2s(s+1)/x+O(x^-2); for d>=3 the nearest-neighbor coefficient is -s(s+1)S_d/(2^d h)+O(h^-2) with S_3=1/6 and S_(d+1)>S_d. Symbolic independent exact checks verified all 4 Q3 rational numerators against common denominator, unique positive quartic root 8.583763463733359, and positive S_d for d=3..9. For s=2, Q1,Q2 all h remain nonnegative; analytic coefficient signs establish Q3 iff cutoff. No extrapolation from bounded tests.

## originality

PASS

Existing results establish Gauss/Padé stability and the two-stage unconditional-positivity classification for all Cartesian products of cliques (hence Q_d=K2^d), so the two-stage d<=2 unconditional boundary is prior-covered. They do not yield the exact Q3 step-size threshold or the stage-parity d>=3 theorem for arbitrary even/odd s. The latter and the explicit first-failure cutoff survive as original motivated results, subject to specialist numerical-analysis priority risk.

## value

PASS

A minimal reversible 8-state system where a spectrally stable, mass-preserving implicit method loses Markov positivity has a sharp analytical timestep threshold; the full stage-parity obstruction distinguishes spectral contractivity and positive state propagation across all dimensions. Both are motivated benchmarks for geometric integrators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
