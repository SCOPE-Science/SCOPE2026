# Independent mathematical audit

## correctness

PASS

Reconstructed the infinite proof from the three counts x1<=x2<=x3 of zeros preceding the ones. The counts of 011, 101 and 110 are 2x1+x2, 2(x3-x1) and 3(n-3)-x2-2x3, respectively, fixing the integral variation (-t,2t,-t). The difference in sum_i binom(x_i,2) is t(b-c+3t). The sum of the x_i is fixed; equality of this binomial sum fixes the sum of squares and hence both remaining mixed counts. The distinct root t=(c-b)/3 is exactly the stated nonnegative-gap swap, and each doubleton has one representative with c>b. Writing a=t+A gives n-3=4t+2b+A+d, yielding the asserted generating function; its order-four pole with leading factor 1/8 at 1 gives n^3/48+O(n^2), hence 7/8. One representative per fiber is necessary and sufficient. This includes the empty-pair regime n=3..6. A fresh prefix-DP computation of the eight deck counts for every weight-three word through n=17 corroborated the exact fibers and coefficients; e.g. P_7=1, P_16=44 and P_17=56. Replay: /workspace/review-work/small_checks.py deck; output /workspace/review-work/deck_results.txt. This is a finite check of the infinite proof, not a substitute for it.

## originality

FAIL

The complete finding, not only the n=7 example, is covered by distinct earlier-dated Resultary records. The weight and deck definitions, at-most-two fibers, explicit partners, exact pair series, maximum distinguishable codebook, and limiting behavior agree. Same-day matches are additional overlap, not evidence of posting order. No judgment about authorship or global priority follows.

## value

FAIL

The underlying constant-weight classification is structurally useful, but the submitted finding re-establishes the same exact fibers and capacity previously recorded. It supplies neither a distinct regime nor a new implication or independently motivated exact fact beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
