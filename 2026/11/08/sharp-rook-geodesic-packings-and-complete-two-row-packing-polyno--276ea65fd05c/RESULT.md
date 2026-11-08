# Sharp rook-geodesic packings and complete two-row packing polynomials

## Finding
Let \(R_{m,n}=K_m\square K_n\) for integers \(m,n\ge2\). A *geodesic packing* is a family of pairwise vertex-disjoint maximal shortest paths. The following statements hold jointly.

**Sharp packing number for every rectangle.**
\[
\operatorname{gpack}(R_{m,n})=\left\lfloor\frac{mn}{3}\right\rfloor.
\]

**Exact all-packing polynomial for two rows.** Fix \(n\ge2\). Let \(\mathcal P_n(z)\) count all (including empty) geodesic packings of \(R_{2,n}\) by the number of paths, and let \(\mathcal M_n(z)\) count those inclusion-maximal under adding a disjoint maximal geodesic. Define \((q)_{\underline i}=q!/(q-i)!\) for integer \(0\le i\le q\), and \((q)_{\underline i}=0\) otherwise. Then
\[
\mathcal P_n(z)=\sum_{k=0}^{\lfloor2n/3\rfloor}\binom nk z^k
\sum_{i=0}^k\binom ki(n-k)_{\underline i}(n-k)_{\underline{k-i}}.
\]
Writing \(\mathbf1_E\) for the indicator of a condition \(E\),
\[
\mathcal M_n(z)=
\sum_{k=\lceil n/2\rceil}^{\lfloor2n/3\rfloor}
\frac{n!}{(n-k)!}\binom{n-k}{2k-n}2^{2n-3k}z^k
+\mathbf1_{n\equiv1\pmod3}\frac{n!}{((n-1)/3)!}z^{2(n-1)/3}.
\]
The inclusion-maximal cardinality spectrum is the full integer interval
\[
\left\{\left\lceil\frac n2\right\rceil,\ldots,\left\lfloor\frac{2n}{3}\right\rfloor\right\}.
\]

**Exact number of maximum packings.** If \(n=3h\), \(3h+1\) or \(3h+2\), respectively, the coefficient of \(z^{\lfloor2n/3\rfloor}\) in \(\mathcal P_n(z)\) is
\[
\frac{n!}{h!},\qquad \frac{(2h+1)n!}{h!},\qquad \frac{2n!}{h!}.
\]
For \(n=3h+1\) in the stated domain, \(h\ge1\); for \(n=3h+2\), \(h\ge0\).

## Assumptions and scope
All graphs are finite, simple and undirected; rows and columns are labelled. Vertices of \(R_{m,n}\) are pairs \((r,c)\) with \(0\le r<m\) and \(0\le c<n\); adjacency means sharing a row or column. Different paths in a packing have disjoint vertex sets. Path direction and ordering of the family are not counted. A maximal geodesic cannot be extended as a proper subpath of another shortest path. **Inclusion-maximal packing** does not mean maximum-cardinality packing: the former cannot be augmented by one disjoint maximal geodesic; the latter has the largest possible number of paths. The empty family is included in \(\mathcal P_n\).

## Proof
**1. Classify the maximal geodesics.** For \(m,n\ge2\), a pair of board cells in distinct rows and columns is at distance two; its two shortest paths go through the opposite corners of their \(2\)-by-\(2\) rectangle. Any geodesic of length two is an L-shaped triple comprising a pivot, another cell in its row, and another in its column. The graph diameter is two, so these paths are maximal. Every edge belongs to such a length-two geodesic (choose a cell outside its row or column), so no shorter geodesic is maximal. Every packing path uses three vertices. Therefore \(\operatorname{gpack}(R_{m,n})\le\lfloor mn/3\rfloor\).

**2. Attain the bound for all rectangles.** Disjoint rectangular subboards can be packed independently because every L-shaped triple remains a diameter-two maximal geodesic in the full rook graph. Three base constructions are enough: the \(2\)-by-\(2\) board contains one L; the \(2\)-by-\(3\) board is tiled by two L's; and the \(3\)-by-\(3\) board is tiled by three L's (see the explicit reproducible witnesses in `verify_rook_packing.py`). A \(2\)-by-\(4\) board contains two L's by using its first three columns. A \(4\)-by-\(3\) board is tiled by two stacked \(2\)-by-\(3\) boards; a \(4\)-by-\(2\) board has two disjoint L's by splitting it into \(2\)-by-\(2\) boards. The remaining exceptional \(4\)-by-\(4\) board admits five disjoint L's with the following zero-indexed pivot/wing triples:

`[(0,1),(1,1),(0,2)]`; `[(1,3),(0,3),(1,0)]`; `[(2,2),(1,2),(2,0)]`; `[(3,1),(2,1),(3,0)]`; `[(3,3),(2,3),(3,2)]`.

For two rows and arbitrary width, strip off three-column blocks, reducing to widths two, three and four. For three rows, split the width into blocks of width two, except for a single three-column block when the width is odd. For four rows, strip three-column blocks, reducing to widths two, three and four. Finally, for every height at least five, remove three rows (which can be tiled perfectly by the preceding three-row construction) and recurse on the remaining height. Each removed strip contains a number of cells divisible by three and is fully packed; the base remainder uses exactly the floor of its size divided by three. Hence all rectangles attain the vertex-count bound.

**3. Enumerate all packings in two rows.** In \(R_{2,n}\), every L uses *both* cells of its pivot column and one additional cell, called a wing, in its pivot's row and in a different column. No two paths in a packing share a pivot column, and no wing may occupy a pivot column. For a packing of \(k\) paths, choose its \(k\) pivot columns in \(\binom nk\) ways and write \(q=n-k\) for the number of other columns. If \(i\) pivots have their wings in the first row, there are \(\binom ki\) row assignments, \((q)_{\underline i}\) distinct wing-column injections in the first row and \((q)_{\underline{k-i}}\) in the second row. The two rows may independently use the same nonpivot column, but not the same cell. Every packing is recovered uniquely from this data. Summation proves the formula for \(\mathcal P_n\). The coefficient vanishes unless \(k\le2q\), equivalently \(k\le\lfloor2n/3\rfloor\); conversely an assignment exists for every \(k\) in that range.

**4. Characterize and enumerate maximal packings.** A packing is inclusion-maximal exactly when the unoccupied cells contain no L. All unoccupied cells lie in the \(q\) nonpivot columns. An L exists among them precisely when some completely unoccupied column coexists with another unoccupied cell in a different column: the full column is then the pivot column of an L, and the other cell is a wing. Consequently a packing is maximal precisely in one of two disjoint cases: (a) no nonpivot column has both cells unoccupied, or (b) the only unoccupied cells are the two in one nonpivot column.

In case (a), let \(i\) be the number of first-row wings, and let \(d=k-q=2k-n\). The unoccupied first-row and second-row cell-column sets are disjoint, of sizes \(q-i\) and \(q-k+i\), respectively. The number of ways to choose both disjoint sets is \(\binom qi\binom i d\). For every such choice, assign the \(i\) labelled pivots of the first row bijectively to its occupied nonpivot cells in \(i!\) ways, and do the analogous assignment in \((k-i)!\) ways for the second row. After choosing pivots and their row labels, the count in case (a) at rank \(k\) is
\[
\binom nk\sum_i\binom ki i!(k-i)!\binom qi\binom i d
=\frac{n!}{q!}\binom qd 2^{q-d}.
\]
The identity follows from \(\binom qi\binom id=\binom qd\binom{q-d}{i-d}\) and the binomial theorem; out-of-range binomial terms are zero. The condition \(q-d=2n-3k\ge0\) and \(d\ge0\) is exactly \(\lceil n/2\rceil\le k\le\lfloor2n/3\rfloor\), and every coefficient in this interval is strictly positive.

In case (b), there are exactly two unoccupied cells, so \(2n-3k=2\). This occurs exactly when \(n=3h+1\) and \(k=2h\). Choose the \(2h\) pivot columns, the one empty nonpivot column, and assign \(h\) pivot wings bijectively to the other \(h\) nonpivot columns in each row. The resulting number is
\[
\binom{3h+1}{2h}(h+1)\binom{2h}{h}(h!)^2=\frac{(3h+1)!}{h!}.
\]
Adding the two cases proves the formula for \(\mathcal M_n\) and its consecutive support.

**5. Count maximum packings.** At \(k=\lfloor2n/3\rfloor\), every packing is necessarily inclusion-maximal. Substituting \(n=3h\), \(3h+1\), or \(3h+2\) into the preceding formula for \(\mathcal M_n\) gives respectively \(n!/h!\), \((2h+1)n!/h!\), and \(2n!/h!\). This completes the proof.

## Verification
`verify_rook_packing.py` requires only Python's standard library. It directly constructs adjacency lists, independently obtains graph distances by breadth-first search, enumerates every length-two shortest path and every vertex-disjoint path family for \(2\le n\le7\), and tests inclusion-maximality by searching for an additional disjoint geodesic. All coefficients of both polynomials agree for those orders. Independently, the constructive rectangle algorithm produces packings of size \(\lfloor mn/3\rfloor\) for all 225 ordered pairs with \(2\le m,n\le16\), checking every chosen triple and all disjointness conditions. Finite checks support but do not replace the unrestricted mathematical proof.

## Relationship to prior work
Manuel, Brešar and Klavžar [1] introduced geodesic packing and explicitly noted that maximal geodesics in rook graphs are L-shaped paths of length two. Their Lemma 2.3 supplies the vertex-count upper bound, and their Proposition 2.6 determines the *transversal* number of square rook graphs. They do not give the complete rectangular packing equality or the two-row all-packing/maximal-packing enumerators in the inspected relevant sections. The sharp rectangular equality extends their upper bound; the two-row enumerators classify the whole packing set system rather than solely its maximum.

Peterin and Semanišin [2] study the related *covering* (hitting) problem of maximal shortest paths, not enumeration of vertex-disjoint path families. General induced three-vertex-path packings provide related formulations, since in rook graphs these are exactly the maximal geodesics. Equivalence to an unnoticed existing formula in that broader literature remains a priority risk.

## Limitations
The exact two-row formulas do not claim to count all packings for arbitrary rectangular heights. The unrestricted statement for general rectangles concerns only the maximum packing number. The result does not assert uniqueness or publication priority, and it has not been independently mathematically audited. The formulas count labelled board configurations and path families without order or orientation; using a different convention changes multiplicities.

## References
[1] P. Manuel, B. Brešar, and S. Klavžar, *Geodesic packing in graphs*, first public arXiv submission 2022-10-27, arXiv:2210.15325; *Applied Mathematics and Computation* 459 (2023), 128277, DOI:10.1016/j.amc.2023.128277.

[2] I. Peterin and G. Semanišin, *On the Maximal Shortest Paths Cover Number*, *Mathematics* 9 (2021), article 1592, DOI:10.3390/math9141592.
