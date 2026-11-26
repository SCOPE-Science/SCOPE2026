# Independent mathematical audit

## correctness

PASS

For i<=j-2 the record and peak use disjoint observations; for i>=j+2 the insertion rank determining the record is independent of the preceding internal order, which determines the peak. On the three remaining diagonals the respective joint probabilities are 1/((j-1)(j+1)), 1/(j+1) and zero. For the first probability, given R_(j-1), the first j-1 maximum has density (j-1)x^(j-2), and the two new observations produce a peak at j with probability (1-x^2)/2 conditional on this maximum. The second joint event is precisely that the first j+1 maximum occurs at j; the third is impossible. Subtracting 1/(3i) gives the frozen kernel, including the zero at j=2,i=1. The column sum is 1/(3j(j-1)(j+1)); partial fractions telescope to the stated total. The independent insertion ranks give the record variance. For two peaks at lag two, conditioning on the shared observation x yields joint probability integral_0^1 ((1-x^2)/2)^2 dx=2/15 and covariance 1/45; lag one is incompatible and greater lags are independent. Summing gives peak variance 2(n+1)/45 for n>=4 and the separate 2/9 at n=3. The claimed correlation and its asymptotic then follow with the stated n>=4 convention.

## originality

FAIL

The distinct Resultary record 9c70121babad states the same position-resolved theorem, not merely a related aggregate, and gives the same strictly positive column sums and total covariance on the identical full domain. The frozen correlation is a normalization by the marginal variances and does not leave an independent scientific contribution. This is a finding of equivalent coverage, not priority: the comparison record is catalogue-dated November 8 and the frozen record November 2; dependence or a chronology beyond those dates is not inferred. Published aggregate formulas are also relevant, but the direct indexed kernel, not an unverified implication from a count generating function, is decisive here.

## value

PASS

As mathematical content the complete position-resolved law is structurally useful for mixed second moments of weighted sums of two classical permutation statistics. It identifies pairwise independence off the three diagonals and an exact cancellation within every column that accounts for the order-one total. This is value of the full structural result, not an independent value claim for routine correlation normalization or for duplicating the indexed theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
