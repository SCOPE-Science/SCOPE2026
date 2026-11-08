# Geodesics and spanning trees in three-colour Bell graphs of complete bipartite graphs

## Finding
Let \(m,n\ge3\) be integers. The Bell graph \(\mathcal B_3(K_{m,n})\) of unlabelled proper colour partitions with at most three classes is the one-vertex union
\[
\mathcal B_3(K_{m,n})\cong P_m\vee_o P_n,
\qquad P_s:=Q_s/(x\sim\overline x),
\]
where \(P_s\) is the simple antipodal quotient of the binary \(s\)-cube, and \(o\) is the orbit of the all-zero word. In particular, the number of vertices is \(2^{m-1}+2^{n-1}-1\). The sole cut vertex is the ordinary two-class bipartition, whose deletion leaves exactly two components. Thus the graph is connected and non-Hamiltonian. Its diameter is
\[
\operatorname{diam}\mathcal B_3(K_{m,n})=\lfloor m/2\rfloor+\lfloor n/2\rfloor.
\]

Here are exact geodesic and spanning-tree counts. In the factor \(P_s\), choose any binary representatives \(x,y\in\{0,1\}^s\), put \(h=\operatorname{Ham}(x,y)\) and \(d=\min(h,s-h)\). Then
\[
\operatorname{dist}([x],[y])=d,\qquad
N_{\rm geo}([x],[y])=\begin{cases}2d!,&2h=s,\\d!,&2h\ne s.\end{cases}
\]
If \(u\) is in the first factor off the shared vertex and \(v\) is in the second off it, the distance is \(\operatorname{dist}(u,o)+\operatorname{dist}(o,v)\), and the number of geodesics is the product of their counts to \(o\). The formula within one factor also applies at the shared vertex. The total number of spanning trees is
\[
\tau(\mathcal B_3(K_{m,n}))=T_mT_n,\qquad
T_s=\frac{1}{2^{s-1}}\prod_{\substack{2\le j\le s\\j\text{ even}}}(2j)^{\binom{s}{j}}.
\]
For example \(\mathcal B_3(K_{3,3})\) is two copies of \(K_4\) meeting at a vertex: it has seven vertices, twelve edges, diameter two, and 256 spanning trees.

## Assumptions and scope
Graphs are finite and simple; the two partite sets of \(K_{m,n}\) are individually labelled and nonempty. A Bell three-colouring is a partition of the vertex set into **at most three nonempty** independent blocks; colour names are discarded. Two different partitions \(A,B\) are adjacent precisely if there is a base-graph vertex \(v\) such that their restrictions to the vertex set without \(v\) coincide as unlabelled partitions. Each reconfiguration edge is simple even when multiple vertices witness it. The antipodal quotient identifies each binary word with its bitwise complement, and has one simple edge for each pair of distinct orbits having adjacent cube representatives. The lower bounds \(m,n\ge3\) are essential to the simple quotient's degree and the 2-connectivity argument.

## Proof
**Partition reduction.** Write the bipartition of \(K_{m,n}\) as \(U\sqcup W\), with sizes \(m,n\). Every independent colour block is contained entirely within one of these two sides, as each cross pair is adjacent. Since at most three nonempty blocks are allowed and each side needs at least one, the only possibilities for numbers of blocks in the two sides are \((1,1)\), \((2,1)\), and \((1,2)\). There is exactly one \((1,1)\) partition, denoted \(o\). A partition of type \((2,1)\) is a bipartition of \(U\) into two unnamed blocks with the whole of \(W\) as the third block; complementing the associated length-\(m\) binary indicator has no effect. Including \(o\), this gives precisely the orbit set \(\{0,1\}^m/(x\sim\bar x)\). The other branch similarly gives the length-\(n\) orbit set.

**Exact adjacency.** Within one branch, deleting a particular vertex and comparing restricted partitions has exactly the effect of flipping that one vertex's binary bit, modulo global complementation. Thus the branch including \(o\) is the simple cube quotient \(P_m\) or \(P_n\). A non-root partition of type \((2,1)\) cannot be adjacent to a non-root partition of type \((1,2)\): if the deleted vertex lies in \(U\), then the induced partitions of untouched \(W\) differ (one versus two blocks), and if it lies in \(W\), the induced partitions of untouched \(U\) differ. Therefore there are no branch-crossing edges. This proves the one-vertex union and order formula.

**Connectivity and cut vertex.** Fix the final bit of any length-\(s\) representative to zero to identify \(V(P_s)\) with \(\{0,1\}^{s-1}\). The quotient contains all ordinary edges of \(Q_{s-1}\), plus the antipodal matching in \(Q_{s-1}\). For \(s\ge3\), the spanning \(Q_{s-1}\) is 2-vertex-connected; adding edges preserves this property. Hence neither factor has a cut vertex, whereas their common \(o\) is a cut vertex, and indeed the only one. As there are two nontrivial factors, a Hamilton cycle cannot exist.

**Exact shortest routes.** An orbit walk of length \(\ell\) in \(P_s\) lifts uniquely after fixing its initial cube vertex to a cube walk of length \(\ell\), ending at either \(y\) or its complement. The two possible Hamming distances are \(h\) and \(s-h\). The minimum is \(d=\min(h,s-h)\). Any shortest cube walk to its endpoint changes exactly the differing coordinates in any order, so there are \(d!\) such walks. Both endpoint lifts achieve distance \(d\) exactly when \(2h=s\), producing two disjoint batches; otherwise only one lift does. The covering map is locally bijective for \(s\ge3\), so these correspond to distinct quotient paths. For endpoints in distinct factors all paths pass through \(o\), and a shortest path is necessarily the concatenation of a shortest path to \(o\) and a shortest path away from it. Their counts therefore multiply. Every factor has radius and diameter \(\lfloor s/2\rfloor\) (this follows directly from the orbit-distance formula); choosing an orbit at maximal distance from \(o\) in each factor yields the diameter of their vertex union as the sum of those radii.

**Exact spanning trees.** Each spanning tree of a one-vertex union restricts to a spanning tree in each factor, and conversely any two such factor trees meet at \(o\) to form a spanning tree. Hence the tree numbers multiply. For a factor \(P_s\), cube characters indexed by \(A\subseteq\{1,\dots,s\}\) descend to the antipodal quotient exactly when \(\lvert A\rvert\) is even. The cube Laplacian has eigenvalue \(2\lvert A\rvert\) on this character. Consequently the Laplacian spectrum of \(P_s\) consists of \(2j\) with multiplicity \(\binom{s}{j}\) for all even \(j\in\{0,\dots,s\}\); in particular the zero eigenvalue is simple. The matrix-tree theorem divides the product of nonzero Laplacian eigenvalues by the vertex count \(2^{s-1}\), yielding \(T_s\) exactly. This proves every displayed formula for all \(m,n\ge3\).

## Verification
The self-contained Python standard-library script `artifacts/verify.py` independently enumerates unlabelled set partitions, tests Bell adjacency by deleting each base vertex, constructs the proposed cube quotients, and compares complete edge sets. It also checks all-pairs distances and shortest-path counts by breadth-first search against the formulas for \((m,n)\in\{(3,3),(3,4),(4,4),(3,5),(4,5)\}\). An independent exact-integer Bareiss determinant of the reduced Laplacian checks spanning-tree counts for all tested graphs up to sixteen vertices, and similarly for \(P_3,P_4,P_5\). It checks the product formula for \(P_6\) algebraically. The script terminates with `VERIFY_OK`. These finite checks test the definitions and critical examples; the unrestricted theorem follows from the proof, not from extrapolation.

## Relationship to prior work
Asgarli, Krehbiel and MacLean (2025, Section 5, Example 5.5) prove that the Bell two-colour graph of an edgeless \(s\)-vertex graph is a cube with antipodal edges and apply it to stars. That one-factor identification is prior work, not claimed as new. The present result identifies how **two** such factors glue for genuine complete bipartite bases with both sides at least three, and determines all cross-branch geodesics and an exact spanning-tree census. Celaya, Choo, MacGillivray and Seyffarth (2016) study *named* recolouring graphs of complete bipartite graphs, finding Hamiltonian three-colour graphs when both side sizes are odd; the *unlabelled* Bell graphs here are non-Hamiltonian in that same range. Haas and MacGillivray (2018) prove cut-vertex and Hamilton-path results for **canonical** colouring graphs, which are ordering-dependent spanning subgraphs of the Bell graph and do not by themselves determine its extra edges, shortest routes, or spanning trees. Bard (2014) studies named k-colour reconfiguration graphs of complete multipartite graphs; this does not cover unlabelled Bell graphs. Finbow and MacGillivray (2025/2026) prove Bell graph Hamiltonicity for trees and for sufficiently large palettes but do not assert the three-colour complete-bipartite formulas. An earlier result on Bell colour graphs of edgeless graphs gives edit distances by block matching; the present complete-bipartite structure and route counts are distinct.

## Limitations
This is a theorem for the **simple** Bell three-colouring graph of labelled \(K_{m,n}\) with \(m,n\ge3\); it does not address parallel-edge multiplicities, one- or two-vertex sides, higher palettes, or arbitrary bipartite host graphs. The all-pairs geodesic formula counts distinct graph-theoretic shortest paths, not labelled vertex-move histories. The proof is self-contained but historical priority is provisional; exhaustive literature coverage and independent mathematical audit have not been established.

## References
1. S. Asgarli, S. Krehbiel, S. MacLean, *Bell coloring graphs: realizability and reconstruction*, arXiv:2512.10177v1, first posted 2025-12-11; especially Example 5.5 and Section 5. URL: https://arxiv.org/abs/2512.10177
2. M. Celaya, K. Choo, G. MacGillivray, K. Seyffarth, *Reconfiguring k-colourings of Complete Bipartite Graphs*, Kyungpook Math. J. 56 (2016), 647–655, DOI 10.5666/KMJ.2016.56.3.647; especially Theorem 2.1. URL: https://doi.org/10.5666/KMJ.2016.56.3.647
3. R. Haas and G. MacGillivray, *Connectivity and Hamiltonicity of Canonical Colouring Graphs of Bipartite and Complete Multipartite Graphs*, Algorithms 11 (2018), 40, DOI 10.3390/a11040040; especially Proposition 4. URL: https://www.mdpi.com/1999-4893/11/4/40
4. S. Finbow and G. MacGillivray, *Hamiltonicity of Bell and Stirling colour graphs*, arXiv:2512.13864v1 (2025); Utilitas Mathematica 127 (2026), 239–258. URL: https://combinatorialpress.com/um-articles/vol-127/hamiltonicity-of-bell-and-stirling-colour-graphs/
5. S. Bard, *Gray code numbers of complete multipartite graphs*, MSc thesis, University of Victoria (2014), especially Chapters 3 and 5 on named colour-reconfiguration graphs. URL: https://dspace.library.uvic.ca/bitstreams/f39cda59-feac-478d-87b0-381f010c58e8/download
