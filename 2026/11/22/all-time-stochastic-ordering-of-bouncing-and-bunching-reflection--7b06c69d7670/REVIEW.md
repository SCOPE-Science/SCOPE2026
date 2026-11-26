# Independent mathematical audit

## correctness

PASS

Reconstructed the wall rows: only the outward forward move from w=(1,-1) changes, from a self-loop to u=(1,+1), with the same one-step absorption vector. Subtracting the first-step equations gives z f (I-zQ_B)^(-1)_{i,w}(F^U_u-F^U_w). The two bunching wall exit laws are geometric with parameters f and b and share the same continuation H from (2,+1), or H=1 for N=2. Their PGF difference has numerator z(f-b)(1-z)H; the 1-z cancels for cumulative probabilities. The remaining product has nonnegative coefficients. For N>=3 a leftward run reaches w, using a reverse step first if needed; a right-facing walker at site 1 can first move to site 2 and reverse. H has a positive coefficient from a rightward run. For N=2 only w reaches w, and equality at f=b is of hitting laws, not of transition kernels. Positive probabilities of finite rightward runs give almost-sure absorption. Inspected VERIFICATION.md and the finite exact replay path python3 check.py in the frozen directory; did not execute the uploaded program. The infinite proof is algebraic, not based on the reported 40 systems.

## originality

PASS

The predecessor has the same reflection conventions and general first-passage machinery, but the distinct supported contribution is the coefficientwise CDF order, including its sign reversal, equality and start-dependent strictness. The nearby catalogue records examined do not cover that theorem.

## value

PASS

The law-level comparison determines one protocol for every deadline and increasing hitting-time cost for a natural transport model, rather than choosing by a mean or a single peak. The reversal threshold and the sharp two-site exception explain when the choice actually changes a deadline probability. It does not assert pointwise mass ordering or extend to partially absorbing targets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
