# Independent mathematical audit

## correctness

PASS

After edge subdivision every link type with at most \(N\) sticks can be represented with exactly \(N\) vertices. A labeled cyclic component decomposition is encoded by a permutation with cycle lengths at least three. Relabeling coordinate slots by \(\tau\) conjugates the permutation by \(\tau\sigma\tau^{-1}\) and induces an isomorphism of the corresponding wall arrangement, so one representative per conjugacy class suffices for ordinary unlabeled links. Conjugacy classes of permutations are exactly cycle types, hence restricted integer partitions of \(N\). The source's fixed-decomposition chamber estimate is uniform and equals \((AN)^{3N}\), so summing over \(p_{\ge3}(N)\) models proves the finite bound; Hardy--Ramanujan gives the subexponential partition factor. The verifier exhaustively confirms the cycle-type/restricted-partition quotient through \(N=9\).

## originality

FAIL

The source manuscript already states that fixed labeled link combinatorics is a cyclic decomposition, equivalently a permutation of the labeled vertices, gives the uniform \((AN)^{3N}\) chamber bound for every such decomposition, and observes that passing to ordinary unordered links only identifies types. Replacing the source's crude count of at most \(N!\) permutations by the elementary conjugacy-class count is therefore a direct symmetry quotient of the exact combinatorial model already printed. Under the required implication-level standard, the improved exponent is an unprinted but mechanically implied corollary rather than an independent result.

## value

PASS

Removing a factorial-scale overcount improves the leading upper exponent for ordinary links from four to three and is therefore quantitatively meaningful. The record fails because the quotient is too directly implied by the source's own labeled permutation model, not because the sharper bound is insignificant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
