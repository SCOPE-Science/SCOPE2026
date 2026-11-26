# Exact maximal-bipartite-set enumerators of rook graphs and asymptotic half-splitting

## Finding

For integers \(2\le m\le n\), let \(R_{m,n}=K_m\square K_n\) be the graph of an \(m\)-by-\(n\) board, with cells adjacent precisely when they share a row or a column. Let
\[B_{m,n}(z)=\sum_{S\text{ inclusion-maximal bipartite}}z^{|S|},\]
where the summation runs over labeled vertex subsets whose induced graph is bipartite and cannot remain bipartite after any unselected vertex is added.

For \(m<n\), write \(P_m(x_1,\ldots,x_m)=1+\sum_{i=1}^{m}x_i+\sum_{1\le i<j\le m}x_ix_j\). Then
\[\boxed{B_{m,n}(z)=z^{2m}[x_1^2\cdots x_m^2]P_m(x_1,\ldots,x_m)^n.}\]

Define \(A_r\) for \(r\ge0\) by
\[\sum_{r\ge0}\frac{A_r}{(r!)^2}t^r=\exp\!\left(\sum_{j\ge2}\frac{t^j}{2j}\right)=\frac{e^{-t/2}}{\sqrt{1-t}}.\]
Thus \(A_0=1\), \(A_1=0\), and \(A_2=1\), \(A_3=6\), \(A_4=90\), \(A_5=2040\). For every \(r\ge2\),
\[\boxed{B_{r,r}(z)=r^2A_{r-1}z^{2r-1}+A_rz^{2r}.}\]

If \(S_r\) is chosen uniformly among all inclusion-maximal bipartite induced vertex sets of \(R_{r,r}\), then
\[\boxed{\Pr(|S_r|=2r-1)=\frac12+\frac{1}{8r}+O(r^{-2})\qquad(r\to\infty).}\]
For \(r=2\), the first coefficient is zero, and there is exactly one maximal set (the whole four-cycle). For \(r\ge3\), both sizes occur. This is an asymptotic statement about **uniformly sampled maximal sets**, not about maximal sets produced by a greedy procedure.

## Assumptions and scope

All graphs are finite and simple. Rows and columns are individually labeled, and the enumerator counts distinct cell subsets without quotienting by graph automorphisms. Inclusion-maximal means maximal under adding one cell, which is equivalent to inclusion-maximality because bipartiteness is hereditary. The theorem covers \(2\le m\le n\); exchanging coordinates covers the reverse inequality. It does not assert the same formulas for boards with just one row or one column.

## Proof

**1. Incidence reduction.** Identify the cell \((i,j)\) with edge \(ij\) of \(K_{m,n}\). The rook graph is the line graph of this complete bipartite graph. For any selected cell set, write \(d_i\) and \(e_j\) for its row and column occupancies. An induced triangle arises if and only if some \(d_i\) or \(e_j\) is at least three: three pairwise incident edges of a bipartite graph share one endpoint. If every occupancy is at most two, the chosen incidence edges form a disjoint union of paths and even cycles. Their line graph is a union of paths and even cycles (also allowing isolated vertices), and is bipartite. Therefore the selected rook subgraph is bipartite **exactly when** all row and column occupancies are at most two. This incidence equivalence is already established in Bachstein–Goddard, Observation 13.

**2. Exhaustive maximality classification.** The selected set is maximal if and only if every unselected cell has its row or column occupancy equal to two. Define \(U\) to be the set of rows with occupancy at most one, and \(W\) the analogous set of columns. If both are nonempty, every cell in \(U\times W\) must already be selected. Since each such row or column has occupancy at most one, necessarily \(|U|=|W|=1\). Denote this unique selected cell by \((i,j)\). Its row and column have occupancy exactly one, and every other row and column has occupancy two. Counting the same selected cells by rows and columns now gives \(2m-1=2n-1\), hence \(m=n\). Conversely, any pattern of this form is maximal.

If \(U=\varnothing\), every row is saturated at occupancy two, giving \(2m\) selected cells and requiring \(m\le n\). If \(W=\varnothing\), every column is saturated and \(n\le m\). Consequently, for \(m<n\), the **only** maximal patterns have every row saturated. For \(m=n=r\), the patterns are precisely (i) all rows and columns of occupancy two, or (ii) one isolated selected row-column incidence, with all remaining rows and columns of occupancy two. Here 'isolated' refers to the selected incidence subgraph, not to the rook graph. The size-support and lower bipartite number of rook graphs were obtained in Bachstein–Goddard, Observation 14; what follows enumerates these classes coefficientwise.

**3. Rectangular count.** In a column there are zero, one, or two chosen cells. Encode these choices respectively by \(1\), \(x_i\), or \(x_ix_j\) with \(i<j\). Raising \(P_m\) to the \(n\)-th power independently labels the columns. Extracting the coefficient of \(x_1^2\cdots x_m^2\) forces every row to contain two cells. There is no factorial correction: each monomial records one column subset. This proves the formula for \(m<n\).

**4. Balanced count.** A pattern of type (i) is a spanning simple two-regular bipartite graph with labeled partite classes each of order \(r\). It is a disjoint union of alternating cycles of lengths \(2j\), \(j\ge2\). On fixed sets of \(j\) labeled vertices in each shore, the number of such cycles is \(j!(j-1)!/2\). The labeled exponential formula therefore gives the generating function for \(A_r\) displayed above. Type (ii) has \(r^2\) choices of its exceptional row-column incidence, and a completely independent two-regular bipartite graph on the remaining \(r-1\) rows and \(r-1\) columns. It contributes exactly \(r^2A_{r-1}\) sets of size \(2r-1\); the two types are disjoint and exhaustive.

**5. Asymptotic split and first correction.** Put \(a_r=A_r/(r!)^2=[t^r](1-t)^{-1/2}e^{-t/2}\). The exact probability of the smaller type is
\[p_r=\frac{r^2A_{r-1}}{A_r+r^2A_{r-1}}=\frac{a_{r-1}}{a_r+a_{r-1}}.\]
Expanding the entire factor about its dominant singularity at \(t=1\),
\[e^{-t/2}=e^{-1/2}\left(1+\frac{1-t}{2}+O((1-t)^2)\right),\]
and using \([t^r](1-t)^{-1/2}=\binom{2r}{r}/4^r=(\pi r)^{-1/2}(1-1/(8r)+O(r^{-2}))\) and \([t^r](1-t)^{1/2}=-(2\sqrt\pi)^{-1}r^{-3/2}(1+O(r^{-1}))\), one obtains by standard coefficient transfer (with the analytic remainder)
\[a_r=\frac{e^{-1/2}}{\sqrt{\pi r}}\left(1-\frac{3}{8r}+O(r^{-2})\right).\]
It follows that \(a_{r-1}/a_r=1+1/(2r)+O(r^{-2})\), and substitution yields \(p_r=1/2+1/(8r)+O(r^{-2})\), as required.

## Verification

The accompanying standalone \(\texttt{verify.py}\) independently constructs labeled rook-graph edges, checks induced bipartiteness by breadth-first two-coloring, and tests every possible one-vertex extension for maximality. It agrees with the proposed polynomial for the eight parameter pairs \((2,2)\), \((2,3)\), \((2,4)\), \((2,5)\), \((3,3)\), \((3,4)\), \((3,5)\), and \((4,4)\), comprising 104272 graph-vertex subsets in total. It additionally checks a state-based rectangular count and the balanced exact coefficient recurrence. Run with \(\texttt{python verify.py}\). These experiments are finite corroboration; the proof above is all-order.

For example, \(B_{3,3}(z)=9z^5+6z^6\), \(B_{4,4}(z)=96z^7+90z^8\), and \(B_{3,4}(z)=114z^6\).

## Relationship to prior work

Bachstein and Goddard (first public release February 7, 2023) already prove the induced-bipartite/2-matching equivalence and the lower bipartite number of rectangular rook graphs in Observations 13–14. The support \(\{2r-1,2r\}\) for balanced boards (away from its small boundary) and its singleton support on unequal boards are therefore **not** asserted as new. The present contribution is the complete labeled cardinality **multiplicities**, the balanced generating function, and the asymptotic half-split with its first-order bias. Goddard–Kuenzel–Melville (2019/2020) investigate well-bicovered graphs and Cartesian products, but do not give this count. Madsen–Nielsen–Skjernaa (2002) give general bounds and algorithms for listing maximal induced bipartite subgraphs, without the rook-family coefficient formula. The enumeration of labeled two-regular bipartite graphs is a classical component count and is used, not claimed as a novel standalone fact.

## Limitations

This theorem concerns rook graphs with both clique factors of order at least two. The all-order proof uses a standard analytic coefficient-transfer estimate; the verifier checks finite cases only. Priority is provisional: equivalent counting formulas could exist in differently indexed regular-bipartite-matrix literature. The known qualitative rook-graph classification and all external underlying enumerative ingredients are explicitly credited. No independent external mathematical audit is claimed.

## References

1. Anna Bachstein and Wayne Goddard, *The Lower Bipartite Number of a Graph*, Mathematica Pannonica 29 (2023), 49–56, DOI: 10.1556/314.2023.00003. First publicly available 2023-02-07; primary MSC2020 05C69. Observations 13–14.
2. Wayne Goddard, Kirsti Kuenzel, and Eileen Melville, *Graphs in which all maximal bipartite subgraphs have the same order*, arXiv:1909.07503 (2019); Aequationes Mathematicae 94 (2020), 1241–1255.
3. Bolette Ammitzbøll Madsen, Jesper Makholm Nielsen, and Bjarke Skjernaa, *On the Number of Maximal Bipartite Subgraphs of a Graph*, BRICS Report Series RS-02-17 (2002), DOI: 10.7146/brics.v9i17.21735.
