# Independent mathematical audit

## correctness

PASS

For n>=3 and q>0, Z_n(q)=∏_{k=1}^n[k]_q by Mallows insertion. Deleting fixed boundary entries gives P(I1)=P(In)=1/[n]_q and P(I1I2)=P(I1In)=1/([n]_q[n-1]_q). For I2, splitting on pi(1)=1 or k≥3 yields 1+∑_{k=3}^n q^k in the numerator because first value k creates k−1 inversions and second fixed value 2 creates one with residual value 1. Covariances follow exactly by cancellation. q^{n-1}/(1+q) is strictly increasing (n>=3), so one root >1 and it strictly descends to 1 in n; log(1+e^h)=log2+h/2+O(h²) proves n log r_n=log2+(3 log2)/(2n)+O(n^-2). For q=e^{β/n}, q-integers/n converge to L(β), providing cubic covariance limits; at β_n=log2+t/n the adjacent numerator equals (3 log2-2t)/n+O(n^-2), giving quartic crossover. For n=2, indicators coincide with covariance q/(1+q)^2. Fresh independent exhaustive weighted enumeration for n=3..7 and six rational q values verified six exact formula families per case (30 cases); independent root bisection, critical-scaling checks, and seven-entry Git tree reconstruction corroborate. Finite checks are not a proof of all-n statements.

## originality

PASS

Best-of-knowledge, the exact finite-n signed comparison of two natural positional fixed-point pairs, the unique boundary threshold q^{n-1}=1+q, and explicit n^-3/n^-4 weak-bias crossover are not implied by the specific statements inspected in the most closely matched primary work. Mallows law, inversion enumerators, fixed-point cycle counts and first-order weak-bias independence are prior; the signed pair dependence is the precise surviving claim. Closest Resultary hits either are this same claim or concern mixed statistics, q=1, Ewens, or other ranking measures. A q-rook derivation in unindexed literature remains a real priority risk.

## value

PASS

The two boundary pairs have the same two-site joint fixed probability but different second-site marginals, giving a mathematically motivated dependence contrast. The exact finite-size attraction/repulsion phase, strict monotonicity of threshold with n, first negative case n=3, logarithmic scaling constant and quartic critical window are a complete exact classification of these named local observables in a classical nonuniform permutation model. This natural sign-reversal and sharp crossover is not merely renaming of a known constant or a single arbitrary numerical evaluation; does not claim all-position correlations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
