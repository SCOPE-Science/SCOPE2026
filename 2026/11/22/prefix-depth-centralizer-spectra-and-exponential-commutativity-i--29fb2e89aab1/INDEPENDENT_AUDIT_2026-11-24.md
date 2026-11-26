# Independent mathematical audit

## correctness

PASS

Composition of balanced prefix replacements gives either zero or a balanced pair at the larger input level; inverse swaps the two words. Counting normal forms gives B. Fix x=(u,v) at level m. For a candidate y=(s,t) at j<=m, nonzero xy requires s to be the j-prefix of v and nonzero yx requires t to be the j-prefix of u. Inclusion-exclusion gives (r^j-1)^2 both-zero outcomes; the unique both-nonzero pair commutes exactly when the two prefixes agree. For j>m, both nonzero requires s=va,t=ub; the products are (ua,ub) and (va,vb), equal iff u=v. The two nonzero events have size r^(2j-m) and intersection size r^(2(j-m)), giving the longer summand. Zero and identity commute with everything, including N=0. A common prefix of length d<m is counted by choosing its d letters, an ordered pair of distinct next letters and independent tails, giving the stated multiplicity. On summing with the shorter level fixed, the both-zero term is r^(2h)(r^ell-1)^2; the both-nonzero term is r^ell times r^(2(h-ell)), also valid on the diagonal. After the zero-containing pairs are included, the deficit per level pair is 2r^(ell+2h)-r^(2h)-r^(2h-ell). The lower-order terms total O(N r^(2N)) as N tends to infinity. Writing ell=N-j and h=N-k gives the scaled leading diagonal sum 2/(1-r^(-3)) and the off-diagonal sum 4/((r-1)(1-r^(-3))). Dividing by the squared size factor (1-r^(-2))^(-2) gives the stated positive coefficient. Independently, composition of explicit partial maps on depth-N words matched every tested centralizer and level-pair count at (r,N)=(2,0),(2,1),(2,2),(2,3),(3,2); the last two counts were 5062 and 6298 (python3 /workspace/branches/independent-replay.py 5).

## originality

PASS

The normal form and partial-bijection representation are standard, and a single level is a known matrix-unit object. The checked statements do not cover the balanced finite truncation's cross-level centralizer multiset and sharp pair deficit. This is a best-of-current-knowledge judgment with explicit finite-tree and access risks.

## value

PASS

Balanced prefix maps preserving depth give a canonical family of finite inverse submonoids, rather than a size cutoff chosen arbitrarily. The whole centralizer multiset identifies the role of shared prefixes and allows exact pair counts for unequal levels. A sharp positive coefficient for the vanishing noncommuting mass explains behavior not captured by any isolated matrix-unit level or by cardinality alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
