# Exact visibility and facet polynomials for three-row rook graphs

## Finding

**Theorem.** For every integer \(n\ge2\), write \(R_n=K_3\square K_n\), with vertices labelled by \([3]\times[n]\). If \(V_n(z)=\sum_{S}z^{|S|}\) ranges over all ordinary mutual-visibility sets \(S\subseteq V(R_n)\), then
\[
V_n(z)=\sum_{j=0}^{\min(3,n)}\binom{3}{j}(n)_{\underline j}\,z^{2j}(1+3z)^{n-j}+nz^3(1+3z)^{n-1}.
\]
Here \((n)_{\underline j}=n(n-1)\cdots(n-j+1)\), with \((n)_{\underline0}=1\).

If \(F_n(z)=\sum_{S\text{ inclusion-maximal}}z^{|S|}\) ranges over inclusion-maximal ordinary mutual-visibility sets, then
\[
F_n(z)=\bigl(n3^{n-1}+3n(n-1)\bigr)z^{n+2}+\mathbf 1_{n\ge3}\,n(n-1)(n-2)3^{n-3}z^{n+3}.
\]
Each inclusion-maximal set belongs to exactly one of the three support types defined below. For \(n\ge3\) the two possible facet cardinalities are distinct, so the simplicial complex of mutual-visibility sets is not pure.

## Assumptions and scope

The graph is finite, simple, undirected, and has the usual Cartesian-product adjacency: distinct \((r,c)\) and \((s,d)\) are adjacent iff \(r=s\) or \(c=d\). All rows and columns are labelled. A set \(S\) is an *ordinary mutual-visibility set* when, for each pair \(u,v\in S\), there exists a shortest \(u,v\)-path whose internal vertices lie outside \(S\); this is not total mutual visibility, which quantifies over every pair of graph vertices. Maximal means inclusion-maximal, not merely maximum cardinality. Empty and singleton sets are included in \(V_n\), but none is maximal when \(n\ge2\).

For each column \(c\), define its support \(A_c=\{r\in[3]:(r,c)\in S\}\). We call a support of size one a *singleton*, size two a *pair*, and size three a *triple*.

## Proof

**Step 1 (the exact forbidden pattern).** Any two vertices differing in both coordinates have distance two, with exactly two common neighbors, the other corners of their \(2\)-by-\(2\) submatrix. Such a selected pair has an unobstructed geodesic if and only if at least one of those two corners is not in \(S\). Adjacent selected vertices impose no restriction. Consequently
\[
S\text{ is ordinary mutual-visible}\iff |A_c\cap A_d|\le1\quad\text{for every distinct }c,d.
\]
This is precisely the absence of a selected four-cycle in the bipartite row-column incidence graph. In particular, a triple support excludes every pair support in other columns, and, when there is no triple, each of the three possible pair supports occurs at most once.

**Step 2 (all sets).** First count configurations without triple supports. Choose \(j\in\{0,\ldots,\min(3,n)\}\) distinct row-pair supports from the three possible ones, assign these distinct supports injectively to \(j\) labelled columns, and put any of the four possibilities (empty or one of three singleton rows) in each of the other \(n-j\) columns. Their contribution is \(\binom3j(n)_{\underline j}z^{2j}(1+3z)^{n-j}\). Next count configurations with a triple: choose its column in \(n\) ways, and each other column is empty or a singleton, contributing \(nz^3(1+3z)^{n-1}\). These disjoint cases exhaust the allowed supports and prove \(V_n(z)\).

**Step 3 (maximality: preliminary restrictions).** A maximal configuration has no empty column: one singleton can always be inserted in an empty column without creating two equal row-pair supports. A triple configuration cannot contain another pair/triple, so it is maximal exactly when its other columns are all singletons: inserting another vertex there creates a pair also contained in the triple column. This is type A. If no triple is present, configurations with at most one pair support are not maximal: for zero pairs one may create a pair, and for one pair one may enlarge its column to a triple; these changes preserve all pairwise support intersections.

**Step 4 (two or three pairs).** Suppose there are exactly two pair supports. They must be distinct and intersect in a unique row \(r\). A remaining singleton in row \(r\) cannot be enlarged: either second selected row reproduces one of the existing pair supports. A singleton in either other row *can* be enlarged to the unused third pair support, so maximality forces all remaining singletons to use row \(r\). The resulting configurations are maximal since each unselected cell would duplicate an existing pair support. This is type B. With all three distinct pair supports already present, every other column must be singleton and cannot be enlarged without duplicating one of the three pairs; these are exactly the maximal type C configurations. No fourth pair can occur. All asserted cases are mutually exclusive.

**Step 5 (facet count).** Type A: \(n\) choices for the triple column, \(3^{n-1}\) singleton assignments, and \(3+n-1=n+2\) selected vertices. Type B: choose the omitted support (three choices), order the two remaining distinct supports on two distinct columns (\(n(n-1)\) choices), and force all other singletons to their common row; cardinality \(2+2+(n-2)=n+2\). Type C exists exactly for \(n\ge3\): injectively place all three distinct pair supports in \((n)_{\underline3}\) ways, then choose one of three rows for each remaining singleton. Its cardinality is \(6+(n-3)=n+3\). Summation proves \(F_n(z)\) and the claimed facet-size spectrum. This concludes the proof for all integers \(n\ge2\), including the two-column boundary.

## Verification

The included standalone `verify.py` constructs the graph from its literal Cartesian adjacency, tests all selected nonadjacent pairs for an avoiding common neighbor, and independently tests maximality by adding each unselected vertex. Every subset was checked for each \(n=2,3,4,5,6\) (a total of \(299584\) subsets). Every coefficient of \(V_n\) and \(F_n\), and every maximal support type, agreed with the formulas. Integer-arithmetic checks cover a further \(89\) parameter values through \(n=90\). Run `python3 verify.py` with a standard Python 3 interpreter. These finite computations support but do not replace the proof for arbitrary \(n\).

For \(n=3\), the literal enumeration finds \(334\) mutual-visibility sets and \(45\) facets of size \(5\) together with \(6\) facets of size \(6\).

## Relationship to prior work

Cicerone, Di Stefano and Klavžar established the general equivalence between mutual visibility in Cartesian products of complete graphs and the \(C_4\)-free bipartite incidence condition [1]. Brešar and Yero established the general *lower* mutual-visibility number \(m+n-1\) for \(K_m\square K_n\) [2, Corollary 7], via the Bollobás–Wessel bound. Those structural and scalar results are prior work, not new claims. The new result here is the exact complete polynomial and the labelled classification and multiplicities of **every** inclusion-maximal set in the three-row family, including its facet-size distribution.

Bryant and Fu investigated the possible edge cardinalities of \(C_4\)-saturated bipartite graphs in 2002 [3]. Its accessible abstract does not state labelled counts or a full polynomial; its full text was not available for comparison, so it is a material outstanding priority risk. Later visibility-polynomial studies [4,5] develop general definitions and other graph families, without a directly matching three-row rook formula in the inspected accessible portions.

## Limitations

The formula concerns ordinary mutual visibility in exactly three rows with arbitrary \(n\ge2\), not arbitrary row counts, and not total mutual visibility. It enumerates labelled subsets rather than isomorphism classes under coordinate permutations. The complete classification and formulas are mathematical claims supported by a self-contained proof and finite cross-checks; they have not undergone independent mathematical audit. Possible equivalent results in unindexed literature or in the inaccessible complete Bryant–Fu article remain unexcluded; no publication-priority certification is asserted.

## References

1. S. Cicerone, G. Di Stefano, S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, arXiv:2112.13024, https://arxiv.org/abs/2112.13024.
2. B. Brešar, I. G. Yero, *Lower (total) mutual-visibility number in graphs*, arXiv:2307.02951, https://arxiv.org/abs/2307.02951, Section 2.3 / Corollary 7.
3. D. E. Bryant, H.-L. Fu, *C4-saturated bipartite graphs*, Discrete Mathematics 259 (2002), 263–268, https://doi.org/10.1016/S0012-365X(02)00371-0.
4. C. Bujtás et al., *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066, https://arxiv.org/abs/2412.03066.
5. K. B. Tonny, M. Shikhi, *On the Visibility Polynomial of Graphs*, arXiv:2507.01851, https://arxiv.org/abs/2507.01851.
