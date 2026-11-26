# Independent mathematical audit

## correctness

PASS

The greedy last index is v_last+2D(v), so presence is exactly D≤k−1. Deleting one letter loses at most one weak descent: at either end the loss is one exactly for a weak descent, and inside it is zero just for 010 and 101. Thus absence with all deletions present gives exactly D=k, both descending boundary pairs, and the pattern exclusions. Each strict ascent is followed by a distinct weak descent other than the first, giving the stated length bound; the k+2 shortest words are the weakly descending words of length k+1. For the transfer computation put t=yz and use suffix series u_00=1+t u_00+y u_01, u_01=t u_11, u_10=1+t u_00 and u_11=1+t u_10+t u_11. Solving yields u_11=1/((1−t)^2−yt^3) and initial weight y²z times u_00+u_10+u_11 gives the displayed rational function. The characteristic cubic is negative at both critical points, so the other roots are a conjugate pair of strictly smaller modulus; the simple dominant pole gives the stated growth rate and constant.

## originality

FAIL

The complete local membership claim and bivariate generating function have exact earlier catalogue coverage. A second earlier record gives even the closed binomial coefficients. This is demonstrated coverage; it does not assert anything about authorship or provenance. No distinct new claim in the frozen statement remains after the comparison.

## value

FAIL

This periodic host is a natural binary test of the gap between shortest and minimal absence, and the exact spectrum is a worthwhile invariant in itself. As a new finding, however, the frozen result only restates an already determined invariant and its elementary consequences. The notation change and check do not provide a substantive independent gain; no supported repair was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
