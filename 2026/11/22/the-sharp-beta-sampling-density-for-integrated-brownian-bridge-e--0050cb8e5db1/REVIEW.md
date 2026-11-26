# Independent mathematical audit

## correctness

PASS

The posterior is its linear interpolant plus independent Gaussian bridges in the positive gaps. On [a,b] of length ℓ, let U=B_a and D=B_b−B_a. Their covariance is −aℓ and Var(D)=ℓ(1−ℓ), so the interpolant covariance at offsets u,v is a(1−a)−a(u+v)+(1/ℓ−1)uv. Wick's rule gives conditional-mean risk 2∬C²+4∬C(K−C); triangle integration gives ℓ⁴/90 and a(1−b)ℓ³/12+(1−ℓ)ℓ⁴/45, respectively for the two unweighted integrals. This yields the frozen formula, with zero-length gaps contributing zero. The uniform grid gives (5m²−5m+2)/(90m⁴) for m=n+1. Near-minimizers have maximum gap tending to zero since the remainder is at least ℓ⁴/45 per gap and the grid gives O(m⁻²) total risk. Discrete Hölder yields the cube of the converging Riemann sum of [a(1−b)]^{1/3}ℓ as a lower bound for 3m²R. For attainment, put g(t)=[t(1−t)]^{1/3} and I=∫g. On every equal-g-mass gap, a(1−b)ℓ³≤(∫gap g)³=(I/m)³. On the middle half of any gap, t(1−t)≥ℓ/8, so equal mass also forces maximum gap O(m⁻³⁄⁴), and ∑ℓ⁴≤(max ℓ)³=o(m⁻²). This establishes the same limsup directly, including the endpoints. Independent evaluation gives 0.0496233141903951098 and a 10.6780344572888 percent improvement over 1/18.

## originality

PASS

Credit the previous exact two-reading case, established smooth-functional quadrature and the classical cube-root design mechanism. The supported distinction is the elementary all-design gap identity and a sharp optimum over arbitrary deterministic bridge point designs with the full nonlinear conditional mean, including endpoint control. A matching curve of the local density in another information class is not by itself a lower bound for the richer conditional-mean problem.

## value

PASS

For a canonical nonlinear Gaussian path functional, the theorem gives an exact risk evaluable on any mesh, proves an optimum for the leading risk over all deterministic designs and provides simple attaining nodes. The nonuniform design gives a quantified 10.68 percent gain relative to the natural equally spaced benchmark. That is a useful design result even though the underlying cube-root mechanism is familiar and it does not optimize each fixed budget.

The dated certificate retains the supplied scientific assessment, sources and limitations.
