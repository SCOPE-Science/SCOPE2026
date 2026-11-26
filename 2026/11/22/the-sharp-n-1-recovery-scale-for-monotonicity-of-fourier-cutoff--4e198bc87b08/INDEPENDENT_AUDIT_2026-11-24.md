# Independent mathematical audit

## correctness

PASS

With the stated symmetric cutoff and circumference, F=-H'/2 is the sine sum with weights k exp(-tk²). Log-differentiating the Jacobi product at fixed t>0 makes F positive and gives F/sin(theta) >= b t^(-1/2) exp(-pi²/(4t)) for t<=1 by retaining the first product summand and the nearest Poisson image. Since |sin(k theta)| <= k sin(theta) on the open angle interval, the omitted tail divided by sin(theta) is <= C_c N² exp(-tN²) uniformly for t>=c/N (k=N+j gives the summable factor exp(-2cj)). The ratio to the full lower bound decreases in t on [c/N,1] and is O_c(N^(3/2) exp[-N(c-pi²/(4c))]) there, proving the uniform sufficient times for c>pi/2. For t>=1 the first sine mode strictly dominates: the sum of the other modes after division by exp(-t) sin(theta) is bounded by sum_{j>=1}(4e^(-3))^j<1, for all N. For c<pi/2 and theta=pi-alpha_N/N, the tail divided by N exp(-cN) has summable majorant (1+j)exp(-2cj); along either parity the sign factor (-1)^N sin(alpha_N)=1 yields the positive limit 1/(1+exp(2c)). The derivative of the full periodized Gaussian is bounded there by C_c N^(3/2) exp(-pi² N/(4c)): each image distance is at least pi-O(1/N), and after factoring out the nearest-image exponential the more distant terms are summable uniformly with their distance multipliers. This is o(N exp(-cN)), proving F_N<0, equivalently H'_N>0, for both witness subsequences. A failure at time c/N bounds the infimum of eventual times from below whether or not attained; the upper estimate is uniform in every later time. This proves finiteness and the exact limit with no claim at c=pi/2. RESULT.md lines 31–115 are decisive. verify.py and its recorded 585 diagnostics were read, not run; those samples are neither an exhaustive sign check nor needed in the proof.

## originality

PASS

The supported distinct statement is the sharp eventual strict derivative sign for continuous symmetric sections, including two parity witnesses. Full-kernel radial monotonicity and antpodal Gaussian estimates, and related nodal positivity horizons with the same rescaled leading constant, are prior or overlapping ingredients. Their exact statements do not imply the continuous derivative sign and both-sided sharp-time obstruction.

## value

PASS

A sharp time for the recovery of a natural geometric shape property under a specified standard spectral cutoff is useful independently of heat-kernel norm estimates. The theorem supplies uniformity in all interior angles and all later times, and quantitative obstructions below the same sharp constant in both parities. The antipodal regime makes mere fixed-time Fourier convergence insufficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
