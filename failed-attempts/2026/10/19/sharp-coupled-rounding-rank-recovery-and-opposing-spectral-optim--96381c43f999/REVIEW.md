# Independent mathematical audit

## correctness

PASS

Write the row probabilities for 00, 10, 01, 11 as a=1−2p+q, b=p−q, b and d=q. Rank is below two exactly when all nonzero rows occupy at most one direction. Inclusion–exclusion yields F_n=2(a+b)^n+(a+d)^n−2a^n, with the common intersection the all-zero sample. At fixed p the derivative in q is 2n[(a+q)^(n−1)−a^(n−1)], positive at any feasible q>0, so the smallest feasible q is uniquely optimal. Independently, if a>0, replacing zeros independently by uniform nonzero row types preserves equality of the two marginals, never destroys rank, and strictly improves recovery on the all-zero event. Hence the global optimum has a=0. On that edge strict convexity of x^n equalizes the three masses at 1/3, giving p=2/3, q=1/3 and failure 3^(1−n) for all n≥2. The iid-row strong law gives Gram/n with diagonal p and off-diagonal q, hence minimum eigenvalue b≤1/2 with equality exactly when a=d=0. Substitution gives the two condition-number limits and failure probabilities, and at p=2/3, q=p² the leading failure term (5/9)^n gives ratio asymptotic to (5/3)^n/3.

## originality

FAIL

The most relevant indexed result already proves the same three-ray occupancy law and strict separation of rank and spectral optima. The difference in input families is real, but the earlier passage transfers exactly to the no-zero edge, and to the full finite failure law by binomial conditioning. The only extra optimization issue, whether a zero row can improve recovery, is resolved by a monotone replacement that preserves common marginals when p may vary. The spectral scaling, fixed-p boundary and independent benchmark then follow directly from the Gram calculation and occupancy polynomial. The published comparison is mathematical implication, not inference from dates or from matching numerical optima alone.

## value

FAIL

The rank-versus-conditioning distinction is a worthwhile design question, but the earlier model already gives this exact occupancy conflict, failure optima and sharp singular-value tradeoff after direction matching. The remaining zero atom, same-p benchmark, and fixed-p monotonicity are direct conditioning, substitution and a derivative of that law. They do not establish a separate nonroutine invariant or a new design consequence for the stated iid two-column class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
