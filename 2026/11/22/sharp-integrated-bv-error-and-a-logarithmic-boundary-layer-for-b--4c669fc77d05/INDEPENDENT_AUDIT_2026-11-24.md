# Independent mathematical audit

## correctness

PASS

For the canonical right-continuous half-line BV representative, integration against Df reduces the quotient exactly to unit steps. A step in ((j−1)/n,j/n] uses the negative-binomial survival at j, equivalently the CDF of Y=Gamma(j)/Gamma(n) with independent factors. Integrating this CDF by parts gives J (the truncated first moment is j/(n−1) times the shifted beta CDF). The integrated response has second derivative 2 times the positive density, so only the two formal cell ends matter; a jump beyond 1 has a smaller sampled tail than the jump at 1. For s≤1, the response is E|Y−s|−E(Y−1)+, where the last expression denotes the expectation of the positive part. With a=j/n bounded away from zero the centered exponential sum W=(U−aV)/sqrt(n) has variance a(1+a) and uniform Wasserstein normal error O(n^−1/2); Cauchy–Schwarz with E(n/V−1)^2=O(1/n) controls multiplying W by n/V. Thus E|Y−s|=sqrt(2 a(1+a)/(pi n))+O(1/n) at either endpoint. When a→0 the exact inverse-gamma second moments give o(n^−1/2). For the nonstandard tail step, the density has Stirling exponent −nD_a(y) with D_a(y)=(1+a)log((1+y)/(1+a))−a log(y/a), D'_a(y)=(y−a)/(y(1+y)); on a fixed multiple of sqrt(log n/n) near a≈1 Taylor expansion gives a uniform relative 1+o(1) Gaussian density. Chernoff applied to U−yV at lambda=(y−a)/(y(1+a)) gives P(Y≥y)≤exp(−nD_a(y)); Cauchy–Schwarz with bounded second moments then makes the contribution outside a sufficiently wide window negligible. At a=1−c sqrt(log n/n)+O(1/n), the Gaussian excess integral is asymptotic to 2 n^(−1/2−c²/4)/(c² sqrt(pi) log n). The competitor c=sqrt(2) gives the sharp leading limit and a full-moment loss of (3/(2 sqrt(pi)))sqrt(2 log n)/n+O(1/n). Any maximizing sequence must have a→1. Larger fixed c incurs a strictly larger full-moment loss by monotonicity of the variance profile; smaller fixed positive c incurs, by stochastic ordering in j, a tail dominating sqrt(log n)/n. This proves the location limit for every winning pair, unchanged by the 1/n endpoint choice. Verification.md and the supplied Python code were inspected as finite diagnostics, not executed or relied on as proof.

## originality

PASS

The strongest distinct indexed result has the same logarithmic boundary mechanism, not the same operator or theorem. The comparison supports the specific negative-binomial beta-prime norm and retreat theorem, not priority for the mechanism itself.

## value

PASS

Fixed-window approximation of discontinuous half-line data naturally needs the error integrated where observations are available, relative to whole-input variation. The formula gives an exact all-degree benchmark (as a supremum, not an attainment classification). The location law identifies a distinct logarithmically enhanced scale and exact constant for all winning candidates, distinguishing variance gain from boundary leakage in this classical sampler.

The dated certificate retains the supplied scientific assessment, sources and limitations.
