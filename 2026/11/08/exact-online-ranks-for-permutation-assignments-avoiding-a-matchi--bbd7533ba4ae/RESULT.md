# Exact online ranks for permutation assignments avoiding a matching

## Finding
Fix an integer \(n\ge 2\) and \(0\le t\le n\). Delete a matching \(M_t\) of size \(t\) from the complete bipartite graph with \(n\) labeled vertices on each side. Let \(\mathcal H_{n,t}\) consist of the edge sets of all perfect matchings in the remaining graph, regarded as binary functions on the full \(n\)-by-\(n\) edge grid. A query \((i,j)\) returns one if the matching uses that edge.

**Exact online dimension.** The dimension is independent of which size-\(t\) matching is deleted and equals
\[
\operatorname{Ldim}(\mathcal H_{n,t})=
\begin{cases}
1,&n=2,\ t=0,\\
0,&n=2,\ 1\le t\le2,\\
2,&n=3,\ 0\le t\le1,\\
1,&n=3,\ 2\le t\le3,\\
3,&n=4,\ 0\le t\le3,\\
2,&n=4,\ t=4,\\
n-1,&n\ge5,\ 0\le t\le n.
\end{cases}
\]

The corresponding **static comparison**, independently established below, is \(\operatorname{VCdim}(\mathcal H_{n,t})=n-1\) for \(n\ge4\) and \(t\le n-1\), but \(\operatorname{VCdim}(\mathcal H_{n,n})=n-2\) for every \(n\ge2\). In the two smaller orders, \(\operatorname{VCdim}\) agrees with the displayed online dimension. Thus for \(n\ge5\), the full forbidden matching produces the exact gap
\[
\operatorname{Ldim}(\mathcal H_{n,n})-\operatorname{VCdim}(\mathcal H_{n,n})=1,
\]
although deleting any fewer edges of a matching gives gap zero. The previously studied derangement shattering complex is used only as a comparison; the new statement is the complete online-rank phase diagram.

## Assumptions and scope
All graphs are finite, simple, and bipartite; \(M_t\) has pairwise disjoint endpoints and may be empty or perfect. Only membership of a *single candidate edge* is queried at each internal node of a complete binary mistake tree. Forbidden edges, although retained as coordinates in the ambient grid, are identically zero and do not affect either dimension. Relabeling the left and right vertices identifies any two forbidden matchings of equal size. The only claimed infinite-parameter result is for the specified matching-deleted complete bipartite graphs, not arbitrary forbidden subgraphs. An empty class never occurs for \(n\ge2\) in these parameters.

## Proof
**1. General upper bound.** Let \(\mathcal F\) be *any* subfamily of the permutation-matrix concepts on an \(n\)-by-\(n\) grid. Then \(\operatorname{Ldim}(\mathcal F)\le n-1\). For \(n=1\) every such family contains at most one hypothesis. For \(n\ge2\), if a queried edge is positive, its row and column are fixed and deleted, leaving a subfamily of the permutation-matrix concepts of order \(n-1\). By induction this positive branch has dimension at most \(n-2\), so a complete tree of depth \(n\) cannot have that edge at its root. This applies to every root query, including constant-negative ones.

**2. Explicit four-by-four base tree.** Normalize \(M_3=\{(1,1),(2,2),(3,3)\}\). The following is a complete depth-three mistake tree for \(\mathcal H_{4,3}\). The root queries \((1,2)\). After answer zero it queries \((1,3)\), then \((2,1)\) on either child. After answer one it queries \((2,3)\), then \((2,1)\) following answer zero or \((3,1)\) following answer one. All eight response strings occur: their respective witness multiplicities in lexicographic order are \((2,1,2,2,1,1,1,1)\). They can be reproduced by `verify.py`. The upper bound proves \(\operatorname{Ldim}(\mathcal H_{4,3})=3\); including more permitted permutations yields the same rank for every \(t\le3\).

**3. Induction with an unprotected row.** For \(n\ge5\) and \(t\le n-1\), take a row \(r\) untouched by \(M_t\). Select two distinct columns \(c,d\) so that deleting either column removes enough forbidden edges to leave at most \(n-2\) forbidden edges on the \((n-1)\)-by-\((n-1)\) residual board. If \(t=n-1\), take two columns met by \(M_t\); if \(t\le n-2\), any two distinct columns suffice. The query \((r,c)\) has a positive branch exactly equivalent, after removing the fixed row/column and constant coordinates, to \(\mathcal H_{n-1,t'}\) with \(t'\le n-2\). Its negative branch contains the subfamily fixing \((r,d)\), itself equivalent to such a class \(\mathcal H_{n-1,t''}\). Starting at the four-by-four base, both branches have dimension \(n-2\). Hence \(\operatorname{Ldim}(\mathcal H_{n,t})\ge n-1\).

**4. Induction at a perfect forbidden matching.** For \(n\ge5\), normalize \(M_n=\{(i,i):1\le i\le n\}\). Choose any row \(r\) and two different columns \(c,d\ne r\). Query \((r,c)\). Fixing \((r,c)\) deletes the two forbidden diagonal positions associated with \(r\) and \(c\); the positive branch is \(\mathcal H_{n-1,n-2}\). The negative branch contains all hypotheses fixing \((r,d)\), another copy of \(\mathcal H_{n-1,n-2}\). Step 3 gives both branches rank \(n-2\), so the derangement class has rank \(n-1\). This completes the unrestricted online-rank theorem by the upper bound in Step 1.

**5. Small exceptional orders.** At order two, deleting one forbidden edge leaves exactly one matching, whereas the unrestricted graph has two. At order three, the numbers of available perfect matchings for \(t=0,1,2,3\) are \(6,4,3,2\); the first two families shatter two disjoint allowed queried edges, and the last two cannot online-shatter depth two because they contain fewer than four hypotheses. At order four with a full forbidden matching, there are nine derangements. Every allowed edge occurs in exactly three; hence its positive branch has at most three hypotheses and cannot online-shatter depth two. The VC dimension equals two by Step 6, giving online dimension two. All the stated exceptional values follow.

**6. Static comparison, checked independently.** Any shattered edge support is a matching, since every queried edge must be simultaneously positive. For \(n\ge4\) and \(t\le n-1\), it suffices to show rank \(n-1\) when precisely \(n-1\) forbidden edges are removed. Choose the one unused row and column as \(n\) and place a single directed cycle \(\sigma\) on the first \(n-1\) positions. Query the matching \(S=\{(i,\sigma(i)):1\le i<n\}\). For any chosen positive set \(T\subseteq S\), fix its edges. The residual forbidden graph is the union of (parts of) the original forbidden matching and the remaining negative query edges. It has maximum degree two and contains no four-cycle because the union of the two full matchings forms a cycle of length \(2(n-1)\ge6\). If at least three rows and columns remain, Hall's condition holds: otherwise the forbidden graph would contain \(K_{a,m-a+1}\) for some \(1\le a\le m\). For \(m\ge4\) this violates maximum degree two; for \(m=3\) it would be a four-cycle. When two rows remain, the single negative query edge can be avoided by swapping its assignment with the unused row. When one row remains, the unused row and column can be matched directly. Therefore every labeling of \(S\) extends to a permitted perfect matching. No support of size \(n\) can be shattered, since fixing \(n-1\) of its positive edges forces the last. Thus \(\operatorname{VCdim}=n-1\) for this range.

For \(t=n\), let \(S\) be any partial derangement matching of size at most \(n-2\) and fix any subset \(T\) positively. On the residual board of order \(m=n-|T|\ge2\), the forbidden graph is a union of two matchings, with at most \(m-2\) edges from the negative queries. If \(m\ge4\), maximum degree two proves Hall. At \(m=3\), a forbidden \(K_{2,2}\) would require at least two negative-query edges, but there is at most one. At \(m=2\) there are no negative-query edges and the complement of a matching in \(K_{2,2}\) has a perfect matching. Thus every such \(S\) is shattered. Conversely, a matching \(S\) of \(n-1\) queried edges cannot be shattered: if it extends to a derangement \(\pi\), denote its uncovered row by \(a\) and its uncovered column by \(b=\pi(a)\), with \(a\ne b\). Some other matched row \(c\) satisfies \(\pi(c)=a\). Setting all edges of \(S\) except \((c,a)\) positive and that edge negative forces \(a\) to be fixed, which is forbidden. Therefore its VC dimension is \(n-2\). The small-order VC values follow directly from the same reasoning and cardinality bounds.

## Verification
The standalone Python 3 checker `verify.py` uses only the standard library. It enumerates every allowed permutation for every \((n,t)\) through \(n=5\), recursively computes Littlestone ranks from all allowed edge queries, and independently checks VC shattering on all potentially shattered matching supports. It also checks every leaf of the explicit eight-leaf base tree and computes the derangement online rank at \(n=6\). The verified output is recorded in `VERIFICATION.md`. The enumeration is corroborating finite evidence; Steps 1–6 prove every claimed unbounded case.

## Relationship to prior work
The 2018 work of Alon, Livni, Malliaris, and Moran emphasizes the distinct role of Littlestone dimension in learning theory. Ghazi, Golowich, Kumar, and Manurangsi (2020) prove general closure bounds for online dimension, rather than exact dimensions of assignment families. Bucic and collaborators (2019) study perfect matching and derangement counts on graphs, and Johnston, Kayll, and Palmer (2022) study deranged matchings and their asymptotics. Johnson and Wickes (2021) use a different notion of permutation shattering, based on order patterns rather than Boolean edge-membership labels. Classical counting of fixed-point-free permutations and rook placements and the static VC/rook characterization are not proposed as new. The claimed advance is the complete **online** phase diagram, including the fact that forbidding the final allowed assignment position lowers static but not online rank above the sharp exceptional order four.

## Limitations
The proof concerns deletion of a matching in a complete balanced bipartite graph, not arbitrary sparse bipartite graphs or other query models. The finite checker alone does not establish the infinite theorem. A historical equivalence under an alternate online-identification terminology may remain unidentified; no claim of independent mathematical audit is made here.

## References
1. N. Alon, R. Livni, M. Malliaris, S. Moran, *Private PAC learning implies finite Littlestone dimension*, arXiv:1806.00949, first posted June 4, 2018.
2. M. Bucic, P. Devlin, M. Hendon, D. Horne, B. Lund, *Perfect matchings and derangements on graphs*, arXiv:1906.05908, first posted June 13, 2019.
3. B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668, first posted July 7, 2020.
4. J. R. Johnson, B. Wickes, *Shattering \(k\)-sets with Permutations*, arXiv:2112.01946, first posted December 3, 2021.
5. D. Johnston, P. M. Kayll, C. Palmer, *Deranged matchings: proofs and conjectures*, arXiv:2209.11319, first posted September 22, 2022.
