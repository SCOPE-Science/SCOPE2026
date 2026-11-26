# Independent mathematical audit

## correctness

PASS

A rank-one projection is uniquely specified by its image point and complementary kernel hyperplane (a vector/covector pair is unique only up to reciprocal scaling). Distinct commuting projections have zero products in both orders, so adjacency is mutual cross-incidence. Counting hyperplanes gives the stated degree and the arc Gram entries gamma, 0 and beta; AB/BA transfers nonzero eigenvalues through A=UTU^T. For lambda outside 0,beta,+/-gamma, paired arc equations give the denominator lambda^2-gamma^2. Summing over the q other points on a line gives lambda(lambda-beta)d=(lambda^2-gamma^2)S-beta lambda D and D=(lambda-gamma)/lambda times the sum of point totals on the line. Each other point is on exactly one line through a fixed point, yielding (lambda^2-gamma^3)S=beta(lambda-gamma)JS with S nonzero. The constant and mean-zero modes bound multiplicities by 1 and v-1 respectively. The all-ones vector realizes k; the two mean-zero incidence combinations have squared norms 2(q^(n-1) minus/plus sqrt(gamma)) times the squared point-function norm, so realize both exceptional large bands with the full v-1 dimensions. For an adjacent pair, a common neighbor's image is in the intersection of their kernels (s choices) and its kernel contains the two image points but avoids its own (beta choices), so the trace through order three is determined. An independent symbolic check of all four trace identities and the constant-space factorization is in /workspace/audit-replay/3.py. The Vandermonde system for 0,beta,+gamma,-gamma is nonsingular; zero has multiplicity 0. The same script tested the exact integer annihilating polynomial on full matrices at (n,q)=(4,2),(5,2),(4,3), and eight columns at (4,4), with exact degree/common-neighbor checks as documented in 3.txt. The GF(4) probes are not a full matrix census. The analytic argument covers all prime powers, including absence of the +gamma band at q=2, and implies the stated irrationality.

## originality

PASS

Best-of-knowledge pass on the uniform complete adjacency spectrum and nonsingularity, not on the same known cross-incidence graph, its degree, or its local structure. The strongest same-graph Resultary entry gives edge-regular parameters, not a spectrum. No accessible source statement gives a full higher-dimensional antiflag eigenmatrix implying the claim; that possibility remains open as a historical risk.

## value

PASS

This is a complete invariant of a standard projective graph and natural matrix commuting geometry, not a small parameter sample or another degree count. The no-zero result establishes full adjacency rank uniformly, and the two radical bands distinguish integral from nonintegral families. Both conclusions depend on resolving the spectrum beyond the known edge-regularity data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
