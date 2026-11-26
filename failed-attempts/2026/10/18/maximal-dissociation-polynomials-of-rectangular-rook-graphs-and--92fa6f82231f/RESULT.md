# Maximal dissociation polynomials of rectangular rook graphs and parity gaps

## Finding

A **dissociation set** of a finite simple graph is a vertex subset inducing maximum degree at most one. It is **inclusion-maximal** if no additional vertex can be adjoined without violating this condition. Write \(R_{m,n}=K_m\square K_n\), with the vertices interpreted as cells in an \(m\)-by-\(n\) board: cells are adjacent precisely when they share a row or a column. For integers \(m,n\ge 1\), let
\[
M_{m,n}(z)=\sum_{\substack{S\subseteq V(R_{m,n})\\ S\text{ inclusion-maximal dissociation}}}z^{|S|}.
\]

**Theorem 1 (complete maximal-set enumerator).** Put
\[
 A=xyz,\qquad T=\tfrac12z^2(xy^2+x^2y).
\]
With the harmless boundary convention \(M_{0,n}(z)=M_{m,0}(z)=1\) (the empty graph has one maximal dissociation set), the complete bivariate exponential generating function is
\[
\boxed{\displaystyle
\sum_{m,n\ge0}M_{m,n}(z)\frac{x^m}{m!}\frac{y^n}{n!}
=e^{y+T}+e^{x+T}-2e^T+e^{A+T}.}
\]
The formula counts *labelled vertex subsets*, not orbits under graph automorphisms. Equivalently, it gives the explicit finite sum
\[
\boxed{\displaystyle
M_{m,n}(z)=\sum_{(a,b,c)\in\mathcal F_{m,n}}
\frac{m!\,n!\,z^{a+2b+2c}}{2^{b+c}a!b!c!r!s!},\quad
r=m-a-b-2c,\quad s=n-a-2b-c,}
\]
where \(\mathcal F_{m,n}\) consists exactly of the nonnegative integer triples \((a,b,c)\) for which \(r,s\ge0\) and either \(a=0\) with \(r=0\) or \(s=0\), or \(a\ge1\) with \(r=s=0\). Here \(a\) counts isolated selected edges and \(b,c\) count respectively row-centred and column-centred two-edge stars in the bipartite representation. The indexing condition lists each labelled configuration once.

**Theorem 2 (wide-board parity gaps and exact coefficients).** For \(1\le m\le n\) with \(n\ge2m\),
\[
\boxed{\displaystyle
M_{m,n}(z)=\sum_{c=0}^{\lfloor m/2\rfloor}
\frac{m!\,n!}{2^{m-c}(m-2c)!\,c!\,(n-2m+3c)!}\,z^{2m-2c}.}
\]
In particular, the possible cardinalities of inclusion-maximal dissociation sets are **exactly**
\[
 2\lceil m/2\rceil,\quad 2\lceil m/2\rceil+2,\quad\ldots,\quad 2m.
\]
Thus every intervening odd cardinality is impossible. For example, on a \(2\)-by-\(n\) board with \(n\ge4\),
\[
 M_{2,n}(z)=n z^2+6\binom{n}{4}z^4;
\]
no inclusion-maximal dissociation set has cardinality three. The extremal minimum and maximum cardinalities in this wide-board regime are \(2\lceil m/2\rceil\) and \(2m\), respectively.

## Assumptions and scope

All graphs are finite, simple, and undirected. Rows and columns are individually labelled. A maximum dissociation set (largest cardinality) is **not** the same as an inclusion-maximal dissociation set; the latter may have varying size. Theorems 1 and 2 concern all inclusion-maximal sets and their cardinality counts, rather than only the largest ones. The term \(R_{m,n}\) is the *rook graph* (a Cartesian product of two complete graphs), not the usual grid graph \(P_m\square P_n\).

## Proof

**Step 1: edge-model decomposition.** Identify each rook cell \((i,j)\) with the edge from row vertex \(i\) to column vertex \(j\) of \(K_{m,n}\). This identifies the rook graph with \(L(K_{m,n})\). For a selected edge set \(F\), the selected rook vertex corresponding to edge \(ij\) has selected-rook degree
\[
 (d_F(i)-1)+(d_F(j)-1)=d_F(i)+d_F(j)-2.
\]
Consequently, requiring this degree to be at most one for every selected edge forces every nontrivial connected component of \(([m]\sqcup[n],F)\) to be either a single edge \(K_2\), or a two-edge star \(K_{1,2}\). Indeed, no endpoint of a selected edge may have selected degree three; if an endpoint has selected degree two, both opposite endpoints must have degree one. Distinct components have disjoint endpoints. Conversely, every disjoint union of isolated selected edges and two-edge stars gives a dissociation set. Let \(a\) count isolated selected edges, \(b\) the stars centered in a row, and \(c\) the stars centered in a column.

**Step 2: the inclusion-maximality criterion.** Call a row/column *unused* when none of its incident edges is selected. If \(a\ge1\) and an unused row exists, connect it to the column endpoint of an isolated selected edge; adjoining that new edge converts a singleton selected component into a two-edge star and retains dissociation. The same reasoning uses an unused column and the row endpoint of an isolated selected edge. Therefore maximality with an isolated selected edge requires **no unused rows and no unused columns**.

Conversely, under these conditions, every unselected edge has both endpoints incident to selected edges. If those selected edges are distinct, adding the new edge makes its rook vertex adjacent to at least two selected rook vertices. If they are the same selected edge, that edge is already selected. Thus no extension is possible.

Suppose now \(a=0\), so every selected component is a two-edge star. If at least one row and one column are unused, the edge between them can be added as a new isolated selected component: the original dissociation set was not maximal. Conversely, if every row is used or every column is used, any unselected edge meets a used endpoint of a two-edge star. That endpoint either has two selected incident edges, giving the new rook vertex two selected neighbours, or has one selected incident edge whose rook vertex already has one selected neighbour within its existing star. In either case adjoining the new edge violates induced maximum degree one. Therefore a star-only configuration is maximal **if and only if all rows are used or all columns are used**.

This proves a disjoint, necessary-and-sufficient classification:

1. No isolated selected edges, with row and column resources occupied by two-edge stars and at least one side fully occupied.
2. At least one isolated selected edge, with both sides fully occupied by disjoint singleton edges and two-edge stars.

For a board with zero rows or columns the unique empty set is inclusion-maximal, giving the stated boundary convention.

**Step 3: labelled generating function.** An unused row contributes \(x\); an unused column contributes \(y\). An isolated selected edge uses one row and one column and contributes \(xyz=A\). A row-centred two-edge star uses one row and an unordered pair of columns and contributes \(xy^2z^2/2\); a column-centred star contributes \(x^2yz^2/2\). Labelled exponential assembly of vertex-disjoint components therefore yields \(e^{x+y+A+T}\) for all dissociation sets; the exponential formula is justified because each selected component has its own disjoint row/column labels.

For maximal star-only sets, every row occupied contributes \(e^{y+T}\), every column occupied contributes \(e^{x+T}\), and their intersection is counted twice and must be subtracted once as \(e^T\). For sets having at least one isolated edge with both sides fully used, the contribution is \(e^{A+T}-e^T\). Adding these two disjoint cases proves Theorem 1, including the zero-size boundary.

**Step 4: wide-board rigidity.** Suppose \(1\le m\le n\) and \(n\ge2m\). In every dissociation set each row contains at most two cells, hence at most \(2m\) columns can be occupied. If \(n>2m\), no configuration can occupy all columns. Moreover, a maximal configuration containing an isolated selected edge would need all columns occupied, which is impossible. Thus every maximal configuration is star-only and occupies every row.

The same conclusion holds when \(n=2m\): occupying all \(n\) columns requires \(2m\) selected cells, exactly two in each row, each in a distinct column. Such a configuration contains no isolated selected edge and occupies every row. Hence for all \(n\ge2m\), maximality is equivalent to packing two-edge stars so that **every row is used**. In the notation above, \(a=0\) and \(b+2c=m\), so \(b=m-2c\) with \(0\le c\le\lfloor m/2\rfloor\). The number of occupied columns is \(2b+c=2m-3c\), leaving \(n-2m+3c\) unused. For fixed \(c\), the exponential component formula gives exactly
\[
 \frac{m!\,n!}{2^{b+c}b!c!(n-2b-c)!}
 =\frac{m!\,n!}{2^{m-c}(m-2c)!c!(n-2m+3c)!}
\]
labelled sets. Their selected-cell cardinality is \(2(b+c)=2m-2c\). Every \(c\) in the indicated range is feasible (all factorial arguments are nonnegative), so no listed coefficient vanishes. This proves the closed formula and exactly characterizes the cardinality support, establishing Theorem 2.

## Verification

A reproducible standard-library Python checker accompanies this document as `verify_maximal_dissociation.py`, with captured output in `verification_output.txt`. For each board with \(1\le m\le n\le8\), \(m\le5\), and \(mn\le20\), it checks every vertex subset against (i) the original induced-degree condition and (ii) the requirement that adjoining *any* unselected cell fails the induced-degree condition. It compares the resulting coefficient polynomial with the independent star/singleton factorial enumeration. In total **1,501,518 labelled subsets across 21 boards** are examined. Additionally, 325 parameter pairs with \(1\le m\le n\le25\) are checked against independent component counting and boundary cases. All programmed checks passed.

The infinite-family theorems rest on the complete maximality classification, exponential counting, and arithmetic argument above; finite computation is corroboration only. No claim of machine formalization or independent mathematical certification is made.

## Relationship to prior work

Dissociation sets and their extremal cardinalities are established graph-theoretic invariants. Orlovich, Dolgui, Finke, Gordon and Werner (2011) explicitly relate dissociation sets of line graphs to disjoint three-vertex paths and isolated edges and study complexity and both maximum-cardinality and minimum-maximal optimization. They do not enumerate all inclusion-maximal rook-graph sets. **That general line-graph correspondence is prior work and is not claimed as new.** The advance here is the complete *inclusion-maximal* size distribution for all rectangular rook graphs, through a necessary-and-sufficient side-occupation criterion; general maximum-cardinality bounds do not yield this distribution.

Wang, Xu and Zhang's public August 2026 preprint studies **maximal** dissociation sets of trees, focusing on extremal numbers of maximal sets, rather than rook graphs. Zhou, Chen, Deng and Tu (2024) enumerate dissociation sets in \(P_m\square P_n\) grid graphs; these are not rook graphs \(K_m\square K_n\). Mertens (2024) counts ordinary *dominating* sets in rook graphs, not maximal dissociation sets.

A published rook-graph general-position polynomial also counts edge-subgraph star forests, allowing stars of arbitrary order, but **without the inclusion-maximality requirement** for induced-degree-one subsets. Neither its unrestricted forest count nor its maximum general-position size asserts this maximal-dissociation polynomial or the wide-board odd-cardinality gaps. Results on complete multipartite graphs and generalized windmills concern different graph families. This relationship is about distinct claims, not a claim of absolute publication priority.

## Limitations

The result concerns simple rectangular rook graphs only; it does not classify maximal dissociation sets in arbitrary line graphs, noncomplete bipartite line graphs, or higher-dimensional Hamming graphs. The verified experiments are finite and do not prove the unrestricted identity. Although targeted literature and mathematical-record comparisons did not identify the same enumerator, an unnoticed earlier formulation under the terminology “maximal induced subgraphs of degree at most one,” “maximal 2-component independent sets,” or “maximal path/star packings” remains possible. Definitive bibliographic priority and external mathematical auditing are open.

## References

1. M. Wang, M. Xu and N. Zhang, *The maximum number of maximal dissociation sets in trees*, arXiv:2608.16639, first posted 2026-08-17, https://arxiv.org/abs/2608.16639.
2. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon and F. Werner, *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics 159 (2011), 1352–1366, DOI:10.1016/j.dam.2011.04.023.
3. Zhou, Chen, Deng and Tu, *Enumeration of dissociation sets in grid graphs*, AIMS Mathematics 9 (2024), 14899–14912, DOI:10.3934/math.2024721.
4. S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716, 2024, https://arxiv.org/abs/2401.00716.
