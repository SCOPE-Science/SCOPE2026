# Independent mathematical audit

## correctness

PASS

Independently express the centered statistic as n^(-1) times a sum over unordered observation pairs of g(theta_i-theta_j), where g has Fourier coefficients w_|k| for all nonzero signed integer k and zero constant coefficient. Mean zero and integration at a degree-one observation vertex give the variance: only a repeated pair survives and its integral is 2 sum w_k^2. At order three only a triple use of one pair or the three edges of a triangle survive. The former has integral 6 sum_{a,b>=1} w_a w_b w_{a+b}: two choices of sign of the lone-sign frequency and three positions for it. There are binom(n,2) choices of pair. The triangle integral is 2 sum w_k^3 by balancing the signed characters around the cycle, with 6 binom(n,3) ordered triples of edges. Division by n^3 gives both coefficients in the theorem, including n=2, zero weights, and repeated harmonics. Unit weights give M(M-1)/2 ordered additive pairs, yielding the stated skewness after division by the exact variance to power 3/2. For b=4n-11 the sign of the adjacent difference of 3 sqrt(M)+b/sqrt(M) is the sign of 3-b/sqrt(M(M+1)). For n>=3 equality would force the coprime consecutive M and M+1 to both be squares, which is impossible for M>=1. At n=2 the difference is always positive and the minimum skewness is zero. The threshold gives M_opt/n -> 4/3; substitution gives sqrt(n) times the minimal skewness -> 2 sqrt(3). In the other joint limits the leading skewness terms are (3/2)sqrt(M)/n and 2/sqrt(M); this gives the stated limits without asserting a distributional converse. Supplied finite code was inspected, not executed; the unrestricted identities are analytic.

## originality

PASS

The Sobolev family, standard harmonic kernel method and growing-cutoff CLT are prior. The independently inspected strongest matches do not supply the exact weighted signed-frequency cubic count and strict finite integer minimum for this statistic. The pass is for those exact conclusions, not historical priority across all cumulant literature.

## value

PASS

Choosing the harmonic cutoff is intrinsic to the published test. The exact mixed moment detects dependence that the diagonal covariance hides; the finite strict optimizer and the different n and n^2 scales quantify how a real calibration diagnostic changes with cutoff. This is useful without interpreting smallest skewness as optimal size, power or proximity to a Gaussian law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
