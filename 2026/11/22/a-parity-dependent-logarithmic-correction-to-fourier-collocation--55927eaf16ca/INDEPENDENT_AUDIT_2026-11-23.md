# Independent mathematical audit

## correctness

PASS

The circulant entry S=N*P_0j uses a single Nyquist cosine on even grids and symmetric Fourier modes through (N-1)/2 on odd grids. The full Poisson-periodized Gaussian Theta is positive. Write c=Nt, d=N/2-j with 0<=j<=floor(N/2), and phi(c)=(c-pi²/c)/4. In the odd omitted tail, frequency (N+1)/2+l has nodal cosine (-1)^(j+l) sin(2pi*d*(l+1/2)/N), since (N/2)x=pi*j. This gives a geometrically summable multiplier d/N absent in the even bound. Using the nearest Gaussian image, the tail/Gaussian ratio on pi/2<=c<=2pi is bounded by a constant times N^-1/2 times exp(-N*phi(c)) on even grids, or N^-3/2 times that exponential on odd grids: one uses x²/(4t)-N²t/4 <= -N*phi(c)-pi²*d/(2c), so the factor d is uniformly absorbed on the compact c range. At c_plus=pi-(kappa*log N-B)/N, N*phi=-kappa*log N/2+B/2+o(1), with phi increasing. This proves strict positivity up to c=2pi when B is sufficiently large. For 2pi<=c<=2N the geometric prefactors and d/N are bounded, sqrt(t)<=sqrt(2) and phi(c)>=phi(2pi)>0. For t>=2 the constant mode exceeds the sum of all nonconstant magnitudes. Thus the upper bound is for every later real time. For the lower bound choose j=2*floor(N/4), hence d=0,1 (even) or 1/2,3/2 (odd). The two nearest Gaussian images together give a positive constant multiple of sqrt(N)*exp(-pi²*N/(4c)) uniformly when c→pi. At that even j, geometric domination gives the positive even tail factor tanh(c/2); the scaled odd linearized sine sum is sum_l (l+1/2)(-exp(-c))^l=(1-exp(-c))/(2(1+exp(-c))²)>0. The odd factor d/N survives because d is bounded away from zero. The resulting Gaussian/tail ratio at c_minus=pi-(kappa*log N+B)/N is a bounded positive prefactor times exp(-B/2)(1+o(1)), below one for sufficiently large fixed B. A negative entry there and the uniform upper positivity yield the stated bracketing and O(N^-2) error. Independent 220-digit replay at B=12 covered N=100–103, 128–131, 200–203, 256–259 and all upper-time entries. For N=100 and 101 the scaled lower witnesses were approximately -4.4500e-33 and -1.3949e-34; upper minima were 9.3425e-33 and 1.1275e-33. Replay: python3 /workspace/reviews/evidence/4-heat-check.py (mpmath). This finite arithmetic neither proves the asymptotic nor certifies positivity at all subsequent times; the analytical envelope does. Frozen verifier inspected, not executed.

## originality

PASS

The directly preceding even-grid theorem does not state the logarithmic correction, but its existing proof yields the even coefficient by a short uniform boundary-layer re-evaluation. The new content is chiefly the odd-grid first-order tail cancellation, the matching positive odd tail witness, and hence the sharp parity split in the eventual horizon. No inspected broader norm or other discretization result covers that odd coefficient. Historical priority is bounded by the sources inspected.

## value

PASS

For an unmodified spectral heat discretization, exact preservation of the nonnegative nodal cone is stronger than near-contractivity. The sharp leading odd law and its factor-three logarithmic advance resolve a parity-dependent sign effect at a physically motivated threshold, while uniform all-later-time positivity makes the claim about the last occurrence of negativity rather than a sampled sign. No exact finite-grid root or off-grid positivity is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
