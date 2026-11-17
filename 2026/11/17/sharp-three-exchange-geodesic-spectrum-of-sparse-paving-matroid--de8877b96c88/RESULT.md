# Sharp three-exchange geodesic spectrum of sparse-paving matroid base polytopes

## Finding

Let \(M\) be a sparse-paving matroid of rank \(k\) on \(n\) elements with \(3\le k\le n-3\). Write \(P(M)=\operatorname{conv}\{\mathbf1_B:B\text{ is a basis of }M\}\) in the standard \(0\)-\(1\) realization, and let \(G(M)\) denote its one-skeleton. For any two bases \(A,B\) with \(|A\setminus B|=|B\setminus A|=3\), let \(g_M(A,B)\) count *ordered* three-edge paths from \(\mathbf1_A\) to \(\mathbf1_B\) in \(G(M)\); equivalently, geodesics with these fixed endpoints.

There is an integer \(s(A,B)\in\{0,1,2,3,4\}\), the number of nonbases lying strictly between \(A\) and \(B\) in the Boolean exchange interval, such that
\[
\boxed{g_M(A,B)=36-4s(A,B)\in\{20,24,28,32,36\}.}
\]
In particular, **at least twenty of the thirty-six shortest exchange paths in the encompassing hypersimplex survive**, a sharp retention fraction of \(5/9\). Every value occurs for some sparse-paving matroid and pair of bases, and indeed for each allowed pair \((n,k)\) above.

More precisely, identify \(A\setminus B\) and \(B\setminus A\) with two three-element sets of labels. The eighteen possible internal exchange vertices fall into two nine-vertex layers. A locally permissible forbidden-vertex configuration is a stable set of their induced Johnson graph, with \(p\) deleted vertices in the first layer and \(q\) in the second. **All** possible such local configurations have bivariate enumerator
\[
\boxed{F(u,v)=1+9(u+v)+18(u^2+v^2)+6(u^3+v^3)+45uv+36(u^2v+uv^2)+18u^2v^2.}
\]
Thus the exact counts of local configurations with geodesic counts \(36,32,28,24,20\) are respectively \(1,18,81,84,18\) (a total of \(202\)). Each of these configurations is realizable by a sparse-paving matroid of the prescribed rank and ground-set size.

Equality \(g_M(A,B)=20\) occurs **exactly** when the four deleted internal vertices form a two-by-two crossed rook rectangle: in the first layer the forbidden cells are \((i,j)\) and \((h,\ell)\), with \(i\ne h\), \(j\ne\ell\), and in the second layer they are \((i,\ell)\) and \((h,j)\). There are exactly \(18\) such labelled sharp patterns for each ordered endpoint pair. The all-bases case gives the opposite extreme \(36\).

## Assumptions and scope

The ordinary Euclidean matroid base polytope is used only through its canonical **one-skeleton**, whose edges are one-element basis exchanges; every such edge has Euclidean length \(\sqrt2\). The distance under discussion is **graph distance**, not the ambient Euclidean distance or the combinatorial diameter. Paths are counted with ordered intermediate vertices and fixed ordered endpoints; reversing the endpoints reverses the paths without changing the number. The matroid may be disconnected; no representability assumption is made. Sparse paving means that the rank-\(k\) nonbases are pairwise nonadjacent in \(J(n,k)\). The condition \(3\le k\le n-3\) ensures that exchange-distance-three endpoint bases exist.

For any bases \(A,B\) at exchange distance three, put \(C=A\cap B\), \(X=A\setminus B=\{a_1,a_2,a_3\}\), and \(Y=B\setminus A=\{b_1,b_2,b_3\}\). Their exchange interval is the set of \(k\)-sets \(T\) with \(C\subseteq T\subseteq A\cup B\) and \(|T|=k\). It consists of \(20\) sets: the two endpoints, nine at graph distance one from \(A\), and nine at graph distance two from \(A\). The latter eighteen are the *internal* vertices. A forbidden set outside the exchange interval cannot lie on a three-edge shortest path between these endpoints.

## Proof

**1. One-skeleton and exchange interval.** The standard matroid base-polytope edge characterization identifies \(G(M)\) with the induced Johnson graph on the bases. Because every edge changes exactly one element, a three-edge path between \(A\) and \(B\) must delete each member of \(X\) exactly once and insert each member of \(Y\) exactly once. There are \(3!\) deletion orders and independently \(3!\) insertion orders, yielding \(36\) geodesics before any forbidden vertices are removed. Every intermediate set belongs to the twenty-set interval defined above; conversely every three-edge path within that interval is geodesic.

**2. Rook representation and adjacency.** Label a first-layer vertex \(L_{ij}=C\cup(X\setminus\{a_i\})\cup\{b_j\}\) by the cell \((i,j)\) of a three-by-three board. Label a second-layer vertex \(U_{ij}=C\cup\{a_i\}\cup(Y\setminus\{b_j\})\) by a cell on a second board. In either board, two distinct vertices are adjacent in the Johnson graph exactly when their cells share a row or column. Across the two boards, \(L_{ij}\) and \(U_{h\ell}\) are adjacent exactly when \(i\ne h\) and \(j\ne\ell\). Thus a stable set has nonattacking rooks within each board, and every cross-board pair of selected cells must share a row or a column.

**3. Number of surviving paths.** Each internal vertex lies on exactly \(2!\,2!=4\) of the original \(36\) three-edge geodesics: fixing a first- or second-layer cell determines one exchange, and the other two exchanges can be performed in any two orders on the deletion and insertion sides. A geodesic contains exactly one first-layer and one second-layer vertex, and these are adjacent. Since sparse-paving nonbases are stable, no geodesic can contain *two* deleted internal vertices. Consequently deletion losses are disjoint, and exactly \(4s\) geodesics are lost, proving \(g=36-4s\).

**4. The exact two-board enumeration.** On a three-by-three board, nonattacking rook subsets of sizes \(0,1,2,3\) number \(1,9,18,6\), respectively. To count a second-board set compatible with a fixed first-board set, use the cross-board adjacency rule from step 2:

- If the first board is empty, the second board contributes \(1+9v+18v^2+6v^3\).
- If it has one rook, say \((1,1)\), the second-board cells must share the first row or column, leaving five eligible cells. These yield one empty set, five singletons, and four nonattacking pairs. There are nine choices for the first rook, giving \(9u(1+5v+4v^2)\).
- If it has two rooks, say \((1,1),(2,2)\), the second board has precisely two eligible cells, \((1,2),(2,1)\), which are nonattacking. There are eighteen choices for the first-board pair, giving \(18u^2(1+2v+v^2)\).
- If it has three rooks, no second-board cell can share a row or column with all three, giving \(6u^3\).

Adding the cases yields the displayed \(F(u,v)\). Substituting \(u=v=z\) gives \(F(z,z)=1+18z+81z^2+84z^3+18z^4\). Thus \(s\le4\), all five values of \(s\) occur, and their precise counts follow. A four-rook configuration has two rooks on each board; the compatibility rule forces the second-board pair to occupy exactly the opposite corners of the rectangle determined by the first pair. There are \(\binom32^2\cdot2=18\) such patterns. This proves sharpness and the complete equality classification.

**5. Realization, including all sharp cases.** Take an arbitrary prescribed \((n,k)\) with \(3\le k\le n-3\), choose \(C\) of size \(k-3\) and disjoint triples \(X,Y\), and set \(A=C\cup X\), \(B=C\cup Y\). For any of the \(202\) locally permissible configurations, declare *only* its indicated internal \(k\)-sets to be nonbases among all \(\binom nk\) \(k\)-sets. They form a global Johnson stable set. The surviving sets satisfy basis exchange: for two surviving distinct bases and any element to remove, the possible one-element replacements are pairwise adjacent, so at most one is forbidden; when there is only one possible replacement, it is the surviving target itself. This constructs a sparse-paving matroid realizing exactly the chosen local configuration. Hence no values in the asserted spectrum are merely formal.

## Verification

The accompanying standalone Python 3 checker enumerates all \(2^{18}\) subsets of the internal vertices of \(J(6,3)\), retains precisely the \(202\) stable subsets, and for each independently counts three-edge paths in the induced basis graph. Its exact-integer result is:

`SPARSE_PAVING_THREE_EXCHANGE_PASS stable_sets=202 spectrum=20:18,24:84,28:81,32:18,36:1 sharp_patterns=18`

The checker also verifies that all eighteen maximizers use two deleted vertices in each layer. This finite exhaustive check validates the local combinatorial enumeration. The proof above establishes its applicability to *all* allowed ranks and ground-set sizes, rather than extrapolating the finite check to infinitely many parameters.

## Relationship to prior work

Ferroni's 2021 study of sparse-paving matroid base polytopes develops their circuit-hyperplane and hypersimplex geometry and Ehrhart polynomials. Ferroni and Schröter's 2023 preprint determines face-enumeration information for split matroid polytopes, including sparse paving. The known equivalence between Johnson-stable deleted \(k\)-sets and sparse-paving matroids, and the edge characterization of matroid base polytopes, are starting facts, **not novel contributions** here. The new claim is the complete three-exchange *geodesic multiplicity spectrum* in their one-skeleta, including the universal sharp surviving-path bound, bivariate local pattern count, and equality structures. A published spherical-width variance formula for sparse-paving matroid base polytopes counts compatible forbidden pairs and is not a statement about length-three geodesics. Nor do surface-area and Ehrhart formulas determine local geodesic counts.

## Limitations

No claim is made for endpoint pairs at exchange distance four or greater. At greater distances a geodesic may meet more than one nonadjacent deleted vertex, so the simple additive loss formula need not hold. This is a local three-exchange metric theorem, not a formula for the total number of all geodesics in the entire basis graph or for a global polytope diameter. The labelled number \(202\) counts possible local deleted configurations relative to fixed endpoints, not globally distinct matroids. Historical priority has not been independently certified; an earlier equivalent result under matroid basis graph or Johnson-code terminology remains possible.

## References

1. Luis Ferroni, *Matroids are not Ehrhart positive*, arXiv:2105.04465, first public version May 10, 2021. Sections 2--5 and 7 for sparse paving, matroid polytopes and Johnson-stable sets.
2. Luis Ferroni and Benjamin Schröter, *Face enumeration for split matroid polytopes*, arXiv:2310.05487, first public version October 9, 2023. Sparse-paving face-enumeration examples and formulas.
3. Published mathematical record, *Pair-sensitive spherical width variance of sparse-paving matroid polytopes*, published-finding corpus, October 25, 2026, identifier `2026/10/25/SCOPE-pair-sensitive-spherical-width-variance-of-sparse-paving-matroid--8948d9980837` (comparison only).
4. Published mathematical record, *Euclidean surface area of sparse-paving matroid base polytopes depends only on their nonbases*, published-finding corpus, November 8, 2026, identifier `2026/11/8/SCOPE-euclidean-surface-area-of-sparse-paving-matroid-base-polytopes-d--f28b7ecdc05e` (comparison only).
