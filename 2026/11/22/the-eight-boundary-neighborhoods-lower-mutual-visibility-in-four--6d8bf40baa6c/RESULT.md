# The eight boundary neighborhoods: lower mutual visibility in four-cycle cylinders

## Finding
For every integer \(n\ge2\), the lower ordinary mutual-visibility number of the Cartesian cylinder \(G_n=C_4\square P_n\) is exactly
\[
\boxed{\mu^-(G_n)=4.}
\]
For \(n\ge3\), **all** inclusion-maximal mutual-visibility sets of minimum size are the eight distinct closed neighborhoods of boundary vertices,
\[
\{N_{G_n}[(r,0)],N_{G_n}[(r,n-1)]:r\in\mathbb Z/4\mathbb Z\}.
\]
For \(n=2\), when \(G_2\cong Q_3\), there are exactly ten such sets: its eight vertex closed neighborhoods and its two bipartition classes. The count is of labelled vertex subsets, not symmetry classes.

## Assumptions and scope
Graphs are finite, simple and undirected, and paths are shortest in the unweighted graph metric. The vertex set of \(G_n\) is \(\{(r,c):r\in\mathbb Z/4\mathbb Z,\ 0\le c<n\}\). Two vertices are adjacent if they agree in the second coordinate and are consecutive modulo four in the first, or if they agree in the first coordinate and are in consecutive path columns.

For \(S\subseteq V(G)\), members \(u,v\in S\) are *mutually visible in* \(S\) if a shortest \(u,v\)-path has all its internal vertices in \(V(G)\setminus S\). A set is mutually visible when all its pairs are; it is *inclusion-maximal* if no outside vertex can be added while retaining the property. Define \(\mu^-(G)\) as the minimum cardinality among inclusion-maximal ordinary mutually visible sets, not the largest such set and not the total-visibility variant. The notation \(N_G[x]\) means \(\{x\}\cup N_G(x)\).

## Proof
**1. Boundary-neighborhood upper bound.** Brešar and Yero's Neighborhood Lemma applies to any vertex \(x\) if each pair of nonadjacent neighbors of \(x\) has a second common neighbor outside \(N[x]\); it then guarantees \(N[x]\) is a maximal mutually visible set. For any boundary vertex \(x=(r,0)\), its three neighbors are \((r-1,0),(r+1,0),(r,1)\). The first two share the additional common neighbor \((r+2,0)\). The other two pairs share \((r-1,1)\) and \((r+1,1)\), respectively. These are all outside \(N[x]\). The opposite boundary is symmetric. Thus every one of the advertised neighborhoods is inclusion-maximal and has size four. For \(n=2\), these are the eight distinct neighborhoods of the cube.

**2. A bounded-column lemma for the lower bound and rigidity.** Consider an arbitrary selection \(S\) of at most four vertices of \(C_4\square P_n\). Let its \(k\le4\) distinct selected column indices be \(a_1<\cdots<a_k\). Replace the vacant initial and terminal column runs by runs of length \(\min(a_1,2)\) and \(\min(n-1-a_k,2)\); replace each gap \(a_{i+1}-a_i\) between successive selected columns by \(\min(a_{i+1}-a_i,4)\). Retain each selected vertex's row and relative marked column. This defines a compressed selection \(S'\subseteq C_4\square P_m\) with
\[
m\le1+2+3\cdot4+2=17.
\]
The two assertions are equivalent before and after this compression: (i) \(S\) is mutually visible; and (ii) \(S\) is inclusion-maximal mutually visible.

Here is a geodesic-normal-form proof of that compression claim. Every geodesic between \((r,c)\) and \((s,d)\) changes its path coordinate monotonically through precisely \(|d-c|\) steps, and changes its cyclic row coordinate by exactly \(\operatorname{dist}_{C_4}(r,s)\le2\) steps in one shortest cyclic direction (there can be two choices only when rows are opposite). Thus the row changes, at most two, can be inserted at column positions during this monotone traversal. Obstacles from a fixed selection occur only at its marked columns. Within a gap with no marked columns, any row changes can be moved to the bounding marked columns or to unmarked interior columns. If both changes must be made strictly in the interior, they can be made consecutively at the same unmarked column: no obstacle is present there. Consequently for a pair of selected endpoints, existence of a selected-interior-free geodesic depends only on which marked columns coincide, their order, and whether each intervening gap has length one or at least two. This proves preservation of (i), including same-column endpoint pairs.

For (ii), test one possible added vertex \(w\). If its column is already marked, preserve that column exactly; otherwise it lies in an initial run, a terminal run, or between two consecutive marked columns. Its influence on avoiding geodesics is still controlled by at most two cyclic row changes; relative to adjacent marked columns, the only distinct positions that matter are distance one and distance at least two. Hence the two outer run lengths can be capped at two. In an interior gap, the cases are \((1,\ge1)\), \((\ge2,1)\), and \((\ge2,\ge2)\), together with their exact short-gap instances. A gap capped at four realizes all of these, with one additional empty column on either side of \(w\) in the last case. The preceding row-switch argument works separately on the two sides of \(w\), now treating \(w\) as a marked obstacle, so it gives equivalence for the pair checks in \(S\cup\{w\}\) in the original and compressed cylinder. Conversely every possible added-vertex column of the compressed cylinder has a representative in the original with the same case. Therefore an extension exists before compression if and only if one exists after compression, proving (ii). This is an exact finite reduction for selections of size at most four, not an asymptotic approximation.

**3. Finite classification at the sharp bound.** The standalone `cylinder_minfacet.cpp` builds shortest-path internal-vertex masks for each pair in each cylinder of heights \(2\le m\le17\). It examines *every* three-subset and four-subset, checks whether every selected pair has a geodesic with no other selected interior vertex, then tests adding each outside vertex. Exhaustive output `minfacet_counts.txt` confirms:
\[
\begin{array}{c|cc}
 m & \text{inclusion-maximal three-sets} & \text{inclusion-maximal four-sets}\\\hline
 2 & 0 & 10\\
 3,4,\ldots,17 & 0 & 8
\end{array}
\]
The program does not merely count: it compares the full collection of four-subsets against the explicitly constructed boundary neighborhoods, together with the two checkerboard bipartition classes at \(m=2\), and reports exact equality at every order. `cylinder_bfs_verify.cpp` independently constructs the graph and tests blocked-vertex shortest-path distances for every three- and four-subset at \(2\le m\le8\); both checkers agree. `compression_smoke.py` separately tests compression on 1,430 selected configurations, including heights as large as 48, and agrees on feasibility and maximality; these finite tests corroborate, but do not replace, the normal-form lemma.

**4. Transfer to all path lengths and exclude smaller facets.** Every edge of \(C_4\square P_n\), \(n\ge2\), lies on a cycle, so the graph has no bridge. By the cut-edge characterization of lower mutual-visibility number two (Brešar and Yero, Theorem 13), \(\mu^-(G_n)\ne2\). In a nontrivial connected graph, sets of size at most one are not inclusion-maximal. If an inclusion-maximal triple existed at any length, the compression lemma would give one at some \(2\le m\le17\), contradicting the exhaustive certificate. Hence \(\mu^-(G_n)\ge4\), matching step 1.

Any minimum four-set compresses to one of the enumerated four-sets. For \(n\ge3\), its compression can have height two only when the original path has exactly two columns; thus for \(n\ge3\), the compressed set is a terminal neighborhood. The compression keeps whether the selected column lies at a boundary and whether its unique longitudinal neighbor is one step inward, so the original is the corresponding terminal neighborhood. For \(n=2\), the two additional bipartition classes are present and are directly confirmed by the certificate. No other minimum sets occur. \(\square\)

## Verification
The finite case reduction has a mathematical normal-form proof in step 2. Its computer certificate is self-contained and requires no external datasets. Compile with `g++ -O2 -std=c++17 cylinder_minfacet.cpp -o check`; run `for n in $(seq 2 17); do ./check "$n"; done`. Every row must have `size3_facets=0`, `incorrect=0`, `agreement=YES` and `size4_facets` equal ten for \(n=2\) or eight otherwise. The independent BFS checker is compiled likewise and run at heights 2 through 8. The standard-library-only compression test runs as `python3 compression_smoke.py` and reports `COMPRESSION_TEST_OK 1430 1337 18`. Actual execution outputs are included in three companion text files. The 128-bit bitset implementation covers up to 68 vertices as used in the certified range. Tests beyond the certified reduction range are independent spot checks rather than infinite proofs.

## Relationship to prior work
Brešar and Yero introduce the lower mutual-visibility invariant in the July 2023 preprint, establish the Neighborhood Lemma, characterize graphs with lower invariant two, and derive the exact value three for rectangular path grids. Their concluding **Problem 1 explicitly asks** for lower (total) mutual-visibility numbers of Cartesian cylinders \(C_m\square P_n\). The present result addresses the smallest simple even cycle and strengthens the numerical answer to a full classification of minimum inclusion-maximal sets; the cited lemmas alone establish neither absence of maximal triples nor the eight-set rigidity.

Cicerone, Di Stefano and Klavžar investigate ordinary *maximum* mutual visibility and related Cartesian products, a different extremal quantifier. The visibility-polynomial literature concerns all mutually visible sets rather than directly establishing the minimum maximal facets here. A related classification of lower mutual visibility in odd three-row tori treats \(C_3\square C_{2k+1}\), not a four-cycle cylinder; another circular-ladder result is confined to \(C_{2k+1}\square K_2\). Neither covers \(C_4\square P_n\) for arbitrary \(n\). Results on the four-cut complexes of the same graph family concern a different invariant.

## Limitations
The theorem is for ordinary \(C_4\square P_n\), \(n\ge2\), only; it does not determine lower mutual visibility for wider cylinders \(C_m\square P_n\) or lower total visibility. The finite enumeration is exhaustive only through height 17; all-height validity relies on the explicit bounded-column lemma and its proof. No formal proof assistant or independent expert audit was used. Unindexed equivalent literature remains a priority risk.

## References
1. B. Brešar and I. G. Yero, *Lower (total) mutual-visibility number in graphs*, first public preprint 2023-07-06, arXiv:2307.02951v1, later *Applied Mathematics and Computation* 465 (2024), 128411, doi:10.1016/j.amc.2023.128411. https://arxiv.org/abs/2307.02951
2. S. Cicerone, G. Di Stefano and S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, arXiv:2112.13024 (2021). https://arxiv.org/abs/2112.13024
3. C. Bujtás, S. Klavžar and J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066, *Aequationes Mathematicae* (2025). https://arxiv.org/abs/2412.03066
4. *Lower mutual-visibility number of odd three-row tori*, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-lower-mutual-visibility-number-of-odd-three-row-tori--543189f5b94a/RESULT.md (scientific comparison).
