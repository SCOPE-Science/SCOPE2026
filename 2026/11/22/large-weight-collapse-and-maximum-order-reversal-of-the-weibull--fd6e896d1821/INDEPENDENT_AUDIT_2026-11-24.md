# Independent mathematical audit

## correctness

PASS

The profiled Weibull scale enforces sum Y_j=n. Writing A(t)=n^{-1}∑(tY_j−1)_+ and d(t)=t e^{−1/t}, the empirical-minus-null difference is d−A. For any positive mean-one vector A=0 on (0,1/n], and both minCFs are in [0,1], so the absolute error relative to the common integral is bounded by the integral of (1+t²)e^{−γt} from 1/n onward. Integrating gives all displayed coefficients. The common integral is the K_3 integral, whose saddle at t=√(2/γ) gives the stated factor 2^{5/4}√π. In the joint regime the relative error is bounded by a polynomial prefactor times exp(−γ/n+2√(2γ)), which tends to zero uniformly. For fixed data A first becomes active at t_0=1/M, with slope rM/n just to the right, so n(2dA−A²)=2r e^{−M}(t−t_0)+O_Y((t−t_0)²). The further tail is polynomially bounded and exponentially smaller. Integrating the linear onset gives the negative correction to T with relative O_Y(1/γ) error. Deficits for a larger M eventually dominate those for a smaller M at fixed common n, regardless of ties within either sample. Independent 80-digit replay for the fitted raw sample (1,e,e), r=2, found correction-to-prediction ratios 1.03308, 1.01458, 1.00677 at γ=40,80,160, and checked the bound. The proof, not the quadrature, establishes the limits.

## originality

PASS

The minCF test, standardization, exponential weight, and even the K_3 term as a summand of its exact kernel are prior. The supported distinct conclusion is that this term leads the whole statistic at diverging weight, with a sharp tied-maximum deficit that reverses sample order, and a uniform bound for mean-one arrays. The bounded comparison does not certify global priority.

## value

PASS

The result diagnoses what this specific existing fitted goodness-of-fit statistic actually compares at high weight. Its apparent fit discrepancy becomes sample-independent to leading order, yet the first visible ordering is by decreasing score as fitted maxima increase. This distinction between collapse of magnitude and retention of an extreme-based ordering is useful when interpreting weight sensitivity or numerical cancellation. The growing-n bound supplies a deterministic regime rather than an extrapolation from fixed examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
