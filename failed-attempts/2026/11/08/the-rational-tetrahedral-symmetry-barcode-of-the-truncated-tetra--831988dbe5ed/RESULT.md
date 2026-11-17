# The rational tetrahedral symmetry barcode of the truncated-tetrahedral graph

## Finding
Let \(T\) be the truncated-tetrahedral graph, with its intrinsic shortest-path metric. For \(r\ge0\), let \(K_r=\operatorname{VR}_{\le r}(V(T))\) be the inclusive simplicial Vietoris–Rips complex. The natural full automorphism group \(G\cong S_4\) acts on this entire filtration.

The **complete positive-degree rational persistent homology, as a filtration of \(G\)-representations**, has just two nonzero intervals:

\[
\widetilde H_1(K_r;\mathbb Q)\cong
\begin{cases}
\operatorname{sgn}\otimes V_{\mathrm{std}},&1\le r<2,\\
0,&\text{otherwise},
\end{cases}
\qquad
\widetilde H_2(K_r;\mathbb Q)\cong
\begin{cases}
\mathbb Q[\{0,1,2,3\}]\oplus\operatorname{sgn},&2\le r<3,\\
0,&\text{otherwise},
\end{cases}
\]
where \(V_{\mathrm{std}}=\ker(\mathbb Q^4\xrightarrow{\sum}\mathbb Q)\), \(\mathbb Q[\{0,1,2,3\}]\) is the natural four-label permutation module, and \(\operatorname{sgn}\) is the sign line. All other positive-degree rational groups vanish. Maps within each nonzero interval are identities under the canonical identification of the unchanged complex; maps between different intervals are zero. No assertion about the reduced degree-zero representation is made.

For a tetrahedral-label permutation \(g\in S_4\), let \(f(g)\) be its number of fixed labels and \(\varepsilon(g)\) its sign. The two nontrivial characters are exactly
\[
\operatorname{tr}(g\mid\widetilde H_1(K_1;\mathbb Q))=\varepsilon(g)(f(g)-1),
\qquad
\operatorname{tr}(g\mid\widetilde H_2(K_2;\mathbb Q))=f(g)+\varepsilon(g).
\]
In particular, the five degree-two generators contain one invariant line and one sign line, together with a three-dimensional standard constituent. These are representations **over \(\mathbb Q\)**, not claimed to be integral module splittings or equivariant homotopy splittings.

## Assumptions and scope
The graph has exactly twelve vertices \((i,j)\) with \(i,j\in\{0,1,2,3\}\), \(i\ne j\), and distinct vertices are adjacent if their first coordinates agree, or if they form the reversed pair \((i,j),(j,i)\). Every one of the six unordered original-label pairs contributes a reversing edge, and the three vertices with a given first coordinate form a triangle. The graph has eighteen edges, is connected, and has diameter three. Distance means the number of graph edges in a shortest path, not Euclidean distance in an embedding.

Every \(g\in S_4\) acts on vertices by \(g(i,j)=(g(i),g(j))\), preserving graph distances and all complexes \(K_r\). The four truncation triangles are the only triangles of the original graph, so any automorphism permutes them, and their six uniquely attached reversing edges force the action on the twelve vertices. Therefore this identifies the entire graph automorphism group, rather than a specified subgroup.

## Proof
**Finite chain dimensions and ranks.** Enumerating all nonempty subsets of the twelve vertices and retaining exactly those whose pairwise distances are at most the threshold gives, in dimensions zero upward,
\[
(f_0,f_1,f_2)(K_1)=(12,18,4),\qquad
(f_0,f_1,f_2,f_3)(K_2)=(12,42,48,12).
\]
All higher face numbers vanish. For \(K_1\), the four triangles have disjoint edge supports; the oriented second boundary has rank four. Its connected one-skeleton has first boundary rank eleven, so the rational first homology has rank \(18-11-4=3\), while higher homology vanishes. For \(K_2\), the three nonzero oriented boundary ranks are \(11,31,12\), and hence \(\dim_{\mathbb Q}\widetilde H_1=42-11-31=0\), \(\dim_{\mathbb Q}\widetilde H_2=48-31-12=5\), and \(\widetilde H_3=0\). The isolated-point and full-simplex regimes settle the remaining thresholds.

These ranks have a short exact certificate rather than requiring a floating-point computation: the included program constructs each integral oriented boundary. Reducing its columns over \(\mathbb F_2\) finds respectively \(11,4\) independent columns for \(K_1\) and \(11,31,12\) for \(K_2\). Since every nonzero minor modulo two remains nonzero over \(\mathbb Q\), these are rational lower bounds. The upper bounds are exact: \(\operatorname{rank}\partial_1\le11\) for a connected twelve-vertex complex; \(\operatorname{rank}\partial_2(K_1)\le4\); \(\operatorname{rank}\partial_2(K_2)\le42-11=31\) by \(\partial_1\partial_2=0\); and \(\operatorname{rank}\partial_3(K_2)\le12\). Thus all the stated rational ranks follow mathematically from the finite certificate.

**Signed simplicial action.** Each label permutation \(g\) gives an actual simplicial vertex permutation on both complexes. On a positively ordered face \(\sigma=(v_0,\ldots,v_d)\), the induced oriented chain map sends \(\sigma\) to the image with sign equal to the parity of the permutation required to sort \((g(v_0),\ldots,g(v_d))\). Consequently the alternating chain trace (Lefschetz number) is exactly
\[
L_r(g)=\sum_{d\ge0}(-1)^d\sum_{\substack{\sigma\in K_r,\ |\sigma|=d+1\\g\sigma=\sigma}}
\operatorname{sgn}(g\vert_\sigma).
\]
There are five conjugacy classes in \(S_4\), with cycle types \((1,1,1,1)\), \((2,1,1)\), \((2,2)\), \((3,1)\), and \((4)\), of sizes \(1,6,3,8,6\). Direct signed-face enumeration gives \(L_1(g)=(-2,2,2,1,0)\) and \(L_2(g)=(6,2,2,3,0)\) in that order. The companion verifier checks all twenty-four permutations individually, not just one representative per class.

Since both complexes are connected and have only the rational positive homology groups already identified, the Lefschetz formula yields \(\chi_{H_1}(g)=1-L_1(g)=(3,-1,-1,0,1)\) and \(\chi_{H_2}(g)=L_2(g)-1=(5,1,1,2,-1)\). The character of \(V_{\mathrm{std}}\) is \(f(g)-1\), and the character of the four-label permutation module is \(f(g)\). Multiplying by \(\varepsilon(g)\) or adding the sign character gives precisely the two preceding character vectors. Character equality determines rational representations of a finite group (Maschke semisimplicity), proving the decompositions.

**Filtration maps.** Because the graph diameter is three, \(K_r\) is a discrete set for \(0\le r<1\), equals \(K_1\) for \(1\le r<2\), equals \(K_2\) for \(2\le r<3\), and is the full eleven-simplex for \(r\ge3\). The only nonzero positive rational groups occupy distinct degrees at adjacent thresholds, so the maps between them vanish. Within an interval the inclusions are literally identity maps of complexes. This proves the full stated positive-degree persistence representation, not merely the characters of two isolated complexes.

## Verification
`verify.py` independently regenerates graph adjacency, all shortest paths, every face out of the \(2^{12}-1\) possible nonempty subsets, each binary boundary-rank witness and all twenty-four label permutations. It asserts degree three, eighteen edges, diameter three, the two face vectors, the five boundary ranks, class sizes, signed chain action and both closed character formulas. Run `python3 verify.py` with Python 3 (standard library only); the exact previously obtained output is `verify_output.txt`.

A separate exact-rational SymPy matrix calculation, not needed by the verifier, independently reproduced the ranks \((11,4)\) and \((11,31,12)\). The mod-two witness method in the standalone verifier is already sufficient for the rational-rank proof because it is combined with the boundary-composition upper bounds above.

## Relationship to prior work
Saleh, Titz Mite and Witzel's study of Vietoris–Rips complexes of Platonic solids (first public version 2023-02-28) explicitly suggests extending the program to Archimedean solids, and discusses difficulty preserving symmetry during Morse collapses. Their objects are Platonic vertex sets, and their theorem does not compute either of the present representations. A publicly available graph-metric computation for the truncated tetrahedron already determines its nonequivariant sphere-wedge filtration, including \(\bigvee^3S^1\) and \(\bigvee^5S^2\); **those homotopy types are prior work and are not claimed as new here**. Its proof does not compute the full automorphism action on homology. Adams, Lagoda, Moy, Sadovek and De Saha study persistent Borel equivariant cohomology for the circle action on metric thickenings of the circle, a different object, group and invariant. The new contribution here is the explicit complete rational \(S_4\)-representation-valued positive-degree barcode of the Archimedean graph metric.

## Limitations
All new representation identifications are rational. In particular, a rational isomorphism to a permutation-plus-sign module need not lift to an integral lattice isomorphism. The result does not compute Borel equivariant cohomology, an integral equivariant persistence module, a canonical equivariant wedge decomposition, or a classification of other Archimedean solids. Literature searching cannot rule out an unindexed equivalent character computation. The finite calculations are exhaustive for this one twelve-vertex graph, not evidence for an unproved infinite family.

## References
1. N. Saleh, T. Titz Mite, S. Witzel, “Vietoris–Rips complexes of Platonic solids,” arXiv:2302.14388, first public version 2023-02-28. https://arxiv.org/abs/2302.14388
2. “The graph-metric Rips filtration of the truncated tetrahedron,” public research note, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-graph-metric-rips-filtration-of-the-truncated-tetrahedron--51e8cc219376 (used solely for comparison with its nonequivariant homotopy statement).
3. H. Adams, E. Lagoda, M. Moy, N. Sadovek, A. De Saha, “Persistent equivariant cohomology,” arXiv:2408.17331, first public version 2024-08-30. https://arxiv.org/html/2408.17331v1
