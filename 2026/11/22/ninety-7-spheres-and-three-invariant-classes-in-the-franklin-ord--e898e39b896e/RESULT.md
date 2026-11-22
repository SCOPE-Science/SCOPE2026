# Ninety \(7\)-spheres and three invariant classes in the Franklin ordinary four-cut complex

## Finding
Let \(F\) be the standard twelve-vertex Franklin graph with vertex set \(\mathbb Z/12\mathbb Z\), all cycle edges \(\{i,i+1\}\), and six chords \(\{2j,2j+5\}\), with indices modulo twelve. Define its **ordinary four-cut complex** \(X=\Delta_4(F)\) to have facets equal to the complements of four-vertex subsets inducing *disconnected* subgraphs. Let \(K=X^\vee\) be its combinatorial Alexander dual. Then there are integral homotopy equivalences
\[
K\simeq\bigvee^{90} S^2,\qquad X\simeq\bigvee^{90}S^7.
\]
Furthermore \(X\) is pure of dimension seven and the full graph automorphism group has order \(48\). Its action on \(\widetilde H_7(X;\mathbb Q)\) has a **three-dimensional invariant subspace**. The complete rational character, organized by conjugacy class, is:

| Class size | Vertex cycle type | Trace on \(\widetilde H_7(X;\mathbb Q)\) |
| ---: | --- | ---: |
| 1 | \(1^{12}\) | 90 |
| 3 | \(2^2 1^8\) | 10 |
| 3 | \(2^4 1^4\) | -6 |
| 6 | \(2^6\) | -2 |
| 1 | \(2^6\) | 2 |
| 6 | \(2^6\) | 2 |
| 8 | \(3^4\) | 3 |
| 6 | \(4^2 2^2\) | 2 |
| 6 | \(4^2 2^2\) | 2 |
| 8 | \(6^2\) | -1 |

The ten class sizes sum to \(48\); their size-weighted traces sum to \(144\), giving invariant dimension \(144/48=3\). The table is rational equivariant information, not an integral module decomposition or an equivariant sphere-wedge splitting.

## Assumptions and scope
All graphs are finite, simple, and undirected. The Franklin graph presentation is the canonical Hamiltonian LCF presentation \([5,-5]^6\). A face of \(X\) is any subset of a facet described above. The Alexander dual is
\[
K=\{W\subseteq V(F):\text{every four-subset of }W\text{ induces a connected subgraph of }F\}.
\]
The condition on a set with fewer than four vertices is vacuous. This is **not** the total four-cut complex obtained using only independent four-sets. We use reduced integral homology unless otherwise noted, and the standard unreduced geometric realization of a nonempty simplicial complex.

## Proof
**1. Connected quadruples and the exact dual.** The graph has twelve vertices, degree three at every vertex, is bipartite, and has precisely three four-cycles, with vertex sets \(\{0,5,6,11\}\), \(\{1,2,7,8\}\), and \(\{3,4,9,10\}\). These squares are pairwise disjoint. In a triangle-free cubic graph a connected induced four-set is one of a claw, an induced four-vertex path, or a four-cycle. There are twelve induced claws, one centered at each vertex. There are \(12\cdot3\cdot2\cdot2/2=72\) unoriented nonbacktracking paths of length three, of which four per four-cycle close to a square. Thus there are \(72-4\cdot3=60\) induced four-vertex paths and three induced squares, giving \(12+60+3=75\) connected four-sets. Among all \(\binom{12}{4}=495\) quadruples, exactly \(420\) are disconnected.

A five-vertex face of \(K\) would induce a graph remaining connected after deletion of any vertex. It would therefore be two-vertex-connected and, since it is bipartite with five vertices and maximum degree three, contain a \(K_{2,3}\). In fact, a two-connected bipartite graph on five vertices is exactly \(K_{2,3}\). Such a graph has multiple four-cycles sharing vertices, impossible because the three four-cycles of \(F\) are vertex-disjoint. Hence \(K\) has no five-vertex faces and no larger faces. Its entire face set is the complete two-skeleton on twelve vertices together with the \(75\) connected-four-set tetrahedra. Its nonempty face vector by dimension is \((12,66,220,75)\).

**2. A finite elementary-collapse certificate.** All \(75\) tetrahedra can be removed by \(75\) elementary collapses, each pairing a tetrahedron with a triangular free face. The finite proof uses a deterministic, reproducible algorithm. At any stage, list all triangular faces of the remaining tetrahedra having exactly one remaining tetrahedral coface; choose the lexicographically smallest pair \((T,\tau)\) of (tetrahedron bitmask, triangle bitmask); delete both faces, and repeat. In this graph the list never becomes empty before the last tetrahedron. The attached standard-library verifier constructs every face from the defining graph, checks the selected triangle is genuinely free in the *entire remaining simplicial complex*, and checks that all \(75\) operations succeed. This is an exhaustive finite certificate, not a sample of possible collapses.

After these collapses the dual is a two-dimensional complex \(K'\) with twelve vertices, \(66\) edges and \(145\) triangles, and no higher-dimensional faces. The original \(K\) contains the full two-skeleton of the eleven-simplex and is simply connected; elementary collapses preserve its homotopy type. The reduced Euler characteristic of \(K'\) is \(12-66+145-1=90\). Since a simply connected two-dimensional finite CW complex has free integral second homology of rank its reduced Euler characteristic and is homotopy equivalent to a wedge of that many two-spheres (Hurewicz, followed by homological Whitehead), \(K\simeq\bigvee^{90}S^2\).

**3. Integral duality and the original complex.** Combinatorial Alexander duality on the twelve graph vertices gives
\[
\widetilde H_i(X;\mathbb Z)\cong\widetilde H^{9-i}(K;\mathbb Z).
\]
Consequently \(\widetilde H_7(X;\mathbb Z)\cong\mathbb Z^{90}\), and all other reduced homology groups vanish. The complete enumeration of \(X\)'s faces gives the dimension-wise vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)=(12,66,220,495,792,924,792,420).
\]
Thus \(X\) contains the entire six-skeleton of the eleven-simplex and is five-connected. Its vanishing sixth homology forces its sixth homotopy group to vanish by the Hurewicz theorem; hence \(X\) is six-connected. Choosing \(90\) spherical maps representing a basis of the integral seventh homology yields a homology equivalence from \(\bigvee^{90}S^7\) to \(X\); the simply connected homological Whitehead theorem upgrades it to a homotopy equivalence. All \(420\) facets have eight vertices, proving purity and dimension seven.

**4. The rational symmetry character.** The verifier enumerates all \(48\) graph automorphisms by exact adjacency-preserving backtracking, and all \(2^{12}\) candidate vertex subsets for \(X\). If \(g\) fixes a simplex \(\sigma\) setwise, its signed chain trace contribution is the orientation sign \(\varepsilon(g,\sigma)\). Because \(X\)'s reduced rational homology is confined to odd degree seven, the Hopf trace formula gives
\[
\operatorname{tr}\!\left(g\mid\widetilde H_7(X;\mathbb Q)\right)
=1-\sum_{j=0}^{7}(-1)^j\!\sum_{\substack{\sigma\in X,\,|\sigma|=j+1\\g\sigma=\sigma}}\varepsilon(g,\sigma).
\]
Every signed face is enumerated exactly. The code also computes the dual trace independently and checks consistency with the vertex-permutation orientation twist in Alexander duality; all \(48\) automorphisms are even on the twelve vertices. It checks the ten conjugacy classes and the displayed character, including the size-weighted average of three invariant dimensions. This character calculation requires no equivariant homotopy equivalence.

## Verification
Run `python verify_franklin_fourcut.py` from an extracted copy of this package. It uses only the Python standard library and regenerates both face posets, the three squares, all \(75\) elementary collapse pairs, the complete automorphism group, and signed chain traces. It checks Alexander-dual membership for all \(4096\) subsets and the complete face vectors, not just mod-two Betti numbers. `verification_output.txt` is the recorded run output, ending in `ALL EXACT TESTS PASSED`. The mathematical topology argument above states exactly how these finite checks imply the integral homotopy claims. No computational evidence for infinite graph families is asserted.

## Relationship to prior work
The ordinary cut construction and its basic graph operations were introduced by Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue, *Topology of Cut Complexes of Graphs* (arXiv:2304.13675; first public version April 26, 2023). Their sequel *Topology of Cut complexes II* (arXiv:2407.08158; July 11, 2024) addresses disjoint unions, squared paths, grids, and certain homology representations, not the Franklin computation.

The same graph's previously published **total** four-cut complex has homotopy type \(\bigvee^{43}S^4\) and no invariant rational homology under its full automorphism group (*The Franklin total four-cut complex: 43 four-spheres and its symmetry character*, public published-finding corpus record dated November 8, 2026). Total four-cuts use **independent** quadruples, whereas ordinary four-cuts use **all disconnected** quadruples; the earlier result does not imply the ninety-copy seven-sphere statement, nor the three invariant classes. A previously published all-graph ordinary four-cut sphere-wedge theorem assumes girth at least five; Franklin has three four-cycles, so that theorem's hypotheses are false. The original foundational cut-complex paper and the closely related total-cut paper were inspected in full-text HTML. The published Franklin total-cut RESULT and high-girth RESULT were materially compared at their theorem and proof levels. No previously published covering claim was found in the stated sources and targeted database searches, but undiscovered equivalent computations remain possible.

## Limitations
The classification is for exactly this named graph and this cut parameter; no theorem for all cubic graphs or arbitrary short-cycle configurations is claimed. The 75-pair collapse is a complete finite computer-checkable proof, not a symbolic formula for a parameter family. The rational character is not an integral representation decomposition; the sphere-wedge equivalences are not asserted to be automorphism-equivariant. No claim is made about shellability, persistent maps between distinct cut parameters, or uniqueness against unindexed literature.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503 (first posted September 27, 2022), https://arxiv.org/abs/2209.13503.
2. The same authors, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first posted April 26, 2023), https://arxiv.org/abs/2304.13675.
3. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, and L. Xue, *Topology of Cut complexes II*, arXiv:2407.08158 (first posted July 11, 2024), https://arxiv.org/abs/2407.08158.
4. *The Franklin total four-cut complex: 43 four-spheres and its symmetry character*, publicly available theorem, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-franklin-total-four-cut-complex-43-four-spheres-and-its-symm--cb1ddb15f1e3.
5. *Homotopy classification of four-cut complexes at the pentagonal girth boundary*, publicly available theorem, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-homotopy-classification-of-four-cut-complexes-at-the-pentagonal--94b36fd5471f.
6. E. W. Weisstein, *Franklin Graph*, MathWorld, https://mathworld.wolfram.com/FranklinGraph.html.
