# Maximal induced forests of rook graphs: an exact component census

## Finding

For integers \(2\le m\le n\), let \(R_{m,n}=K_m\square K_n\) be the rook graph on an \(m\)-by-\(n\) board: two cells are adjacent exactly when they share a row or column. An **inclusion-maximal induced forest** is a vertex set whose induced subgraph is acyclic and which ceases to be acyclic on adding any omitted vertex. Write \(c(S)\) for the number of nonempty connected components induced by such a set and define the component-refined enumerator

\[
\mathcal F_{m,n}(z,u)=\sum_{S\text{ inclusion-maximal induced forest}}z^{|S|}u^{c(S)}.
\]

**Theorem.** For every pair of integers \(2\le m\le n\),

\[
\boxed{\mathcal F_{m,m}(z,u)=(m!)^2z^{2m-1}u},
\]

whereas for \(m<n\),

\[
\boxed{\mathcal F_{m,n}(z,u)=z^{2m}m!n!\sum_{s=1}^{\min\{m,n-m\}}\frac{\binom{m-1}{s-1}}{2^s s!(n-m-s)!}u^s.}
\]

Every displayed coefficient is positive. Thus every maximal induced forest has \(2m-1\) vertices when \(m=n\) and \(2m\) when \(m<n\). In particular, all these rook graphs are *well-f-covered*. They have only connected maximal induced forests exactly when \(n=m\) or \(n=m+1\). Complementation shows that every inclusion-minimal feedback vertex set is of minimum size, which is \((m-1)^2\) in the square case and \(m(n-2)\) in the rectangular case. The scalar minimum feedback vertex set number is known independently; the contribution here is the exact structural classification and component-refined counting.

For example, \(\mathcal F_{2,4}(z,u)=z^4(24u+6u^2)\), \(\mathcal F_{3,5}(z,u)=z^6(360u+180u^2)\), and \(\mathcal F_{4,4}(z,u)=576z^7u\). For each fixed positive difference \(d=n-m\), as \(m\to\infty\) the proportion of maximal induced forests with exactly \(d\) components tends to one, with error \(O(1/m)\); this is understood along \(m\ge d\).

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled by their given row and column coordinates. The theorem concerns \(m,n\) as above, not the case with a one-vertex factor. An induced forest is maximal under *vertex inclusion*, rather than having the most edges or components. The coefficient counts distinct subsets of the \(mn\) labeled rook-graph vertices. Isolated vertices of \(K_{m,n}\) must be distinguished from components of the selected rook graph: they contribute no rook vertices.

## Proof

**1. Line graph reduction.** Identify a rook vertex \((i,j)\) with the edge \(a_ib_j\) of \(K_{m,n}\). For any set \(S\) of selected cells, let \(H\) be the bipartite graph whose edge set consists of those cells, including all base vertices of \(K_{m,n}\). Then \(R_{m,n}[S]=L(H)\). If a base vertex has at least three selected incident edges, \(L(H)\) contains a triangle. If \(H\) contains a cycle, its line graph contains a cycle. Conversely, if every base degree is at most two and \(H\) is acyclic, its nontrivial components are paths, so \(L(H)\) is a disjoint union of paths. Thus \(R_{m,n}[S]\) is acyclic if and only if \(H\) is a linear forest (a path forest, plus possible isolated base vertices).

**2. Inclusion-maximal classification.** Let \(A\) and \(B\) denote the bipartition classes with \(|A|=m\) and \(|B|=n\). Define \(U_A\) and \(U_B\) as the vertices of the respective classes with selected degree less than two. Suppose both are nonempty. For every pair \(a\in U_A\), \(b\in U_B\), the edge \(ab\), if missing, can be added without raising a degree above two and without making a cycle *unless* \(a\) and \(b\) already belong to the same path component. By maximality they must belong to that same component; if the edge is already present, they also do. A nontrivial path has at most two vertices of degree less than two, its endpoints, and a base isolated vertex cannot lie in a component with an opposite-class vertex. Consequently \(U_A\) and \(U_B\) are singletons, forming the two endpoints of one path component. Any other path component would require further deficient endpoints, so no other component exists. The path spans \(A\cup B\), has endpoints on opposite sides, and hence \(m=n\). It contains \(2m-1\) edges. Conversely, each spanning alternating path in \(K_{m,m}\) is maximal as a linear forest: every missing edge either meets a degree-two vertex or closes its spanning path into a cycle.

If only \(U_B\) were empty, all \(n\) vertices of \(B\) would have degree two, giving \(2n\) selected edges in a forest on \(m+n\) base vertices, impossible because \(2n\ge m+n>m+n-1\). Hence, when \(m<n\), maximality forces \(U_A=\varnothing\): every vertex in \(A\) has degree two. Conversely, this condition makes every missing base edge incident with a degree-two \(A\)-vertex, so no cell can be adjoined without introducing a triangle in the rook graph. The selected base graph is therefore precisely a disjoint union of nontrivial alternating paths, each with both endpoints in \(B\), together with unused isolated \(B\)-vertices. All \(m\) vertices of \(A\) have degree two, so the rook forest has \(2m\) vertices. A component using \(k\ge1\) vertices of \(A\) uses exactly \(k+1\) of \(B\); for \(s\) nontrivial components, this requires \(1\le s\le\min\{m,n-m\}\), and each such \(s\) is feasible.

**3. Enumeration.** In the square case, specifying the ordered \(m\) vertices of each part and the starting side gives \(2(m!)^2\) alternating Hamilton-path orientations. Reversal identifies pairs, giving \((m!)^2\) undirected paths, each one rook forest with one component.

For the rectangular case, the number of undirected alternating paths on a prescribed labeled set of \(k\ge1\) vertices from \(A\) and \(k+1\) vertices from \(B\) is \(k!(k+1)!/2\). The two-sort exponential generating function for an unordered set of these path components, marked by \(u\), together with isolated \(B\)-vertices is therefore

\[
\boxed{\exp\!\left(y+\frac{u x y^2}{2(1-xy)}\right).}
\]

The desired number with \(s\) components is \(m!n![x^m y^n u^s]\) of this series. Indeed, extracting \(u^s\) gives

\[
\frac{e^y}{2^s s!}\frac{x^s y^{2s}}{(1-xy)^s},
\]

and the further \(x^m\) coefficient is \(\binom{m-1}{s-1}y^{m+s}\). The remaining \(y^n\) coefficient of \(e^y\) is \(1/(n-m-s)!\). Multiplying by \(m!n!\) proves the formula, including the exact range of nonzero coefficients.

**4. Consequences.** Maximal induced forests all have the same size by Step 2; the complements of these sets are exactly the inclusion-minimal feedback vertex sets. The connectedness claim is the positivity range for \(s\). Finally, holding \(d=n-m\ge1\) fixed and factoring out \(m!n!\), each coefficient for \(1\le s\le d\) is a polynomial in \(m\) of degree \(s-1\) times a positive \(d,s\)-dependent constant; the \(s=d\) coefficient dominates all others by a relative \(O(m^{-1})\) factor, proving the stated asymptotic.

## Verification

The standalone `VERIFY.py` checks acyclicity using union-find *on induced rook-graph edges*, verifies maximality by testing each possible vertex addition, independently counts components, and compares against the closed formulas. It exhaustively checks all nonempty subsets for the 11 boards with \(2\le m\le n\), \(m\le4\), and \(mn\le16\), checking 190,277 subsets and 2,740 maximal sets. A distinct recurrence based on the alternating path containing a fixed \(A\)-vertex agrees with the formulas on 1,375 parameter triples in the stated finite ranges. These tests are finite corroboration only; the unrestricted results follow from the proof above.

## Relationship to prior work

Jafarpour-Golzari (2021) introduced well-f-covered graphs and studied several graph operations; a clique-plus-matching construction in Theorem 6.7 covers the two-row rook graph at the level of uniform forest size, but not the present component-resolved census and not the general higher-row case. His second paper treats *lexicographic* products, unlike the Cartesian products here. Stones (2014) enumerated all spanning forests of \(K_{m,n}\) by edge count, explicitly discussing its rook-graph line-graph interpretation, but her statistic admits arbitrary degrees and cycles of length three in the rook graph; it does not select inclusion-maximal *acyclic induced rook subgraphs*, nor determine their component counts. Dong and Ge (2021) count spanning trees containing a fixed forest, a different extension problem. The ordinary induced-forest polynomial concerns all acyclic induced subsets, not just inclusion-maximal ones. The scalar feedback vertex set number of rook graphs and the square-board alternating Hamilton-path count \((m!)^2\) are already recorded in standard tables and are not asserted to be new. The candidate contribution is the all-parameter if-and-only-if classification and labeled component distribution.

## Limitations

No claim is made for \(m=1\), for general products or arbitrary bipartite line graphs, or about independent mathematical validation. The closed formula refines existing scalar and unrestricted spanning-forest information. A literature search cannot establish absolute priority; an equivalent enumeration under another name may exist. Finite computation is only corroborative. Counts are labeled, not graph-isomorphism classes.

## References

1. R. Jafarpour-Golzari, *Graphs whose all maximal induced forests are of the same order*, arXiv:2105.14339v1, posted May 29, 2021. https://arxiv.org/abs/2105.14339
2. R. Jafarpour-Golzari, *On well-f-coveredness of lexicographic products of graphs*, arXiv:2108.09146v1, posted August 20, 2021. https://arxiv.org/abs/2108.09146
3. R. J. Stones, *Computing the number of h-edge spanning forests in complete bipartite graphs*, Discrete Mathematics & Theoretical Computer Science 16:1 (2014), 313–326, DOI: 10.46298/dmtcs.1248. https://dmtcs.episciences.org/articles/1248
4. F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294v1 (2021). https://arxiv.org/abs/2103.05294
5. J. A. Makowsky and V. Rakita, *Almost Unimodal and Real-Rooted Graph Polynomials*, arXiv:2102.00268v1 (2021). https://arxiv.org/abs/2102.00268
6. E. W. Weisstein, *Feedback Vertex Set Number*, MathWorld. https://mathworld.wolfram.com/FeedbackVertexSetNumber.html
7. OEIS A001044, squares of factorials; also cited for alternating Hamilton paths in \(K_{m,m}\). https://oeis.org/A001044
