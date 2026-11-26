# Independent mathematical audit

## correctness

PASS

With Haar probability, degree ℓ contributes (2ℓ+1) times its character to the projection kernel, and the kernel of the data operator TT* is its restriction in both arguments. For half-turns with axes u,v the character is U_{2ℓ}(u·v); the Chebyshev sum/derivative yields C^{(2)}_{2L−2}. Probability-normalized Funk–Hecke on S² contributes the factor 1/2 in the integral, with only even degrees descending to the quotient. Integration by parts gives each successive level difference as a positive constant times ∫sin(2Lθ)P_{2j+1}(cos θ)dθ. The Legendre cosine coefficients are positive by the generating function, and each odd frequency k in its support satisfies |k|<2L and contributes 4L/(4L²−k²)>0. The constant level is L by the U-polynomial boundary values, and the lowest level follows from the leading coefficient and Legendre norm, so all displayed levels are positive, including L=1 where the lone level is 1. The rank, nullity, reconstruction on the orthogonal complement and condition number then follow by spectral decomposition and the central binomial asymptotic. Independent exact rational computation for L=1–8 checked strict order, endpoints, trace and dimensions, e.g. (2,8/5) and (3,96/35,128/63). Replay: generate Gegenbauer and Legendre polynomials by their three-term recurrences and apply the exact moment functional t^(2r)→1/(2r+1), t^(2r+1)→0 to their products. This corroborates finite bandwidths; the analytic argument supplies all bandwidths.

## originality

FAIL

The exact levels, strict order, rank and asymptotic are a mechanical specialization of the spherical harmonic addition and Funk–Hecke formulas and the classical Gegenbauer connection formula. A direct prior article using the half-turn trace terminology was not established; the failure is the explicit broader-formula implication, not an assertion that a cited fiber transform or torus trace has the same spectrum.

## value

FAIL

The half-turn data model and visible condition number are natural, but the exact rank, singular ordering, endpoints and exponent all follow by elementary specialization of the existing projector and connection formulas. This record does not establish an additional distinct reconstruction or sampling result beyond that specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
