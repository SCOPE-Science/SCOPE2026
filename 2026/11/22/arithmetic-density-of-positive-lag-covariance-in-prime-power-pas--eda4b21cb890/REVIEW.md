# Independent mathematical audit

## correctness

PASS

Kummer reduces the fixed column to v_p(floor(n/p^a)). For quotients q in [1,K] and fixed c≥0, the frequency of v_p(q+c)≥j is bounded by (1+c/K)p^(−j); summing the square tails and applying Cauchy–Schwarz justifies removing bounded periodic truncation. For a nonzero shift of depth d the incompatible part of the joint threshold sum is exactly p^(−d) times the unshifted second moment. The two translated quotient shifts receive weights (r−u)/r and u/r for h=rt+u. If one shift has depth d≥1, the corresponding weight must exceed p^d/((p+1)(p^d−1)); equality cannot hold because its reduced numerator after multiplication by r has p-valuation a+d, and the denominator is prime to p and >1. Depth infinity likewise has no tie. Counting the two remainder sets gives 2r−1−2c_d, including endpoints, and the valuation layers each have frequency (p−1)/p^(d+1). For d≥a+1 the increment above r/(p+1) is <1/(p+1), hence no floor change. In fact the sign alone is periodic modulo p^(2a+1) since the stabilized threshold includes depth infinity; the covariance need not be periodic. The proof's tail argument does not require periodicity. Replacing c_d by rg_d changes the weighted answer by at most 1/(pr) and the remaining series simplifies to the claimed Lambert sum. All four stated numerical examples agree. The swapped ordering of u and r−u in the tie sentence does not affect the symmetric impossibility argument.

## originality

PASS

Credit the local valuation autocovariance as prior framework, with an exact overlap in the odd-prime case. What survives is the all-lag sign count for the mixture induced by the positive-depth column, including p=2, the finite rational expression and the quantitative Lambert-series limit.

## value

PASS

The sign density for a natural family describes how often a random lag reinforces, rather than merely how large an autocovariance can be. Exact residue arithmetic resolves nonvanishing, all finite depths, and a limit with controlled error. This is usable both to classify finite lag residues and to compare columns of different depth; it is not the routine single-valuation correlation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
