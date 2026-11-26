# Independent mathematical audit

## correctness

PASS

For i≠j the common neighbors of a_i and a_j are exactly B minus {b_i,b_j}, nonempty for n≥3. If at most two vertices of B are omitted from X, choose those two excluded indices (padding the pair if necessary); that distance-two pair fails. Conversely three omissions in B defeat every such obstruction, and analogously for A. Adjacent pairs require no internal vertex. For a_i,b_i the shortest length is three: choose omitted b_j with j≠i, then omitted a_k with k≠i,j, obtaining an X-avoiding interior. Thus the feasible choices are independent by part; their enumerator is the squared truncation, the top degree is 2n−6, and each maximal set leaves exactly three omissions per part, giving binom(n,3)^2. At n=3 the graph is C6 and only the empty set qualifies. The frozen verifier independently walks shortest paths by BFS distances for n=3,…,8 and its recorded replay covers 87360 subsets, including degree, coefficients and maximality. I inspected the code and recorded output, not executed it; the proof is unbounded.

## originality

FAIL

Bujtás–Klavžar–Tian, Theorem 5.2, already characterizes precisely these feasible sets in every connected graph by the distance-two common-neighborhood obstructions. On the crown these obstructions are all (n−2)-subsets of each part. Their independence conditions give exactly the claimed sets and all enumerations by direct counting. The original formula need not occur verbatim in the prior paper for this implication to cover it.

## value

FAIL

The natural graph family and explicit enumeration make a clear illustration, but the exact invariant follows mechanically from a published general characterization and counting two independent bounded subsets. The maximal-set count and degree add no separate mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
