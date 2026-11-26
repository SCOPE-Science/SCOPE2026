# Independent mathematical audit

## correctness

PASS

In K_{2,n}, a simple directed cycle must have length four, and occurs exactly when both mixed columns 01 and 10 occur. Thus acyclic orientations are the union of the two product sets omitting one of those mixed columns, with intersection the product on {00,11}. The one-column character sums for the two sets are 3 at 00, 1 at 11, and opposite signs at 01 and 10; the intersection contributes 2 at 00 and 11, zero otherwise. Factoring proves the exact transform and its multinomial multiplicities. Odd total weight cancels; positive even mixed count yields ±2·3^a; for no mixed frequency columns a zero would require 3^a=2^{n−1}, impossible for n≥2. This also explains the n=1 exclusion. Characters diagonalize counting convolution; all nonzero coefficients are even integers, two mixed frequency columns of the same type and all other columns 11 give 2, and the triangle bound is attained at zero with 2·3^n−2^n. The kernel has half the dimension and the range is exactly the fixed space of all-edge reversal, with the stated positive projection and condition number. An independent exact cycle-test/signed-sum computation at n=2,3 matched all coefficients; the general proof does not rely on it.

## originality

FAIL

A distinct published Resultary record already states the same theorem with the same normalization, and explicitly gives the K_{2,n} orientation interpretation. In the two-row binary matrix encoding, lonesum is precisely the acyclic-indicator event; it is equality of signals on the same binary group, not just equality of counts. The checked older record states the full signed formula, support, gap, rank, nullity, condition number, and recovery projection, and its proof gives the sharp maximum. No unattested priority risk is needed for this rejection.

## value

FAIL

An exact nonvanishing theorem and sharp inverse stability can be mathematically useful, but the audited claim supplies no new utility or invariant beyond the already published theorem on the identical signal. The graph interpretation is already explicit in that source. A new certificate, recalculation, or reformulation would not leave a genuinely distinct valuable remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
