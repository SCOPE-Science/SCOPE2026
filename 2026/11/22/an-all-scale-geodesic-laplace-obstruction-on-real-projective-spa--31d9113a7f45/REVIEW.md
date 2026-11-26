# Independent mathematical audit

## correctness

PASS

On the projective line the π-periodic kernel has Fourier coefficients proportional to a[1−(−1)^k e^(−aπ/2)]/(a²+4k²), including k=0. They are positive and summable, and the zero-quadratic-form condition on finitely many distinct sites forces all Fourier moments to vanish, hence by consecutive Vandermonde rows all weights vanish. On RP² pull back to the even kernel on S². With f(t)=e^(−a arccos t) on [0,1] and g=(1−t²)f′, the Legendre equation gives ℓ(ℓ+1)I_ℓ=−2g(0)P_ℓ(0)−2∫_0^1g′P_ℓ for even ℓ≥2: the degree derivative term at 0 is zero by parity, the first differentiated Legendre term at 1 vanishes, and g is absolutely continuous with g(1)=0 and integrable derivative. In angle coordinates the last integral has smooth bounded amplitude a e^(−aθ)(a sin θ−cos θ). On [δ,π/2] the compact-angle expansion and Riemann–Lebesgue imply o(ℓ^−1/2); near zero the Bernstein bound combined with |P_ℓ|≤1 bounds its ℓ^1/2-scaled magnitude by C_a(ℓ^−1/2+√δ). The remainder is therefore little-oh after taking the limits in that order. Since g(0)=a e^(−aπ/2) and P_{2n}(0)=(−1)^n binom(2n,n)/4^n, the coefficient and sign are exactly as stated. A negative even eigenvalue from Funk–Hecke gives a negative integral quadratic form, whose finite weighted Riemann sums yield a negative finite Gram form (repeated projective sites can be merged). The isometric coordinate embedding transfers it to every higher projective dimension. This proves failure separately at each fixed a>0, not a uniform threshold in a; at a=0 the kernel would be constant, outside scope. The numerical CHECK.py was inspected, not executed; its finite quadratures are not used for the universal asymptotic.

## originality

PASS

The supported distinct claim is the separate obstruction at every positive damping, certified by a signed, normalized plane coefficient, with the projective line as the classical circle side of the boundary. General spectral criteria, earlier negative-type obstructions, the square-distance Gaussian result and standard Legendre asymptotics are not claimed as new. A general signed expansion theorem is a plausible priority risk: the particularly relevant Sidi paper was identified but not available to verify the coverage of its formulas. The accessible results compared below do not establish that signed specialization or an every-scale linear-distance conclusion. This is a bounded decision, not a certification of priority.

## value

PASS

The distinction between lacking PSD simultaneously at all scales and failing at every possible scale is important in choosing intrinsic covariance kernels. The coefficient proof identifies why no damping repairs the projective-plane case and why failure does not extend to the projective line. The signed asymptotic adds a spectral diagnostic, not simply a conditional-negative-type counterexample or a finite test at one parameter. It need not provide a uniformly small finite witness to be useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
