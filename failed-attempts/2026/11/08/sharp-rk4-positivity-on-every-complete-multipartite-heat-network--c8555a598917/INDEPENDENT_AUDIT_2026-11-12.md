# Independent mathematical audit

## correctness

PASS

The orthogonal projectors onto constants, block-constant zero-sum modes, and each within-part zero-sum mode diagonalize L with eigenvalues 0,N,N-n_i. Hence every cross-part RK4 entry is (1-f(Nh))/N, with f(x)=1-x+x²/2-x³/6+x⁴/24. Same-part off-diagonals are (d_i h²/24)[12-4(N+d_i)h+(N²+Nd_i+d_i²)h²], whose quadratic discriminant is -32N²-16Nd_i-32d_i²<0. Diagonals add positive f(d_i h). The strictly increasing cubic x³-4x²+12x-24 has one positive root β; cross-part entries therefore become and remain negative after β/N. Since N is in the spectrum and f(x)>0, spectral absolute stability has exactly the same bound. The r>=2, singleton, h=0 and endpoint cases are covered by the proof. Independently recomputed 232 rational graph matrices, N=2..8.

## originality

FAIL

The complete October 25 Resultary theorem has the same graph class, normalization, RK4 polynomial, universal β/N bound, entrywise positivity iff spectral stability, strict same-part and diagonal positivity, and the exact same boundary behavior. Thus the entire present final claim is mathematically covered, irrespective of identical title or numerical approximations.

## value

FAIL

The submitted classification would be a useful graph-specific Runge–Kutta positivity theorem if unknown, but its full theorem, exact threshold, strict entry signs, Euler comparison and stability coincidence are already in the October 25 publication. A fresh rederivation and finite test are not separately valuable mathematical advances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
