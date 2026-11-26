# Independent mathematical audit

## correctness

PASS

If m=ba+r with 0≤r<b, rounding either m/b or (m+1)/b produces only a or a+1, even at an integral endpoint. Unbiasedness fixes the weight on a+1, so induction proves the law for arbitrary successive reciprocal-integer denominators and order independence of the terminal law. For any nonreciprocal real q, m=⌊1/q⌋ satisfies 0<mq<1<(m+1)q<2. The interval (m/q,(m+1)/q) has length >1 and contains a positive integer k, giving positive intermediate mass at both m and m+1 and positive terminal mass at 0, 1 and 2. This disproves collapse for all k already at two steps, not necessarily at each k. With j=⌊μ⌋, E[(Z-j)(Z-j-1)]≥0 gives the stated variance bound and equality condition; the three-atom witness makes it strict. For q=2/5 and k=6, exact composition gives masses (3,20,2)/25, mean 24/25 and variance 124/625 versus the single-step 24/625. Zero is absorbing, so the tail is min(1,k/b^n); summing it from n=0 gives the claimed expectation, including k=1 and exact powers of b. These are exact fixed-grid results; neither floating-point arithmetic nor arbitrary slopes or initial states are implied. The frozen rational script was inspected but not run; the main checks are analytic.

## originality

FAIL

A distinct Resultary record, 374d6aac7770, states the same full two-step iff, nearest-neighbor law for mixed reciprocal denominators, variance formula and extinction law on the same state space. Its displayed survival and mean formulas are equivalent, and it additionally analyzes the logarithmic phase. This is demonstrated statement-level coverage, not a claim about who had chronological priority. The frozen variance-minimum corollary and its numerical witness do not provide an uncovered substantive theorem. No repair is proposed.

## value

FAIL

The exact collapse and absorption laws would be useful in an idealized fixed-grid model, but those precise facts are already available in the matched result. The distinct remainder is a routine variance-minimum inequality for any integer marginal, its immediate application to a covered witness, and a numerical illustration. It does not establish a separate worthwhile mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
