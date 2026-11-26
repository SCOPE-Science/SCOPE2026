# Independent mathematical audit

## correctness

PASS

On the unit S³ the degree-ℓ harmonic sign is that of the integral against sinθ sin((ℓ+1)θ). The base cosine integral is I_k=a(1−(−1)^k exp(−πa))/(a²+k²); its difference gives the positive base coefficient J_ℓ=(I_ℓ−I_(ℓ+2))/2. Multiplying by cos2θ shifts the sine modes by ±2. The negative sine index at ℓ=0 gives slope (t−8)/(t+16), and the zero sine index at ℓ=1 gives slope (t+1)/(t+25); thus only degree zero can bound b from above, only for t<8. For ℓ≥2 the two shifted coefficients are positive and the common parity factor cancels, giving R_m with m=ℓ+1. The denominator increases in m²≥9 and is positive at 9; R_m>0, is less than 1 for m²>t+5, and tends to 1, so its minimum is positive, below 1, and attained. The derivative in y=m² changes sign just once for y≥9, at μ(t)², giving the floor/ceiling test. The exact adjacent difference has positive factor times C_m−(2m²+2m+11)t−3t²; C_(3+u)=u⁴+14u³+63u²+98u+28>0. Its unique switch occurs between μ=m and μ=m+1 (with t=0 interpreted by continuity for m=3), proving strict ordering, no skips, and no triple minimum. For candidates m=√(3t)+O(1), the numerator of 1−R_m is 48t+O(√t), denominator 16t²+O(t^(3/2)), giving the claimed asymptotic. All sufficiently high degrees have positive coefficients, so both parities occur and even boundary kernels are strictly positive definite on distinct points. For uniform density, the integral of a kernel section against a harmonic of present degree recovers a nonzero scalar times that harmonic; finite sums approximate this integral uniformly. Harmonic polynomials are dense, whereas a missing degree is detected by a nonzero continuous linear functional. This proves the universality and exact absent-degree assertions. A separate symbolic replay (`python3 /workspace/independent_checks.py 5`) confirmed the ratio, adjacent difference and degree-zero slope; the supplied checker was inspected but not executed.

## originality

PASS

Best-knowledge pass for the sharp signed S³ region and its consecutive active-degree law. The two strongest mirror matches were checked: the S³ pure-wave theorem determines signs for the unmodulated and pure-wave components, and the same-day circle theorem proves a comparably structured staircase, but neither gives the evaluated signed S³ lower envelope. The general harmonic tests and the strictness criterion are prior inputs, not new results here.

## value

PASS

The full two-parameter region is a useful design criterion for geodesic covariances. Its finite upper cutoff and unbounded sequence of active lower modes explain distinct mechanisms for losing positivity, while the two-candidate test is exact regardless of damping. The spectral zeros separate finite interpolation from uniform approximation even on the admissible boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
