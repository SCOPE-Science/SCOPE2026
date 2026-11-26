# Independent mathematical audit

## correctness

PASS

A specified split pair is a cherry exactly when the other keys avoid its maximal common-prefix cylinder. For multiple prescribed disjoint pairs, the cylinders must be disjoint (otherwise at least one pair's cylinder contains a third key), and the remaining keys must avoid their union. Conditional on the lengths, the cylinder words are independent uniform words, so either containment for a pair has probability equal to its larger mass. On epsilon<=nX_i<=M this gives O(r^2 M/n) relative error in the conditional disjointness factor; the binomial-to-product comparison has relative error O_r,M(1/n) by Taylor expansion. Outside the band the joint contribution is bounded by products of one-dimensional exponential sums, since 1-sum X_i<=product(1-X_i) for disjoint cylinders. Summing X/2 over the small dyadic X gives O(epsilon/n); on the upper side the weighted sum of X exp(-nX/2) is O((M+1)e^(-M/2)/n) by geometric doubling. For the mean, when X<=1/2, |(1-X)^(n-2)-exp(-nX)|<=C( X+nX^2 )exp(-c nX) for large n, and X=1 contributes exponentially little to the approximant. Summing dyadically gives the stated O(1/n) after multiplying by n. In Proof §3 the missing tail is j>k (far positive), not far negative; it is the exponentially small tail. The Fourier coefficient follows by integrating one period at frequency h and substituting u=2^(s+j); it is Gamma(1-2*pi*i*h/log(2))/(2 log(2)). Positivity, continuity, nonconstancy and phase density (e.g. n=floor(2^(k+s)) for s in [0,1)) then settle the absence of an unphased law. Disjointness gives exactly (n)_{2r}/2^r ordered r-edge choices. Factorial moments along phase subsequences identify the Poisson by moment determinacy; ordinary moments are sums of factorial moments, and pointwise convergence on the integers plus tightness gives total variation. For q>=3 it is the second factorial moment, not the ordinary second moment as the last proof paragraph calls it, that is O(n^(4-2q)); the formula immediately preceding it is already for factorial moments, and this is the quantity required by Bonferroni. These two slips do not change the argument or theorem. The n=2 pair probability uses the usual empty avoidance product 1.

## originality

FAIL

The core asymptotic collision laws are direct consequences of the known same-model concentration of one-tree cherry counts and the distribution-free overlap formula for independent exchangeable matchings. The latter is explicit in a separate already-published record bearing the same publication date; this review does not infer time-of-day priority between the records. The combined premises cover the proposed limit, not merely its mean or a different tree model. The alternative direct cylinder proof is valid but does not establish a distinct original theorem of the stated scope.

## value

PASS

The probability of concordance between independently built indexes with persistent labels is a meaningful benchmark: two replicates retain a nondegenerate calibrated overlap, whereas three or more rarely agree, and an exact small phase modulation precludes a fixed reference Poisson. This is meaningful as a benchmark, independently of whether it merits a new result. The valid direct proof and finite example do not rescue the originality of the frozen finding; no separately motivated new remainder is established here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
