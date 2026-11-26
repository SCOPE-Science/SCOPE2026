# Independent mathematical audit

## correctness

PASS

The Finding follows under its exact hypotheses from Fairfax-Ball Theorem 4.3 and Kummer. The first admissible row is 2m and k=m is its only selected index. Thus the row is extremal iff the central binomial valuation equals r. In the doubling of an r-digit m there are at most r outgoing carries, one at each occupied position; the final leading digit cannot generate another. Equality is exactly an outgoing carry at the units position with input zero and at every higher position with input one. This proves the two digit thresholds and the binary all-ones case. For odd p the permitted top digit is nonzero automatically, and multiplication of the choices gives precisely the stated count, including r=1 and m>=2. The all-(p-1) digits of p^a-1 obey both thresholds. Independent comparison using sums of floor quotients for the factorial valuations agreed in 369 parameter cases (p=2,3,5,7,11, 2<=m<=100, p not dividing m); 16 odd-prime digit-length counts also agreed.

## originality

FAIL

No inspected source states the full classification in this exact wording. Nevertheless it is a mechanical corollary of the known maximum, the definition of the first extremal row, and Kummer's exact valuation theorem: at the first row only a single coefficient exists. The identified restricted-GCD subcases already cover some inputs explicitly. No claim is made that an earlier paper printed the whole digit-count formula.

## value

FAIL

The least extremal row is a natural invariant, but this particular branch collapses just by evaluating the unique coefficient at the first permitted row, then applying the standard carry rule and multiplying independent digit choices. The result gives no new mechanism for finding a first extremal row beyond the already decided singleton case. This is a routine deduction, not a further exact obstruction or a resolution of a nontrivial part of the least-row problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
