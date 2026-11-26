# Independent mathematical audit

## correctness

PASS

For independent Brownian walkers the dimensionless no-reset survival is erf(t^(−1/2))^N, so the k-th raw moment is 2k times the stated u-integral, which is finite exactly for N>2k. Under the common independent exponential clock it is a reset before completion that renews the whole ensemble. Laplace-transforming this renewal equation gives F(q+s)/(1−qF(q+s)); the denominator at s=0 is strictly positive since there is positive probability of completing before reset. Differentiation in s gives the mean and second moment and their variance quotient in RESULT.md. Dominated differentiation at q=0 uses only three baseline moments, including for N=7. In particular C=−2F′/F²−1, so the cancellation leaves C′(0)=G_N/m₁³. A strict right derivative fixes the difference from the zero-rate value for sufficiently small q>0, not global monotonicity. Independently ran `python /workspace/reproductions/check_reset_intervals.py`: Machin's π identity and alternating series bound 2/√π; integer-directed Horner evaluation brackets erf using truncations at indices 109 and 110; exact rational cell weights with directed sums use monotonicity. The first cell uses erf(u)≤(2/√π)u, and the upper tail uses erfc(4)≤exp(−16)/(4√π)<2e−8, proved with a lower Taylor bound on exp(16). Rational arithmetic confirms every strict sign for N=7,…,12. For the tight G_11 case an outward bracket is [−0.001981,−0.001197]. The frozen script's 75-digit Decimal arithmetic does not literally direct every final rounding outward; the independent certificate closes that gap for the signs and supports the displayed rounded brackets. No signs are inferred for other N or finite rates outside a local neighborhood.

## originality

PASS

The distinct claim is the joint local comparison of the absolute variance and squared relative dispersion with the known positive mean slope, not the resetting model, general renewal formulas, or mean transition.

## value

PASS

At and immediately above the known mean threshold the six natural population sizes exhibit three strict risk tradeoffs: variance may fall as the mean grows, or absolute variance may rise while relative dispersion falls, or all may rise. This is useful for choosing a risk measure under common-clock restart. The certified comparisons add information not available from the mean optimum or a curve fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
