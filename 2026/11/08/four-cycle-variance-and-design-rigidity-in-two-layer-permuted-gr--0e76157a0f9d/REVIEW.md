# Independent mathematical audit

## correctness

PASS

For all binary d-by-d regular incidence matrices with row and column degree r, 2<=r<=d-2, two independent uniform interlayer permutations reduce the second-step pile support to a uniform r-subset S. Pair-collision statistic C2 equals sum_{u<v in S} c_uv with row codegrees c_uv, common mean mu=r(r-1)/(d-1). Centered h_uv=c_uv-mu has zero row sums, so identical, adjacent and disjoint ordered edge-pair contractions are H,-2H,+H. Inclusion rates alpha=(r)_2/(d)_2, beta=(r)_3/(d)_3, gamma=(r)_4/(d)_4 give Var(C2)=(alpha-2beta+gamma)H = r(r-1)(d-r)(d-r-1)H/[d(d-1)(d-2)(d-3)], strictly positive coefficient. Constancy iff all row pair intersections equal mu, equivalently symmetric 2-(d,r,mu) design, necessarily integer mu. Identity H=2C4+d*binom(r,2)-binom(d,2)mu^2 follows from counting K_2,2 motifs. Independently verified exact first and second moments across many circulant matrices d=4..9, r=2..d-2; d=7 r=3 design variance0 vs consecutive offset variance 6/5. The proof quantifies all matrices, finite checks only corroborate.

## originality

PASS

Best-of-knowledge originality follows from statement-level and implication-level comparisons; no identified complete earlier theorem covers the stated surviving exact result. See structured checks, inspected source material and risks.

## value

PASS

Exact graph-geometry sensitivity of a natural finite-depth collision fluctuation, and zero-variance rigidity precisely for symmetric incidence designs, identify the first nontrivial observable beyond geometry-independent expected occupancy. The bipartite four-cycle count is a single motif controlling this variance; comparison of same-size regular graphs with variances 0 and 6/5 is a motivated explicit structural distinction, not mere numerical tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
