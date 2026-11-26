# Independent mathematical audit

## correctness

PASS

In the inclusion–exclusion formula, the discarded even-base terms after division by 8! have valuation at least n−5, as the potentially limiting coefficients 28 have valuation 2. Thus the stated tail cutoff suffices. Re-expanding the retained odd bases by 49=1+48, 25=1+24 and 9=1+8 gives the two normalized branches G(t)=F(2t), H(t)=F(2t+1)/4, with integral Mahler coefficients, odd linear coefficients (17 and 21 before division by −315), and quadratic coefficients of valuations 3 and 2. The higher coefficients have valuation at least 3j−4 and 3j−6 respectively. Vandermonde bounds the binomial differences below by ν₂(t−s)−floor(log₂ j); hence each nonlinear difference has strictly higher valuation than the linear term. Both branches induce permutations on every quotient. In a block of length 2q the even branch takes every residue once, and the odd branch takes each multiple of four four times for k≥2, degenerating to two zeros at k=1. No odd shift can be a period because odd indices never give odd output and infinitely many even indices do. An even shift 2d forces q|d by even-branch isometry. The parity mixture gives the stated Haar density. Independently checked two full blocks, a half-period obstruction and both branch histograms at k=1 through 12 using the product ordinary generating function, not the uploaded checker (python3 /workspace/branches/independent_checks_2_5.py). Neither the proof nor the test claims the cutoff is sharp.

## originality

FAIL

Davis's 2014 proof of Theorem 2.1 explicitly establishes a dyadic first-difference valuation (4.4) for the partial Stirling function. At e=2 and Δ=4 it gives precisely the two normalized isometries needed here, not just the zero counts named in the frozen literature comparison. The full fiber table, least period and density follow by finite quotient permutations and counting, and the sufficient cutoff follows by reading the even-base coefficients in Davis's Proposition 1.5 proof. The final table need not appear verbatim in that paper for the claim to be covered as a mechanical corollary.

## value

FAIL

The exact pushforward for a natural Stirling column is worth understanding, and the short Mahler computation is a useful exposition. As a distinct research contribution, however, this record extracts the histogram and density by routine quotient counting from already established branch isometries and uses a merely sufficient cutoff obtained by direct evaluation of the existing error formula. No resolved new obstruction, stronger cutoff or otherwise independently useful new remainder survives that comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
