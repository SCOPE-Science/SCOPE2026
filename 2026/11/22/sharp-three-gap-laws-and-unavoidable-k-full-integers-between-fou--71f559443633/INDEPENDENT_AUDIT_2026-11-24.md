# Independent mathematical audit

## correctness

PASS

For each prime exponent e≥k with nonzero remainder j mod k, remove one copy of k+j and put the remaining multiple of k in A^k; remainder zero goes entirely in A^k. Thus the arithmetic families are disjoint. Each λ>2 is irrational and no positive multiple is an integer, so there are no endpoint exceptions. In the local phase x={n/λ}, the first window contributes for x≥1-p. An adjacent pair would need two integer crossings in length 2p<1. Conditional on the first crossing, the third crosses the next integer precisely at x≥2-3p (x+2p<2), giving overlap length (3p-1)_+. The three marginals and this overlap give the five listed probabilities. The independence input is valid directly from Besicovitch's standard independence of distinct prime-radical monomials with exponents in {0,1/k,...,(k-1)/k}: λ^(-1) is a rational multiple of the monomial with exponent (k-j)/k at each prime put in b_j, giving distinct exponent vectors including the constant. Kronecker–Weyl now gives the finite products. The omitted-scale hit fraction is bounded by 3(1+3/X) times the reciprocal-scale tail, since each multiple can hit at most three starting indices. The reciprocal series is bounded by the stated finite zeta product. This proves each natural density and convergence to the independent-factor count law, with a uniformly convergent PGF on the closed unit tridisc. Only powers of the prime two can give λ<3, and equality λ=3 is impossible. The admissible j are exactly 1 through floor(k log₂(3/2)); every interval (n,n+3) contains a positive multiple from each such scale. All three singleton choices of each forced scale have positive probability, and unforced scales have both positive singleton probabilities and a positive infinite all-zero product after any finite assignments. This proves the complete support. The limiting sums converge in L² by summable means and variances, so the covariances add over independent scales. Their difference is (3/2)r(1-r^J)/(1-r)-J for r=2^(-1/k), J=J_k; expanding gives k(1/2-log(3/2))/log 2+O(1) with absolute remainder, and J≥1 for k≥2 gives strict positivity. No empirical second-moment claim is used. Both frozen scripts were inspected, not executed.

## originality

PASS

The supported distinct claim is the count-valued three-window factor with its endpoint overlap and the exact support and covariance consequences. The two-window independence method and a qualitative four-power nonemptiness observation are credited to Narumi–Tachiya, with residual uncertainty about prior general finite-window coverage.

## value

PASS

Three adjacent power gaps are a natural first setting where the same scale can hit nonadjacent windows. This produces more than a larger PGF: it characterizes the exact lattice support, sharpens uniform nonemptiness to a pointwise floor growing with k, and quantifies the lag-two change in the limiting count covariance. These are usable structural facts about k-full occupancy, not claims about empirical moment rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
