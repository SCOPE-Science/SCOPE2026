# Minimal connected-domination spectrum of rectangular rook graphs

## Finding

Let \(m,n\ge2\), let \(R_{m,n}=K_m\square K_n\) be the rook graph with labeled rows and columns, and call \(S\subseteq V(R_{m,n})\) **inclusion-minimal connected dominating** when \(R_{m,n}[S]\) is connected, every vertex is in \(S\) or adjacent to one in \(S\), and no proper subset has both properties. Write \(\left\{\begin{smallmatrix}r\\j\end{smallmatrix}\right\}\) for a Stirling number of the second kind (the number of partitions of \(r\) labeled elements into \(j\) nonempty unlabeled blocks).

**Theorem.** Every inclusion-minimal connected dominating set consists of the edges of exactly one of the following two kinds of labeled bipartite trees, viewing a rook in row \(i\), column \(j\) as the edge \(ij\) of \(K_{m,n}\):

1. A tree spanning **all** \(m\) row vertices and precisely \(b<n\) column vertices, with every selected column vertex of degree at least two.
2. A tree spanning **all** \(n\) column vertices and precisely \(a<m\) row vertices, with every selected row vertex of degree at least two.

The two families are disjoint. In particular, the complete polynomial enumerating inclusion-minimal connected dominating sets by their number of rooks is

\[
\boxed{\mathcal M_{m,n}(z)=\sum_{j=1}^{\min(m,n)-1}\left(\binom nj\,m^{j-1}\,j!\left\{\begin{matrix}m-1\\j\end{matrix}\right\}z^{m+j-1}+\binom mj\,n^{j-1}\,j!\left\{\begin{matrix}n-1\\j\end{matrix}\right\}z^{n+j-1}\right).}
\]

For \(2\le m\le n\), its positive-coefficient degree set is **exactly**
\[
\{m,m+1,\ldots,2m-2\}\ \cup\ \{n,n+1,\ldots,m+n-2\}.
\]
Thus if \(n\ge2m\), there are \(n-2m+1\) consecutive internal zero coefficients, at all degrees from \(2m-1\) through \(n-1\). These are genuine gaps in the sizes of inclusion-minimal connected dominating sets, not absent degrees in an arbitrary domination polynomial. The minimum size is \(m\), and the maximum size is \(m+n-2\). The number of minimum sets is \(n\) when \(m<n\), and \(2n\) when \(m=n\). For \(m<n\), the number of maximum-size sets is
\[
 m\,n^{m-2}(m-1)!\left\{\begin{matrix}n-1\\m-1\end{matrix}\right\},
\]
while for \(m=n=r\) it is \(2r!\,r^{r-2}\).

## Assumptions and scope

Graphs are finite, simple, undirected; all rows and columns are distinguished. The parameters \(m,n\) are integers at least two. Connectivity is required only for the subgraph induced by the chosen vertices, not for its complement. "Minimal" means inclusion-minimal, not minimum cardinality. The polynomial variable \(z\) marks the number of chosen vertices. An empty Stirling number is zero; the displayed summation range never includes such terms for \(m,n\ge2\). No probabilistic, asymptotic, or computational assumptions are required for the theorem.

## Proof

**Incidence translation.** Associate to any set of selected cells \(S\) a spanning subgraph \(H\subseteq K_{m,n}\) containing exactly the corresponding edges; ignore isolated vertices when discussing its connectivity. Two chosen rook vertices are adjacent precisely when their edges in \(H\) share an endpoint, so \(R_{m,n}[S]\) is connected if and only if the positive-degree portion of \(H\) is connected. An unchosen cell \((i,j)\) has no chosen neighbor precisely when row \(i\) and column \(j\) are both completely unoccupied. Thus \(S\) dominates precisely when every row is met or every column is met.

**Removing cycles.** Suppose \(S\) is connected dominating and \(H\) has a cycle. Removing any cycle edge preserves the connected positive-degree part of \(H\), preserves every previously occupied row and column, and therefore preserves domination. Thus a minimal connected dominating set must correspond to a tree. (The one-edge set cannot dominate when \(m,n\ge2\).)

**Coverage on exactly one side.** Suppose the tree meets all \(m\) row vertices and all \(n\) column vertices. Every nontrivial tree has a leaf. Delete the edge incident to such a leaf. The remaining edges are connected, and either all rows remain occupied (if the removed leaf was a column) or all columns remain occupied (if it was a row). Domination survives, contradicting inclusion-minimality. Hence a minimal tree meets all the vertices on exactly one side, and strictly fewer than all vertices on the other.

**Leaf criterion.** If all rows but not all columns are met, a selected column of degree one has an incident edge that can be removed while retaining connectedness and row coverage; therefore every selected column must have degree at least two. Conversely, for a bipartite tree meeting all rows, fewer than all columns, and with every chosen column of degree at least two, deleting a pendant edge removes the sole selected edge from its row (as leaves are rows), destroying domination, since some column remains unoccupied. Deleting a nonpendant edge separates its remaining edges into two nonempty components, destroying connectivity in the rook graph. Thus no edge can be removed while retaining connected domination. More generally, no proper connected dominating subset can exist: if it did, enlarge it within the original connected set one vertex at a time, preserving connectedness and domination, until only a single vertex has been omitted. This would contradict the deletion test. The symmetric argument gives the second family.

**Tree enumeration.** Choose \(j\) selected columns in \(\binom nj\) ways. For a bipartite labeled tree on \(m\) row vertices and \(j\) column vertices, the standard bipartite Prüfer / weighted matrix-tree identity is
\[
\sum_T\prod_{i=1}^{m}x_i^{d_i-1}\prod_{h=1}^{j}y_h^{e_h-1}
=(x_1+\cdots+x_m)^{j-1}(y_1+\cdots+y_j)^{m-1},
\]
where \(d_i,e_h\) are the row and column degrees. For completeness, this identity follows by applying the weighted matrix-tree theorem to \(K_{m,j}\) with edge weight \(x_i y_h\) and dividing its tree enumerator by \(\prod_i x_i\prod_h y_h\); alternatively, the two words in the bipartite Prüfer correspondence have lengths \(j-1\) and \(m-1\), respectively. Set every \(x_i=1\). Requiring every column degree to be at least two is equivalent to each \(y_h\) appearing in the second word at least once; the number of such words is exactly the number of surjections from an \((m-1)\)-set onto a \(j\)-set, namely \(j!\left\{\begin{smallmatrix}m-1\\j\end{smallmatrix}\right\}\). The first word has \(m^{j-1}\) possibilities. Each such tree contains precisely \(m+j-1\) selected rook vertices. The condition \(j\le m-1\) ensures that such a surjection exists, while \(j<n\) is needed for proper coverage of the column side. Therefore the first family contributes the first summand for \(1\le j\le\min(m,n)-1\). Swapping rows and columns gives the second summand. They cannot overlap since a tree in the first family omits a column whereas a tree in the second omits a row. This proves the full polynomial.

**Extremal degrees and gaps.** Assume \(m\le n\). Every Stirling number \(\left\{\begin{smallmatrix}r\\j\end{smallmatrix}\right\}\) with \(1\le j\le r\) is positive. Thus the first family has every size from \(m\) to \(2m-2\), while the second has every size from \(n\) to \(m+n-2\), giving the asserted support and gap. Evaluate the first coefficients at \(j=1\), and the last at \(j=m-1\), using \(\left\{\begin{smallmatrix}r\\r\end{smallmatrix}\right\}=1\), to obtain the stated extremal counts. If \(m=n\), the two symmetric contributions both appear at each extremal size, producing the factor two. QED.

## Verification

The standalone script `verify_minimal_cds_rook.py` constructs the rook graph from coordinate adjacency, tests every nonempty vertex subset for domination and connectedness, then tests every single-vertex deletion; this independently implements the definition rather than relying on the incidence-tree characterization. For nine rectangular boards from \(2\times2\) through \(4\times5\), all \(1{,}413{,}959\) nonempty subsets were examined and the resulting polynomial coefficients agreed exactly with the Stirling formula. The script and its output are embedded separately. These finite computations are consistency checks; the general theorem rests on the proof above.

## Relationship to prior work

Lokshtanov, Pilipczuk and Saurabh (first arXiv version dated 2016-11-02) define inclusion-minimal connected dominating sets and prove a general exponential bound and enumeration algorithm. Abu-Khzam and coauthors (ESA 2022) study efficient enumeration in general graphs, also without a rook-specific cardinality distribution. Mertens (arXiv 2024) determines the ordinary domination polynomial of \(K_m\square K_n\), which counts **all dominating sets**, without requiring connectedness or inclusion minimality. OEIS A289196 and A360876 report counts of **all connected dominating sets** on square and two-row rook graphs; their statements do not enumerate the inclusion-minimal subset by cardinality. The present formula singles out minimal connected sets by the nonleaf condition in a bipartite incidence tree and includes a new explicit internal-gap criterion.

## Limitations

The graphs have two complete factors, each of order at least two; the theorem does not address products of more factors, ordinary minimum dominating sets, all connected dominating sets, or unlabeled isomorphism types. The bipartite degree-enumerator identity is classical; its application to this precise minimal connected-domination classification is the issue here. The literature comparison is not a mathematical proof of priority, and it cannot exclude equivalent unpublished, differently named, or unindexed edge-domination results. No independent external scientific audit has been performed.

## References

1. D. Lokshtanov, M. Pilipczuk and S. Saurabh, *Below all subsets for Minimal Connected Dominating Set*, arXiv:1611.00840v1 (posted 2016-11-02), https://arxiv.org/abs/1611.00840.
2. F. N. Abu-Khzam et al., *Enumerating Minimal Connected Dominating Sets*, ESA 2022, DOI 10.4230/LIPIcs.ESA.2022.1, https://doi.org/10.4230/LIPIcs.ESA.2022.1.
3. S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716v1 (posted 2024-01-01), https://arxiv.org/abs/2401.00716.
4. OEIS A289196, connected dominating sets in square rook graphs, https://oeis.org/A289196.
5. OEIS A360876, connected dominating sets of two-row rook graphs, https://oeis.org/A360876.
