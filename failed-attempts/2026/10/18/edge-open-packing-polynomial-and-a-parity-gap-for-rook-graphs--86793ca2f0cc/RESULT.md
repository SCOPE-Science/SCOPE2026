# Edge-open-packing polynomial and a parity gap for rook graphs

## Finding

For integers \(m,n\ge1\), let \(R_{m,n}=K_m\square K_n\), the graph on the cells of an \(m\)-by-\(n\) board, adjacent when they share a row or column. An **edge-open packing** is a set \(D\subseteq E(R_{m,n})\) such that no pair of distinct chosen edges has a third edge joining an endpoint of the first to an endpoint of the second. Define its size polynomial by
\[
P_{m,n}(z)=\sum_{\substack{D\subseteq E(R_{m,n})\\D\text{ is an edge-open packing}}}z^{|D|}.
\]
Then all coefficients, for every pair of board dimensions, are determined by
\[
\boxed{\sum_{m,n\ge0}P_{m,n}(z)\frac{x^m y^n}{m!n!}
=\exp\!\left(x+y+\frac{zxy^2}{2}+\frac{zx^2y}{2}+z^2x^2y^2\right).}
\]
Here \(P_{0,n}(z)=P_{m,0}(z)=1\) is the harmless formal convention for empty boards. Equivalently, for positive dimensions,
\[
\boxed{P_{m,n}(z)=m!n!\!\!\sum_{\substack{a,b,c\ge0\\a+2b+2c\le m\\2a+b+2c\le n}}
\frac{z^{a+b+2c}}{2^{a+b}a!b!c!(m-a-2b-2c)!(n-2a-b-2c)!}.}
\]
In particular, the exact edge-open-packing number is
\[
\boxed{\rho_e^o(R_{m,n})=\begin{cases}
\min(m,n)-1,&m=n\text{ is odd},\\
\min(m,n),&\text{otherwise}.
\end{cases}}
\]
For square boards of side \(q\), the number of maximum edge-open packings is
\[
\boxed{\begin{cases}
(q!)^2/(q/2)!,&q\ge2\text{ even},\\
1,&q=1,\\
(q!)^2\left(1/t!+1/(4(t-1)!)\right),&q=2t+1\ge3.
\end{cases}}
\]

## Assumptions and scope

All graphs are finite, simple, and undirected. Rows and columns are individually labelled; all chosen edge subsets, not just isomorphism types, are counted. The graph has vertex set \(\{(i,j):1\le i\le m,\ 1\le j\le n\}\), with the usual Cartesian-product adjacency. The two singleton cases of the definition coincide: a packing can be empty, and the single-vertex board has no graph edges. The theorem concerns edge-open packing, not ordinary vertex open packing or induced matching.

## Proof

**1. General induced-star condition.** For any graph \(G\) and nonempty edge subset \(D\), set \(V(D)\) to be the union of its edge endpoints. The defining condition is equivalent to \(G[V(D)]\) being a disjoint union of induced stars, with *all* star edges selected. Indeed, an additional edge between selected endpoints would be a forbidden third edge between two distinct selected edges. If a connected selected component contained adjacent vertices both of degree at least two, the joining edge would be a forbidden third edge for two other selected edges (a triangle is handled the same way). Thus each connected component is a star. Conversely, different induced-star components have no joining edge, and two star edges have no third edge joining their endpoints. This standard characterization is also explicitly recorded in the cited literature; the argument here fixes the exact convention used.

**2. Exactly three component types.** A row and a column each induce a clique in \(R_{m,n}\). For a star centered at a cell, at most one leaf can lie in its row and at most one in its column; two leaves in one row or column would be adjacent. Thus every nontrivial selected star is either a horizontal single edge, a vertical single edge, or a two-edge right-angle star (an L corner). A horizontal edge occupies one row and two columns; a vertical edge occupies two rows and one column; an L corner occupies two rows and two columns. Distinct star components cannot share a row (nor a column), since cells in that row (column) would be adjacent and connect the components. Conversely, any collection of these components with pairwise disjoint row sets and pairwise disjoint column sets is an edge-open packing. Hence the decomposition is necessary, sufficient, and unique.

**3. Counting.** Treat rows and columns as two independent labelled sorts of atoms. There is one horizontal edge on fixed row and fixed two-column set, one vertical edge on fixed two-row and fixed column set, and precisely four L corners on fixed two-row and two-column sets (four choices of center). Their respective bivariate exponential generating function contributions, with \(z\) marking edges, are \(zxy^2/2\), \(zx^2y/2\), and \(4z^2x^2y^2/(2!2!)=z^2x^2y^2\). Every unoccupied row or column is a singleton component, with contributions \(x\) and \(y\). The labelled set construction is therefore the stated exponential. Expanding the exponential, if \(a,b,c\) denote horizontal, vertical, and L components, respectively, gives exactly the finite coefficient formula above. The constraints leave \(m-a-2b-2c\) unused rows and \(n-2a-b-2c\) unused columns.

**4. Sharp maximum.** By symmetry, assume \(m\le n\). A packing with component counts \(a,b,c\) contains \(a+b+2c\) edges, consumes \(a+2b+2c\) rows, and consumes \(2a+b+2c\) columns. Thus its edge count is at most both \(m\) and \(n\). If \(m=n\) and equality \(a+b+2c=m=n\) held, the row constraint forces \(b=0\) and the column constraint forces \(a=0\); then \(2c=m\), impossible for odd \(m\). If \(m\) is even, take \(m/2\) L corners with disjoint row-column resources, attaining \(m\) edges whenever \(n\ge m\). If \(m\) is odd and \(n\ge m+1\), take \((m-1)/2\) L corners and one horizontal edge, consuming exactly \(m\) rows and \(m+1\) columns and attaining \(m\). If \(m=n\) is odd, take \((m-1)/2\) L corners, attaining \(m-1\). All boundary cases, including \(m=n=1\), follow.

**5. Exact square maximizer counts.** Write \(m=n=q\). For even \(q=2t\), equality of the edge count with \(q\) forces \((a,b,c)=(0,0,t)\), counted by \((q!)^2/t!\). For odd \(q=2t+1\ge3\), an optimum has \(q-1\) edges. Its used row and column counts equal \(q-1+b\) and \(q-1+a\), so \(a,b\le1\). As \(a+b+2c=q-1\) is even, either \((a,b,c)=(0,0,t)\) or \((1,1,t-1)\). Their contributions are \((q!)^2/t!\) and \((q!)^2/(4(t-1)!)\). For \(q=1\), only the empty edge set is possible.

## Verification

Running `python3 verify.py` independently generates the rook graph edges, builds the incompatibility relation directly by testing for a forbidden third edge, recursively counts every admissible selected edge subset, and compares each coefficient with the factorial formula. It agrees for all 21 rectangles \(1\le m\le n\le6\), accounting for 852,484 admissible edge subsets across those rectangles. It also checks the maximum and square extremal counts in every rectangle \(1\le m\le n\le20\). As sample identities,
\[
P_{3,3}(z)=1+18z+45z^2,
\qquad
P_{4,4}(z)=1+48z+360z^2+576z^3+288z^4.
\]
The finite checks are not the proof of the infinite-parameter result; Steps 1–5 are.

## Relationship to prior work

Edge-open packing and its induced-star characterization are established notions. Brešar, Dravec, Hedžet and Samadi (arXiv:2406.04020, Section 5) give general Cartesian-product lower bounds, not the present all-set polynomial or sharp rook-graph formula. Das and Santra (arXiv:2610.02275, first submitted 2026-10-01) develop algorithms for AT-free, chordal and convex bipartite graphs, using the induced-star characterization; the work does not supply a two-parameter rook-graph enumerator. Their earlier algorithmic paper (arXiv:2608.05310) likewise concerns algorithmic graph classes rather than these coefficients. Here the new ingredient is the rigid row-column resource decomposition, yielding a complete labelled counting formula and odd-square equality obstruction. The rook graph is also the line graph \(L(K_{m,n})\), so searches by that equivalent name are relevant.

## Limitations

The result is specific to two-coordinate rook graphs; it does not assert a corresponding formula for arbitrary Cartesian products or higher-dimensional Hamming graphs. All counts are for labelled rows and columns, without quotienting by board symmetries. The supporting computational tests are finite. A nonexhaustive bibliographic survey found no prior statement implying the complete formula, but independent validation and definitive bibliographic priority have not been established.

## References

1. G. K. Das and K. Santra, *Maximum Edge Open Packing on AT-Free, Chordal, and Convex Bipartite Graphs* (2026), arXiv:2610.02275, https://arxiv.org/abs/2610.02275 (first submitted 2026-10-01).
2. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, *Induced Matching vs Edge Open Packing: Trees and Product Graphs* (2024), arXiv:2406.04020, https://arxiv.org/abs/2406.04020, especially Section 5 and Corollary 5.3.
3. G. K. Das and K. Santra, *Maximum Edge Open Packing in Permutation, Interval, and Well-Partitioned Chordal Graphs* (2026), arXiv:2608.05310, https://arxiv.org/abs/2608.05310.
4. A. Pandey and K. Santra, *Edge Open Packing: Further Characterizations* (2025), arXiv:2508.01935, https://arxiv.org/abs/2508.01935.
5. G. Chelladurai, K. Kalimuthu and S. Soundararajan, *Edge Open Packing Sets in Graphs*, RAIRO–Operations Research 56 (2022), 3765–3776.
