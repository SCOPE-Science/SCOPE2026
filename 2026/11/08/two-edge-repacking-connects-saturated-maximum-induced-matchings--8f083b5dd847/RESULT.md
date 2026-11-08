# Two-edge repacking connects saturated maximum induced matchings of square rook graphs

## Finding

For every integer \(t\ge1\), let \(G_t=K_{3t}\square K_{3t}\). Its maximum induced matchings have \(2t\) edges, and they are all **frozen under a single-edge exchange**. Nevertheless, permitting the simultaneous removal of exactly two matching edges and insertion of two others makes the complete family connected. The two-edge exchange graph is vertex-transitive and regular of degree
\[
13t^2-5t.
\]
Its number of vertices is
\[
\left(\frac{(3t)!}{2^t t!}\right)^2.
\]
The last formula follows from a previously available induced-matching packing enumerator and is included to quantify the reconfiguration result, **not** as a new counting claim. The main contribution is the sharp exchange threshold and the exact two-exchange valency across an infinite family.

For \(t=1\), the exchange graph is \(K_9\). For \(t=2\), it has 8100 vertices, 170100 edges and diameter four.

## Assumptions and scope

All graphs are finite, simple and labeled. The rook graph \(K_n\square K_n\) has vertices \((r,c)\), with \(r,c\in\{1,\dots,n\}\), and edges precisely between distinct vertices in a common row or column. An **induced matching** is an edge set whose endpoints induce a disjoint union of individual edges, without edges between endpoints of two distinct members. A *maximum* induced matching has largest cardinality, rather than merely being inclusion-maximal.

Write \(\mathcal F_t\) for all maximum induced matchings of \(G_t\). The **one-edge exchange graph** joins distinct \(M,N\in\mathcal F_t\) if \(|M\setminus N|=|N\setminus M|=1\). The **two-edge exchange graph** \(\mathcal R_t\) joins them if both differences have cardinality two. The simultaneous replacement has no feasibility requirement during an intermediate, temporarily smaller set; only the two endpoints must be maximum induced matchings. Horizontal edges join cells in a common row, vertical edges cells in a common column.

## Proof

**1. Resource bound and saturation.** Two different edges of an induced matching cannot use a common row coordinate or a common column coordinate: such a coincidence would create an edge between endpoints of two selected edges. If an induced matching has \(h\) horizontal and \(v\) vertical members, it consequently uses exactly \(h+2v\) distinct rows and \(2h+v\) distinct columns. In \(G_t\),
\[
h+2v\le3t,\qquad 2h+v\le3t,
\]
so \(h+v\le2t\). A set with \(t\) horizontal and \(t\) vertical edges is obtained by partitioning the rows into \(t\) singletons and \(t\) pairs, similarly partitioning columns, and matching horizontal singleton rows with column pairs and vertical row pairs with singleton columns. This realizes the upper bound. At equality both displayed inequalities are equalities; solving gives \(h=v=t\). Thus *every* maximum matching uses every row and column exactly once in the coordinate-resource sense.

**2. Classification and count.** With \(n=3t\), represent the row resources by \(t\) labeled singleton slots (one for each horizontal edge) and \(t\) labeled unordered pair slots (one for each vertical edge). Assignments number \(n!/2^t\). Columns have the dual slot arrangement with the same number of assignments. A matching is represented \((t!)^2\) times, by simultaneously relabeling the \(t\) horizontal and the \(t\) vertical edges. Therefore
\[
|\mathcal F_t|=\left(\frac{n!}{2^t t!}\right)^2.
\]
This agrees with the earlier complete induced-matching enumerator of rectangular rook graphs; the enumeration is not asserted to be new.

**3. One-edge freezing.** Delete one horizontal edge from a saturated maximum matching. All remaining edges consume every row and column except exactly the old horizontal edge's one row and two columns. Any replacement preserving size \(2t\) must again saturate all resources, and hence must be the same horizontal edge. For a deleted vertical edge the dual argument applies. Thus distinct maxima never differ in exactly one edge.

**4. Exact two-edge degree.** Select which two edges are removed. If they are both horizontal, the two freed rows and four freed columns must be repartitioned as two horizontal edges. There are \(\binom42=6\) possibilities, one unchanged, hence five neighbors. The same is true of two vertical edges. If one is horizontal and one vertical, three rows and three columns are freed. To reconstruct one horizontal and one vertical edge choose the horizontal singleton row (three options) and the vertical singleton column (three options): nine possibilities, one unchanged, hence eight neighbors. Other replacement orientations cannot saturate the resources. No neighbor is double-counted, since the removed edges are its unique difference from the original matching. The valency is therefore
\[
5\binom t2+5\binom t2+8t^2=13t^2-5t.
\]
In particular \(\mathcal R_1\cong K_9\), and the number of edges of \(\mathcal R_2\) is \(8100\cdot42/2=170100\).

**5. Connectivity.** Temporarily fix the **column resources**: each horizontal edge has its fixed two-column pair, each vertical edge its fixed singleton column. Label these \(t\) horizontal slots and \(t\) vertical slots. The row allocation is an assignment of all \(3t\) distinct row labels to \(t\) labeled singleton slots and \(t\) labeled unordered double slots. A two-edge exchange involving one horizontal and one vertical edge can swap the row from any horizontal singleton slot with either row from any vertical double slot, leaving all columns unchanged. Every such swap is legal because it merely repartitions the same three row labels and does not disturb any other coordinate resource. If the positions within each double slot are temporarily distinguished, these are exactly the transpositions across the edges of \(K_{t,2t}\), a connected graph. Edge transpositions of a connected graph generate the full symmetric group. Hence all row allocations are connected with column resources fixed. The same argument, with rows and columns interchanged, shows that all column allocations are connected with row resources fixed.

Given \(M,N\in\mathcal F_t\), apply row-only exchanges to make the row singleton and pair resources agree with \(N\), assigning the fixed column resources of \(M\) arbitrarily to the desired row slots. Then apply column-only exchanges to make every horizontal column pair and every vertical singleton column agree with \(N\). The final matching is \(N\), proving connectivity for all \(t\ge1\).

**6. Transitivity and a small exact diameter.** Any two saturated arrangements are equivalent under independent permutations of the \(3t\) row labels and of the \(3t\) column labels. These automorphisms preserve the two-edge exchange rule, so \(\mathcal R_t\) is vertex-transitive. The exhaustive code below verifies that for \(t=2\), one vertex has distance-sphere populations \((1,42,705,4904,2448)\). Their sum is 8100, and the largest distance is four. Vertex-transitivity therefore gives diameter four for the entire 8100-vertex graph. This finite metric statement is computer verified; connectivity for all sizes is established by the preceding proof.

## Verification

Two standalone dependency-free Python 3 scripts are provided as `direct_verify.py` and `structural_verify.py`. Run them from a directory containing both files with `python3 direct_verify.py` and `python3 structural_verify.py`. Captured outputs appear in `direct_output.txt` and `structural_output.txt`.

The direct verifier constructs the original rook-graph edge set and checks the induced-matching condition pairwise on edge endpoints. It enumerates all maximum-size candidates, rejects larger candidates, builds two-edge exchanges from original graph edges, and checks graph connectivity and distance layers for \(n=3,6\). The structural verifier independently generates all saturated arrangements from coordinate-slot permutations, verifies inducedness, constructs exchange neighbors from freed coordinates and checks the predicted valency and connectivity for \(n=3,6\). Both reproduce 9 states of degree 8 at \(n=3\), and 8100 states of degree 42 at \(n=6\); all 8100 are connected.

Finite enumeration checks the implementation and the small cases, not the all-size theorem. The unrestricted proof uses only the resource inequalities, elementary slot counting, and the connected-transposition lemma proved above.

## Relationship to prior work

The classical induced matching (also called *strong matching* or *2-edge packing*) and its general extremal enumeration are well established [1,2]. In particular, an earlier exact rook-graph induced-matching packing enumeration already determines the maximum size and configuration count used in this article; these scalar facts are **prior coverage** rather than novelty. The new statement concerns the precise exchange threshold: all optima are frozen under one-edge replacement, while the two-edge graph is connected, regular of explicitly given degree, and vertex-transitive.

Brešar, Dravec, Hedžet, and Samadi [3] study induced matching bounds and edge open packing in graph products; their Cartesian-product section establishes lower bounds for related scalar invariants, not exchange connectivity of these saturated rook-graph optima. Eto, Ito, Kobayashi, Otachi, and Wasa [4] study reconfiguration of vertex sets inducing regular subgraphs, including induced matchings, by moving one *vertex* at a time; that is a different transition operation from simultaneously exchanging two entire matching edges. The 2013 maximal-induced-matching enumeration [1] focuses on triangle-free graphs, whereas rook graphs for \(n\ge3\) contain triangles. No covering two-edge-exchange classification was identified in the inspected sources.

## Limitations

The theorem concerns square rook graphs of side divisible by three; other side lengths and rectangular cases are not classified. The exact two-edge diameter for arbitrary \(t\) is not established. The state-count formula is known from a previous packing enumerator; it is included solely to specify the connected reconfiguration graph. Historical priority beyond indexed and inspected accessible sources cannot be guaranteed. No independent scholarly audit has been performed.

## References

[1] M. Basavaraju, P. Heggernes, P. van 't Hof, R. Saei, Y. Villanger, *Maximal induced matchings in triangle-free graphs*, initial public arXiv posting 2013-12-18, https://arxiv.org/abs/1312.5180.

[2] W. Duckworth, D. Manlove, M. Zito, *On the approximability of the maximum induced matching problem*, J. Discrete Algorithms 3 (2005), 79–91, https://doi.org/10.1016/j.jda.2004.05.001.

[3] B. Brešar, T. Dravec, J. Hedžet, B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, initially public 2024-06-06, https://arxiv.org/html/2406.04020v2.

[4] H. Eto, T. Ito, Y. Kobayashi, Y. Otachi, K. Wasa, *Reconfiguration of Regular Induced Subgraphs*, initially public 2021-11-26, https://arxiv.org/html/2111.13476v2.
