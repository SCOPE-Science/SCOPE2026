# Minimal connected domination of rook graphs: a Stirling polynomial and unbounded spectrum gaps

## Finding

For integers \(m,n\ge 2\), let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\) be the rook graph whose vertices are the \(m n\) cells of a rectangular board and whose edges join cells in a common row or column. A connected dominating set is a nonempty vertex set inducing a connected graph and dominating every vertex by its closed neighborhood. It is *inclusion-minimal* if no proper subset has those properties.

Let \(S(a,b)\) be a Stirling number of the second kind (partitions of an \(a\)-element labeled set into \(b\) nonempty unlabeled classes). Put \(t=\min\{m-1,n-1\}\). The polynomial counting all inclusion-minimal connected dominating sets, by their cardinalities, is

\[
\begin{aligned}
C_{m,n}(z)={}&\sum_{r=1}^{t}\binom mr\,r!S(n-1,r)n^{r-1}z^{n+r-1}\\
&+\sum_{s=1}^{t}\binom ns\,s!S(m-1,s)m^{s-1}z^{m+s-1}.
\end{aligned}
\]

Every such set is uniquely one of two kinds: the edge set of a bipartite tree supported on all \(n\) column vertices and a proper nonempty subset of the \(m\) row vertices, with all selected rows of degree at least two; or its transpose, supported on all rows and a proper nonempty subset of the columns, with all selected columns of degree at least two. The two kinds are disjoint.

If \(2\le m\le n\), then the set of *attainable* inclusion-minimal cardinalities is exactly

\[
\{m,m+1,\ldots,2m-2\}\ \cup\ \{n,n+1,\ldots,n+m-2\}.
\]

Consequently the minimum connected-domination cardinality is \(m\), and the largest inclusion-minimal cardinality is \(n+m-2\). If \(n\ge 2m\), none of \(2m-1,2m,\ldots,n-1\) is attained: these are \(n-2m+1\) consecutive absent cardinalities, an unbounded gap when \(m\) is fixed and \(n\) grows.

## Assumptions and scope

All graphs are finite, simple, and undirected. Rows and columns are individually labeled; a selected cell \((i,j)\) is identified with the edge joining row-vertex \(i\) to column-vertex \(j\) in \(K_{m,n}\). The term *minimal* means inclusion-minimal, not minimum-cardinality. The graph is assumed to have both board dimensions at least two; the theorem makes no claim for one-row or one-column boards. Empty connected subgraphs are excluded.

## Proof

**1. Translating domination and connectivity.** For a nonempty selected cell set \(D\), write \(H_D\) for the bipartite graph formed by its selected edges and all their incident row/column vertices, with no isolated vertices. Two vertices of \(R_{m,n}[D]\) are adjacent exactly when their edges in \(H_D\) share an endpoint, so \(R_{m,n}[D]\) is connected if and only if \(H_D\) is connected. A cell is undominated exactly when its row and column both have degree zero in \(H_D\). Thus \(D\) is dominating precisely when at least one of the two complete shore sets is covered by \(H_D\): all rows or all columns have positive selected degree.

**2. A minimal set has a tree incidence graph.** Suppose \(D\) is inclusion-minimal connected dominating and \(H_D\) has a cycle. Delete any edge \(e\) on that cycle. The remaining nonisolated incidence graph is connected; in particular both ends of \(e\) still have selected degree at least one, so the row/column coverage sets do not change. Domination and connectivity therefore persist, contrary to minimality. Hence \(H_D\) is a tree. Because \(m,n\ge2\), a single cell cannot dominate the entire board; thus \(H_D\) has at least two edges.

**3. Exactly one shore is fully covered, and the other has no leaf.** Were both shores fully covered, deleting a leaf edge of the tree would preserve connectivity of the remaining selected edges and preserve complete coverage of the *opposite* shore, violating minimality. Thus exactly one shore is fully covered. Suppose all columns are covered but at least one row is not. If \(H_D\) had a row leaf, deletion of its incident edge would again leave the remaining graph connected and every column covered (the adjacent column has degree at least two, since \(H_D\) has at least two edges). That would violate minimality. Therefore every selected row has degree at least two. The transposed case is identical.

**4. Every listed tree is indeed minimal.** Take a connected bipartite tree meeting all columns and a proper nonempty set of rows, with each selected row degree at least two. Its cells dominate because all columns are represented, and induce a connected rook subgraph. For a selected tree edge \(e\), either \(e\) joins two vertices both of degree at least two, so its deletion splits the tree into two nontrivial edge-containing components and disconnects the remaining rook subgraph; or \(e\) is incident to a leaf column, so its deletion uncovers that column. An already omitted row and the newly uncovered column form an undominated cell. Hence deleting any single selected cell destroys connected domination. This proves inclusion-minimality even against arbitrary proper subsets: if a proper subset \(D'\subsetneq D\) were connected dominating, choose a spanning tree of \(R_{m,n}[D]\) extending a spanning tree of the connected \(R_{m,n}[D']\). A leaf outside \(D'\) may be removed while preserving connectivity, and the remaining set still dominates because it contains \(D'\); this would contradict the single-deletion test. The construction is unique from its selected edge set. The two orientations are disjoint because each omits vertices from a different shore.

**5. Counting the trees.** Fix \(r\) selected row labels and all \(n\) columns, with \(1\le r<m\). Every row is required to have degree at least two; this forces \(r\le n-1\), since a tree has \(n+r-1\) edges. For variables \(x_1,\ldots,x_r\), the standard weighted bipartite spanning-tree identity is

\[
\sum_{T\text{ spanning tree of }K_{r,n}}\prod_{i=1}^{r}x_i^{\deg_T(i)-1}
=n^{r-1}(x_1+\cdots+x_r)^{n-1}.
\]

For completeness, assign weight \(x_i\) to every edge from row \(i\), set \(X=\sum_i x_i\), and delete one column vertex from the weighted Laplacian. The resulting block matrix has upper-left block \(n\operatorname{diag}(x_1,\ldots,x_r)\), lower-right block \(XI_{n-1}\), and off-diagonal blocks \(-x\mathbf1^\mathsf T\), \(-\mathbf1x^\mathsf T\). Its determinant, by the Schur complement and rank-one determinant lemma, is \(n^{r-1}X^{n-1}\prod_i x_i\). The weighted matrix-tree theorem identifies that determinant with \(\sum_T\prod_i x_i^{\deg_T(i)}\), proving the displayed identity after division by \(\prod_i x_i\). The result extends from positive weights to formal variables as a polynomial identity.

Requiring all selected rows to have degree at least two means every \(x_i\) has positive exponent. In the multinomial expansion of \((x_1+\cdots+x_r)^{n-1}\), the sum of coefficients of monomials with every exponent positive is the number of surjections from an \((n-1)\)-element labeled set onto \(r\) labeled boxes, namely \(r!S(n-1,r)\). Thus there are \(n^{r-1}r!S(n-1,r)\) admissible trees on the specified row labels. Select those labels in \(\binom mr\) ways; the trees have \(n+r-1\) edges/cells. Summing over \(r\) gives the first term of \(C_{m,n}\). Interchanging shores gives the second term. Since the classes do not overlap, their counts add.

**6. Spectrum and gaps.** For \(2\le m\le n\), every coefficient associated with \(r\in\{1,\ldots,m-1\}\) is positive because \(S(n-1,r)>0\); this gives exactly the interval \(n,\ldots,n+m-2\). The transposed sum gives exactly \(m,\ldots,2m-2\), with no other sizes. The asserted extremal values and missing interval follow. The already known minimum \(m\) is included for context, not claimed as a new extremal result.

## Verification

The standalone source `verify.py`, using only Python's standard library, independently constructs each rook graph and tests selected subsets for connectivity, closed-neighborhood domination, and inclusion-minimality. It compares its exhaustive cardinality histogram with the Stirling formula for 12 labeled boards: \((2,2)\), \((2,3)\), \((2,4)\), \((2,5)\), \((2,6)\), \((2,7)\), \((3,3)\), \((3,4)\), \((3,5)\), \((3,6)\), \((4,4)\), and \((4,5)\). This entails \(1{,}435{,}460\) nonempty subsets and finds \(7{,}406\) minimal connected dominating sets. In particular, \(C_{3,5}(z)=5z^3+60z^4+3z^5+210z^6\), and \(C_{4,4}(z)=8z^4+288z^5+768z^6\). These finite tests support, but do not replace, the proof for arbitrary dimensions. Reproduce with `python3 verify.py`.

## Relationship to prior work

Abu-Khzam, Fernau, Gras, Liedloff, and Mann (arXiv:2205.00086v1, first public April 29, 2022; ESA 2022, DOI 10.4230/LIPIcs.ESA.2022.1) give general algorithms and bounds for enumerating minimal connected dominating sets, rather than an exact rook-graph cardinality polynomial. Kulli and Sigarkanti's established minimum connected edge domination number of \(K_{m,n}\), quoted as Theorem 2(ii) in Li, Liu, and Liu (2024), is \(\min\{m,n\}\); the present minimum statement is therefore not new. Li, Liu, and Liu study Nordhaus–Gaddum bounds and connected edge domination, not the all-minimal family here. OEIS A360875 and A289196 count **all** connected dominating sets of rectangular or square rook graphs, respectively; they do not classify the inclusion-minimal members or supply this polynomial. Other work on maximal induced forests, clusters, and bipartite subgraphs of rook graphs concerns different monotone set systems and does not imply the minimal connected domination classification.

## Limitations

The proof is for two complete-graph Cartesian factors with both sizes at least two; it does not enumerate all connected dominating sets, extend to rook boards with deleted cells, or determine the analogous invariants for higher-dimensional Hamming graphs. A historical 1988 report and the 2009 connected-edge-domination article were available only through bibliographic descriptions or secondary quotations, not complete readable texts; undiscovered equivalent enumerators remain a publication-priority risk. The result has received only self-review; no independent audit or external certification has been performed.

## References

1. F. Abu-Khzam, H. Fernau, B. Gras, M. Liedloff, K. Mann, *Enumerating Connected Dominating Sets*, arXiv:2205.00086v1, 2022-04-29; *Enumerating Minimal Connected Dominating Sets*, ESA 2022, DOI 10.4230/LIPIcs.ESA.2022.1. https://arxiv.org/html/2205.00086v1
2. H. Li, H. Liu, J. Liu, *Nordhaus–Gaddum-Type Results on the Connected Edge Domination Number*, *Bull. Malays. Math. Sci. Soc.* 47 (2024), 54, DOI 10.1007/s40840-023-01649-1; Theorem 2(ii) cites Kulli and Sigarkanti's complete-bipartite minimum. https://doi.org/10.1007/s40840-023-01649-1
3. V. R. Kulli, S. C. Sigarkanti, *The Connected Edge Domination Number of a Graph*, Technical Report 8801 (1988), cited in Reference 2. DOI 10.13140/RG.2.2.18634.36807.
4. S. Arumugam, S. Velammal, *Connected Edge Domination in Graphs*, *Bull. Allahabad Math. Soc.* 24 (2009), 43–49.
5. A. Howroyd, OEIS A360875, *Number of connected dominating sets in the rook graph \(K_m\square K_n\)*; E. W. Weisstein, A. Howroyd, OEIS A289196 (square diagonal). https://oeis.org/A360875 and https://oeis.org/A289196
