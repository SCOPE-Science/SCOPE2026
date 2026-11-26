# Independent mathematical audit

## correctness

PASS

Conditioning on the fixed site preserves exchangeability at any window not containing it, giving actual independence of the two indicators. In a window containing it, the two other values form a uniform ordered pair; selecting r−1 below j and 3−r above j uniquely determines the ordered pair for the specified pattern. Summing the three incident counts and subtracting (n−1)(n−2)/2 in the common numerator yields in order 123,132,213,231,312,321: n−1, −3i+2n−3, 3i−n, 3i−2n+2, −3i+n−1, 3−n. This checks all endpoint signs, the degenerate 321 zero at n=3 and the peak/valley cancellations. The conditional mean uses P(A)=1/6 and E[F]=1. The proof is exact and independent of the numerical counter.

## originality

FAIL

A distinct same-date indexed four-pattern record contains the exact site-by-site conditional law for every single window of length four in the proof, even though its headline tables are aggregate. For any length-three window and n≥4, extend it at one end to a length-four window, and sum that conditional law over the four distinct ways to insert the rank at the extra position while preserving the order of the original three entries. This yields the full local law including off-window independence, hence the centered six profiles and signs by exact arithmetic. The n=3 cases are the six individual permutations (fixed-point counts 3,1,1,0,0,1 in table order). The later all-length record supplies another explicit implication. This is a coverage finding, not a priority finding against the same-date record.

## value

FAIL

The sign profiles are intelligible and the position-specific covariance is a motivated statistic, but the exact table is a fixed four-way marginal of previously available evidence, and signs and cancellations are simply arithmetic on it. No independently valuable non-implied remainder is identified; the width-three boundary at n=3 is immediate from six permutations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
