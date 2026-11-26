# Independent mathematical audit

## correctness

PASS

On basis triples the only nonautomatic associativity constraints are a_ij e_j^2=0 for i≠j. For the active row set S, the permitted columns of row i in S are exactly {i} union S^c, and row i must be nonzero; annihilation is tested by multiplying separately by each e_i. For a_i=a_ii≠0, e_i^2/a_i^2 is an idempotent with its own one-dimensional field ideal and e_i-a_i(e_i^2/a_i^2) is in the annihilator. The remaining active rows have square in the annihilator; together with the annihilator their span is a cube-zero ideal. This identifies T intrinsically as the dimension of the quotient by the nilpotent ideal. Among permitted rows there are (q-1)q^(n-s) with nonzero diagonal and q^(n-s)-1 nonzero rows with zero diagonal; row and support choices give the exact joint count, including s=n and the empty support. The exponent s(n-s+1) at s=m+j is m^2-j^2 in odd size and m(m+1)-j(j-1) in even size. Centered binomial ratios are at most one (m is a binomial mode for both parities), the nonzero-row corrections are at most one, and both factors tend to one for each fixed j. The lattice weights therefore give summable majorants after assigning zero to invalid j, which proves the total asymptotics and tightness. The conditional binomial parameter is p/(1-q^{-(n-s+1)}); for fixed j the conditional mean differs from pm by pj+o(1) and the variance divided by mp(1-p) tends to one. Applying the binomial CLT for each fixed j and then using tightness to truncate the sum of conditional laws gives precisely the independent joint weak limit.

## originality

PASS

The normal form and cube-zero decomposition are credited to prior work; the exact labelled count is a short consequence of the support form and is not independent novelty evidence. The finding's distinct contribution is the parity-dependent annihilator law, independent Gaussian semisimple law and accompanying exact and asymptotic census for that precise ensemble. The closest checked analogues do not cover this joint limit.

## value

PASS

The two parameters are intrinsic and track different algebraic structure: how many directions survive annihilation and how much of the algebra is semisimple. In a natural finite-field labelled ensemble, identifying one as parity-pinned on a lattice and the other as asymptotically independent at square-root scale gives substantially more distributional information than the standard classification, a total count, or a Gaussian approximation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
