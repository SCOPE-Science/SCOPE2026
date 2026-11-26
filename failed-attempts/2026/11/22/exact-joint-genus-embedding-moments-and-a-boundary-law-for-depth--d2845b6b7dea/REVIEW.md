# Independent mathematical audit

## correctness

PASS

Fix both m and F. Since 2m>F, selecting B is unconstrained and the gap count is F-1-|B|. The irreducibles below 2m are m, the selected m+b, and the interval (F,2m); 2m is reducible. For 1<=i<=r, 2m+i is irreducible precisely when i is missing from ({0} union B)+({0} union B). No integer above F+m can be irreducible. This gives (1) including i=1. At target i, disjoint pairs, one forbidden midpoint if i is even, and the independent requirement of absence of i if i<r give (3) and, summing the odd/even geometric series, (2). The coupling shares all bits through r-1; at r the only extra discrepancy is a newly available bit r, and above r the geometric expected number of holes bounds the probability of any discrepancy. The union bound gives C=3 in (5). The infinite hole probabilities sum to 5/2 over i>=2, giving mean 2 after subtracting the first bit. Two initially absent bits imply W>=1; forcing sufficiently many initial bits present and bounding the remaining tail by monotonicity gives positive probability of W=-1. Tightness and the binomial CLT give (6), uniformly in the permitted choice of m(r). Independent bounded replay `python3 /workspace/evidence/depth_two_exact.py` passed 27 parameter pairs (2<=r<=10, three m per r), 3066 subsets, for (1)–(3); the asymptotics are proved, not sampled. The packaged checker was inspected, not run.

## originality

FAIL

A distinct same-day Resultary record (d2cd7e96a30f) demonstrably covers the core claim; date alone gives no order or historical priority. Under c=m-r, N=r-1, A=B, its count Q_N of positive holes through N+1 in ({0} union A)+({0} union A) is exactly e+g-2m+1. Its exact conditional mean includes the i=1 coefficient, whose normalized contribution is 1-k/N. Its unconditional correction is just the two parities written in one power, and its CLT is the same after equivalent scaling. It gives the same boundary law shifted by one, in a stronger fixed-density conditional setting. The explicit unconditioned TV rate and a short nondegeneracy proof are additional details, but the rate follows by directly summing the inspected source's own odd/even missing-target probabilities and coupling the same bits, and the support distinction uses the same monotone tail bound. No distinct substantive result remains to repair. This is a coverage decision, not an attribution of earlier priority.

## value

FAIL

The exact fixed-genus moment and the tight joint defect alongside a Gaussian marginal would be useful specifications for this natural family, but the same family, finite formulas and boundary statistic are already supplied in equivalent form by the matched finding. The surviving unconditioned TV estimate is the immediate union bound from its displayed geometric probabilities, with no new behavior or sharp rate claim beyond that bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
