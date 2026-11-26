# Independent mathematical audit

## correctness

PASS

Composing the scalar step gives weights w_j=(1−q)q^(n−j) and deterministic multiplier q^n. At uniform permutation the exact centered-noise variance is s²/(n−1) times the sum of (v_i−v_j)² over i<j; this follows from fixed total and exchangeable coordinates. Pairing replaces v by (w+w∘σ⁻¹)/2, preserving its total. Minimizing this pairwise-difference sum is equivalent to minimizing the cross dot product. Swapping any ascending pair in w∘σ⁻¹ strictly lowers the dot product, so the unique minimum is the reverse order. Because w_j w_(n+1−j)=(1−q)²q^(n−1), exact geometric sums give the two stated variances. The reversed covariance is strictly negative by AM–GM on the nonconstant weights; reverse averages are constant for n=2 only, since the first and second averages differ by (1−q)²(1−q^(n−2))/2. Fresh independent epochs give the exact geometric second-moment sum and unchanged stationary ratio. Independently checked the small-step coefficient by centering the linear and reversal-even quadratic terms in the geometric weights: their leading squared norms give (1−q)² Var((t−mean(t))²)/(4 Var(t))=(1−q)²(n²−4)/60 for uniform t on 0,…,n−1. For q=1−λ/n the centered position profiles after multiplying by n converge to λe^(−λt) and its reversal average; their variances yield U and B. The increasing/decreasing exponential profiles have strictly negative covariance under uniform t, hence 0<B<U/2. The continuum centered moments 1/12 and 1/180 give B/U∼λ²/60; the large-λ terms and the fixed-q geometric sums both give 1/2 in their respective regimes.

## originality

PASS

Best-of-knowledge pass for the exact scoped minimizer/comparison and its calibrated epoch-scale law, not for reversal pairing itself or its known cancellation of the leading order sensitivity. The primary antecedent proves the same paired operation and general variance bounds, not the stated finite-population optimum or exact ratio. The stationarity step alone is an elementary consequence of the exact epoch noise.

## value

PASS

The precise comparison is useful as an exact variance benchmark for a previously proposed way to spend two full passes: two independent same-input passes would give half the ordinary innovation variance, whereas the reverse pair is strictly below that baseline, optimizes the specified class, and has a quantified low-epoch-step advantage and a saturation regime. The full crossover and constants are the useful model result, not merely the classical rearrangement or the affine stationarity formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
