# Maximal dissociation sets of rook graphs: an exact two-star-packing polynomial

## Finding
For integers \(m,n\ge1\), let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\) be the rook graph with \(mn\) labelled vertices, one for each cell of an \(m\)-by-\(n\) board. A *dissociation set* is a vertex set inducing maximum degree at most one; *maximal* always means inclusion-maximal. Write \(M_{m,n}(t)\) for the polynomial enumerating maximal dissociation sets by number of selected vertices.

For nonnegative integers \(a,b,c\), set
\[
r=a+b+2c,\qquad s=a+2b+c,\qquad k=a+2b+2c.
\]
The complete polynomial is
\[
\boxed{M_{m,n}(t)=\sum_{\substack{a,b,c\ge0,\ r\le m,\ s\le n\\ (r=m\ \wedge\ s=n)\ \vee\ (a=0\ \wedge\ (r=m\ \vee\ s=n))}}
\frac{m!n!\,t^k}{a!b!c!\,2^{b+c}(m-r)!(n-s)!}.}
\]
A parameter triple is counted **once** when it satisfies the displayed logical condition, even if both clauses apply. Here \(a\) counts isolated selected vertices in the rook graph, \(b\) counts selected adjacent pairs within rows, and \(c\) counts selected adjacent pairs within columns.

In the rectangular regime \(1\le m\le n\) and \(n\ge2m\), this simplifies to
\[
\boxed{M_{m,n}(t)=\sum_{c=0}^{\lfloor m/2\rfloor}
\frac{m!n!}{(m-2c)!\,c!\,2^{m-c}(n-2m+3c)!}\,t^{2m-2c}.}
\]
Thus the possible sizes are exactly \(2\lceil m/2\rceil,2\lceil m/2\rceil+2,\ldots,2m\); all intervening odd cardinalities are absent. In this regime the minimum size of a maximal dissociation set is \(2\lceil m/2\rceil\) and the maximum is \(2m\). The difference \(2\lfloor m/2\rfloor\) is unbounded.

## Assumptions and scope
All graphs are finite, simple, undirected and labelled. The theorem includes the boundary graphs \(R_{1,n}=K_n\) and \(R_{1,1}=K_1\). The cardinality polynomial counts distinct labelled vertex subsets rather than automorphism classes. No assertion is made about a general arbitrary graph or about maximal versus maximum configurations being interchangeable.

## Proof
**1. Component classification.** Identify a selected rook-graph vertex \((i,j)\) with the edge joining row vertex \(i\) to column vertex \(j\) in \(K_{m,n}\). Two selected cells are adjacent precisely when their corresponding edges share an endpoint. Consequently every selected cell has at most one selected neighbour exactly when each component of the selected-edge graph is a single edge \(K_{1,1}\), a two-edge star \(K_{1,2}\), or a two-edge star \(K_{2,1}\), with different components using disjoint row and column vertices. If a selected-edge component contained at least three edges, its line graph would be connected on at least three vertices and hence would contain a vertex of degree at least two, contradicting the dissociation condition. Conversely a vertex-disjoint union of these components gives an induced rook-graph subgraph of maximum degree one.

Let \(a,b,c\) count the three types in the order above. Exactly \(r=a+b+2c\) row vertices and \(s=a+2b+c\) column vertices are used. The selected rook-graph set has size \(k=a+2b+2c\).

**2. Maximality.** If a row and a column are both unused, their intersection cell has no selected neighbour and can be added. Hence maximality requires every row or every column to be used. If all rows and all columns are used, every missing cell meets a selected cell in its row and a *different* selected cell in its column, so the missing cell would have at least two selected neighbours and cannot be added. Such a configuration is maximal.

Suppose all rows are used and some column \(j\) is unused. If the selected configuration contains an isolated component \((i,j')\), adding \((i,j)\) creates exactly one adjacency and keeps all induced degrees at most one. Therefore a maximal configuration in this case has \(a=0\). Conversely, if \(a=0\), every selected cell already has one selected neighbour within its two-edge-star component. Every missing cell whose row and column are both used meets at least two distinct selected cells; every other missing cell meets an already paired selected cell, which would acquire degree two. Thus no missing cell can be added. Interchanging rows and columns proves the same result when all columns but not all rows are used. The exact maximality criterion is therefore
\[
(r=m\ \wedge\ s=n)\ \vee\ (a=0\ \wedge\ (r=m\ \vee\ s=n)).
\]
Because dissociation is hereditary under deleting selected vertices, a set is inclusion-maximal exactly when no single new vertex can be added.

**3. Enumeration.** To arrange \(a\) single-edge components, \(b\) row-centred two-edge stars and \(c\) column-centred two-edge stars, choose disjoint row slots of sizes one, one and two, and disjoint column slots of sizes one, two and one, then pair the corresponding slots within each component type. Dividing by permutations of indistinguishable components and by the exchanges of the two leaves of each star yields exactly
\[
\frac{m!n!}{a!b!c!\,2^{b+c}(m-r)!(n-s)!}
\]
labelled selected-edge configurations. The component decomposition is unique, so configurations are not counted twice. Summing these contributions under the criterion from Step 2 proves the first formula.

**4. Rectangular simplification.** Assume \(m\le n\) and \(n\ge2m\). A maximal configuration with all columns but not all rows used and \(a=0\) is impossible: it would have \(n=2b+c\le2(b+2c)\le2(m-1)<2m\). A configuration using both sides entirely obeys \(n=2m-a-3c\), so \(n=2m\) forces \(a=c=0\) and \(n>2m\) excludes this case. Thus every maximal configuration has \(a=0\) and all \(m\) rows used. Writing \(b=m-2c\), all \(0\le c\le\lfloor m/2\rfloor\) are feasible because the number of used columns is \(2m-3c\le n\). Substitution into the general enumerator proves the second formula, whose coefficients are strictly positive. Its exponents and endpoints give the stated spectrum and unbounded gap.

## Verification
The included standalone file `verify_rook.py` uses only Python's standard library. Run `python verify_rook.py` in the directory containing that file. For each indicated pair of dimensions, it explicitly constructs rook-graph neighbourhood bitmasks, independently tests every vertex subset for induced degree at most one, tests every one-vertex addition for maximality, and compares all size coefficients with the factorial formula. The tested cases have \(1\le m\le4\), \(m\le n\le6\), and \(mn\le20\); this covers 17 labelled graph instances and 1,419,214 vertex subsets.

The observed result is `VERIFY_OK instances=17 vertex_subsets=1419214 dissociation_sets=9778 maximal_sets=1467 all_coefficients=PASS single_vertex_extensions=PASS`. Example enumerators include \(M_{2,2}(t)=6t^2\), \(M_{3,3}(t)=6t^3+9t^4\), \(M_{3,5}(t)=90t^4+90t^5\), and \(M_{4,4}(t)=96t^4+144t^5\). The finite tests are supporting evidence, not a proof for unbounded dimensions; that proof is the component/maximality argument above.

## Relationship to prior work
Tu, Li and Du (2021 preprint; 2022 journal publication) study general upper bounds and extremal graphs for the *number* of maximal dissociation sets, rather than the full size distribution of one arbitrary rook graph. Orlovich, Dolgui, Finke, Gordon and Werner (2011) prove complexity results and, for line graphs of graphs admitting a Hamiltonian path, determine the maximum dissociation size. In particular, that earlier result applies to balanced complete bipartite input graphs and is not claimed as new here. It does not count all maximal dissociation sets of each size.

Tian and Tu (2024) enumerate maximal dissociation sets in ordinary, cyclical and cylindrical grid graphs. These are not the complete-factor Cartesian products \(K_m\square K_n\); however, only their accessible abstract and bibliographic description were inspected, so an unexamined cross-reference remains a publication-priority risk. Results on general-position and induced-forest subsets of rook graphs have different admissibility predicates: selecting three cells in one row is general-position but is not a dissociation set. Their cardinality counts do not determine the maximal-dissociation polynomial.

## Limitations
The result is an exact mathematical derivation for complete-factor rook graphs, not a complexity theorem for arbitrary line graphs. Finite exhaustive checks do not prove the unrestricted statement independently. The literature comparison is substantial but cannot exclude uncatalogued equivalent results or content in inaccessible primary works. No independent mathematical audit has been performed.

## References
1. J. Tu, Y. Li, J. Du, *Maximal and Maximum Dissociation Sets in General and Triangle-Free Graphs*, arXiv:2103.01402v1, first public version 2021-03-02. https://arxiv.org/abs/2103.01402 ; journal DOI 10.1016/j.amc.2022.127107.
2. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon, F. Werner, *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics 159 (2011), 1352–1366, DOI 10.1016/j.dam.2011.04.023.
3. Y. Tian, J. Tu, *Enumerating maximal dissociation sets in three classes of grid graphs*, Applied Mathematics and Computation 474 (2024), article 128711, DOI 10.1016/j.amc.2024.128711.
