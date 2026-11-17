# Four torus components in the pentagon Hom complex of the nine-point Paley graph

## Finding
Let \(R=K_3\mathbin{\square}K_3\) be the nine-vertex rook graph (equivalently the Paley graph of order nine, \(H(2,3)\)). Regard the source \(C_5\) as the simple five-cycle with vertices indexed cyclically. Its **ordinary polyhedral graph-homomorphism complex** has the integral homotopy classification
\[
\operatorname{Hom}(C_5,R)\simeq \bigsqcup_{j=1}^{4}(S^1\times S^1).
\]
More strongly, the original product-of-simplices cell complex has an explicit finite sequence of elementary collapses to a disjoint union of four closed, orientable polyhedral surfaces of genus one. Consequently,
\[
\widetilde H_0\cong\mathbb Z^3,\qquad
H_1\cong\mathbb Z^8,\qquad H_2\cong\mathbb Z^4,
\]
and every higher integral homology group vanishes.

## Assumptions and scope
The graph \(R\) has vertex set \(\{0,1,\ldots,8\}\), with \(a\sim b\) exactly when \(a\ne b\) and either \(\lfloor a/3\rfloor=\lfloor b/3\rfloor\) or \(a\bmod3=b\bmod3\). Thus this is the *Cartesian*, not categorical, product of two three-vertex complete graphs. A cell in \(\operatorname{Hom}(C_5,R)\) is a tuple \((A_0,\ldots,A_4)\) of nonempty subsets of \(V(R)\) such that every member of \(A_i\) is adjacent to every member of \(A_{i+1}\), with indices modulo five. Its dimension is \(\sum_{i=0}^{4}(|A_i|-1)\). All cellular statements refer to this finite regular polyhedral complex, not a clique complex or a simplicial replacement.

## Proof
**Complete finite cell determination.** Encode a nonempty subset of \(V(R)\) by the positive integer whose binary one-bits identify its elements, with the least significant bit representing vertex zero. Enumerating all nine-to-the-fifth possible vertex maps, retaining exactly the graph homomorphisms, gives 900 zero-cells. Extend each valid cell by adjoining one target vertex at one source position whenever both neighboring complete-bipartite constraints remain satisfied; repeat until saturation. This enumerates all cells because every product-of-simplices cell is built from any of its vertex maps by successive single-element inclusions. The resulting dimension counts are
\[
(f_0,f_1,f_2,f_3)=(900,2160,1440,180),
\]
with no cells above dimension three. An independently implemented enumeration by intersecting common-neighbor masks at successive source positions gives the identical set of all 4680 cells. The two algorithms are reproduced in `verify.py`.

**Certified elementary collapse.** Index cells at each dimension by lexicographic order of their five integer masks. For \(d=3,2,1\), considered in decreasing order, scan the surviving \((d-1)\)-cells in index order. Select the first one with exactly one surviving \(d\)-dimensional cofacet, provided that cofacet has no surviving \((d+1)\)-dimensional coface; delete the free face and its unique maximal cofacet and repeat. When no selection exists, stop. The code checks the full current face-incidence relation and maximality before *each* deletion. It performs 180 elementary \((3,2)\) collapses and 180 elementary \((2,1)\) collapses and terminates with a two-dimensional complex having global counts
\[
(900,1980,1080).
\]
Every deletion is an elementary collapse of a regular cell complex, so the residual complex is a strong deformation retract of the original complex.

**Surface classification.** The original one-skeleton has exactly four connected components, each on 225 vertices. Elementary collapses preserve components. The residual counts in *each* component are exactly
\[
(v,e,f)=(225,495,270).
\]
The certificate explicitly checks that every remaining edge lies in exactly two remaining 2-cells. At each of the 900 vertices, the link built from surviving incident edges and face corners is a single cycle (not a disjoint union of cycles); its length is four, five or six. Thus each residual component is a connected closed two-manifold. Its 2-cells can be coherently oriented with opposite induced signs along every shared edge, as verified by an integer \(\pm1\) propagation over the cellular boundary. Each component is therefore orientable. Its Euler characteristic is \(225-495+270=0\); the classification of closed connected orientable surfaces yields genus one. This proves the asserted four-torus homotopy type.

## Verification
Run `python3 verify.py` with the Python standard library. It independently reconstructs the full cell set by two finite enumerations, checks the signed boundary-squared identities, verifies all 360 free-face removals, computes components and Euler characteristics, checks every edge incidence and every vertex link, and propagates an integral coherent orientation across every surviving surface. The expected machine-readable output is `certificate.json`. The proof does not extrapolate from sampled finite cases: the stated object has exactly nine target vertices and five source vertices, and its full face poset is enumerated. Exhaustiveness follows from the algorithms and the independent set-equality assertion, not from unstated external data.

## Relationship to prior work
Fujii, Kimura and Nozaki (first public 2024-12-26) classify components of \(\operatorname{Hom}(G,H)\) for *square-free* target \(H\), and Matsushita independently establishes an analogous square-free classification. Their hypotheses do not include \(R\): for example, its four grid corners form a four-cycle. The reported torus components also cannot be instances of those square-free results, which for nonbipartite source \(C_5\) yield at most circles or points. Csorba and Lutz's graph-coloring-manifold study establishes manifold statements for complete target graphs \(K_n\), notably \(\operatorname{Hom}(C_5,K_4)\), not the nine-vertex Cartesian product \(K_3\square K_3\). The target is the unique nine-vertex strongly regular graph with parameters \((9,4,1,2)\), also known as the Paley nine graph, which motivates the example beyond an arbitrary finite graph.

## Limitations
The theorem concerns only \(\operatorname{Hom}(C_5,K_3\square K_3)\), not arbitrary Hamming graphs, other source cycles, or the categorical graph product. Although the collapse provides an integral homotopy classification, it does not determine the induced action of the full graph automorphism group on the individual torus fundamental groups or their homology lattices. An equivalent computation in unindexed older sources cannot be excluded; the bibliographic comparison is not a mathematical uniqueness theorem. No external independent audit has been performed.

## References
1. S. Fujii, K. Kimura, Y. Nozaki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are square-free*, first publicly posted December 26, 2024, https://arxiv.org/abs/2412.19039 .
2. T. Matsushita, *Hom complexes of graphs whose codomains are square-free*, first publicly posted December 26, 2024, https://arxiv.org/abs/2412.19144 .
3. P. Csorba, F. H. Lutz, *Graph Coloring Manifolds*, ZIB Report 06-11 (2006), https://webdoc.sub.gwdg.de/ebook/serien/ah/reports/ZIBreport/ZR-06-11.pdf .
4. *Paley graph P9*, DistanceRegular.org, https://www.math.mun.ca/distanceregular/graphs/paley9.html .
