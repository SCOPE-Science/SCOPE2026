# Independent mathematical audit

## correctness

PASS

The frozen Finding's blanket wording that neither endpoint is uniformly ranked has a counterexample within its stated range: for m=1 the two ranks are (1,2) or (2,1), each with probability 1/2. The complete repaired RESULT.md fixes the marginal wording and retains all moment formulas and m≥1. For m≥2 the proven variance m(m+1)/8 differs from m(m+2)/12 for a uniform rank; the arcsine marginal is classical. For the moment proof, each nonempty increment block is atomless and symmetric, so there are no tied levels and both rank means are 1+m/2. The centered initial count is minus half the prefix sign sum, and the centered final count is plus half the suffix sign sum. Disjoint pairs have zero expected sign product. For overlapping pairs split increments into X_a,Y_b,Z_c, with the overlap Y_b and a+b+c=m. Conditional on the magnitudes, the nonzero signs are independent fair signs, and each pairwise sum has the sign of the larger block in magnitude. The expected product for the prefix and suffix is therefore the probability that |Y_b| is dominant; the otherwise distinct signs average to zero, including zero-length blocks by declaring sign(0)=0. The three possible dominant-block probabilities sum to one (no nonzero ties). Cyclic reindexing of all nonnegative block-length compositions gives a total of binom(m+2,2)/3 for the middle-block probability; b=0 contributes zero. Multiplying by −1/4 gives the covariance. For nested prefixes, the product average is the probability the common block dominates its complement; exchanging their lengths gives complementary probabilities. Thus the variance is [m+sum_{k=2}^m(k−1)]/4=m(m+1)/8, also for the final rank by reversal. Division gives the correlation, including −1 at m=1, and strict increase to −1/3. All random variables used for these moments are bounded signs or ranks, not step heights.

## originality

PASS

The corrected marginal statement is classical, not an originality claim. The supported distinct claim is the exact within-walk covariance and correlation of the fixed-time endpoint rank indices. Accessible near matches use a different pair of variables, an order-statistic value rather than a rank index, or only one marginal. The possible broad 1972 rank-order result remains a concrete access risk, with no established exact coverage in the available evidence.

## value

PASS

Knowing the arcsine marginals leaves the strength of within-walk endpoint rank dependence open. The exact finite-horizon coefficient and limit −1/3 give a usable baseline for ordinal dependence even when steps have no finite moments. The overlap identity explains the invariance structurally rather than just approximating a correlation by a large-sample calculation. Correcting the trivial uniform m=1 marginal does not change this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
