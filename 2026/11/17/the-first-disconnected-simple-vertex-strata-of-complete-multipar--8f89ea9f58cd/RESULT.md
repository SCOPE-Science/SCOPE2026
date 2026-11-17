# The first disconnected simple-vertex strata of complete multipartite graphical zonotopes

## Finding
Let \(G=K_{a_1,\ldots,a_r}\) be a complete multipartite graph with at least three nonempty parts, and let \(n=\sum_{j=1}^r a_j\le7\). Form its graphical zonotope
\[
Z(G)=\sum_{\{i,j\}\in E(G)}[e_i,e_j]\subset\mathbb R^n.
\]
Let \(\mathcal S(G)\) be the induced subgraph of its one-skeleton on the *simple vertices*, namely vertices incident to precisely \(n-1\) zonotope edges.

**Theorem (sharp seven-vertex cutoff and two fragmentation types).** For every such graph on at most six vertices, \(\mathcal S(G)\) is connected. Among the eleven multipartite types on seven vertices with at least three parts, it is disconnected **only** for
\[
G=K_{3,3,1}\qquad\text{and}\qquad G=K_{3,2,2}.
\]
For \(K_{3,3,1}\), the zonotope has exactly 1,902 vertices, 860 of which are simple; its simple-vertex induced subgraph consists of **two connected components of 430 vertices each**. For \(K_{3,2,2}\), the zonotope has exactly 2,286 vertices, 1,240 of which are simple; its simple-vertex induced subgraph consists of **one component of 1,192 vertices and 48 isolated vertices**. These counts include labeled orientations without quotienting by graph automorphisms. All other cases in the stated range have a connected nonempty simple-vertex subgraph.

A concrete isolated simple vertex of the second zonotope arises from the total order \((5,0,6,1,3,2,4)\), with parts \(\{0,1,2\},\{3,4\},\{5,6\}\); its color sequence is \(C,A,C,A,B,A,B\). It has six reversible edges, and every one of those reversals leads to a nonsimple vertex.

## Assumptions and scope
The parameter domain is **all** unordered integer partitions \((a_1,\ldots,a_r)\) of \(n\) with \(3\le n\le7\) and \(r\ge3\). There are 25 such types in total, including the complete graphs \(K_n\) represented by \(n\) singleton parts. The Euclidean realization above is used only to identify the standard graphical zonotope and its one-skeleton; the claim is combinatorial and invariant under positive segment lengths that preserve the graphic arrangement fan.

Because \(G\) is connected, \(Z(G)\) has affine dimension \(n-1\). An *orientation mask* is one bit for each graph edge \(\{i,j\}\), \(i<j\), with bit one meaning \(i\to j\). Two masks differ by one bit if and only if precisely one directed graph edge is reversed. The adjective *simple* concerns the zonotope's vertex incidence degree, not simplicity of the whole zonotope. Nothing is asserted for graphs with fewer than three parts, or for \(n\ge8\).

## Proof
**1. Orientations and polytope edges.** For a generic linear functional \(u\), maximization over each segment \([e_i,e_j]\) selects one endpoint according to the sign of \(u_i-u_j\). Thus each zonotope vertex corresponds to a region of the graphic arrangement \(u_i=u_j\), or equivalently an acyclic orientation of \(G\). Conversely, every acyclic orientation has a topological order; assigning strictly increasing values along that order realizes its region. Adjacent full-dimensional arrangement chambers share a codimension-one wall belonging to exactly one graphic hyperplane, so their masks differ by one edge reversal. That reversal is a zonotope edge exactly when the new orientation is still acyclic. The degree of a zonotope vertex is therefore the number of one-bit flips that stay in the finite set of acyclic orientation masks. A vertex is simple precisely when this number equals \(n-1\).

**2. An independent structural degree formula.** Acyclic orientations of a complete multipartite graph have a unique word of consecutive nonempty monochromatic blocks, adjacent blocks bearing different colors. (An explicit ordered-block model also appears in Chapoton--Pilaud, Proposition 48.) Let the consecutive block sizes be \(s_1,\ldots,s_k\). Every edge across consecutive blocks is reversible: an alternative directed path would need an intermediate block, which does not exist. Every edge across nonconsecutive blocks is not reversible: because adjacent block colors differ and all different colors are adjacent in the graph, one may choose an intermediate block of a color distinct from the two endpoint colors; or, when the intervening block shares an endpoint color, use the next block to obtain a directed multi-edge path. More directly, the quotient reachability poset of all blocks is a chain, so every edge jumping over a block is transitively implied. Hence
\[
\deg=\sum_{j=1}^{k-1}s_js_{j+1}.
\]
Writing \(t_j=s_j-1\ge0\) gives the exact nonnegative identity
\[
\deg-(n-1)=\sum_{j=2}^{k-1}t_j+\sum_{j=1}^{k-1}t_jt_{j+1}.
\]
This provides a separate check that the minimum degree is \(n-1\), and that simplicity means all interior blocks are singletons and no adjacent pair of block sizes both exceeds one. These identities are not used to assume any of the finite component counts.

**3. Exhaustive finite algorithm.** The supplied standalone Python 3 source `verify_multipartite_simple_connectivity.py` is part of the proof certificate. Its `integer_partitions` recursively generates every unordered size partition, and filters to at least three parts. For each one, `orientation_masks_from_orders` loops through **every** \(n!\) permutation of vertices, orients every edge forward in that order, and collects the resulting distinct bit masks. Every generated mask is acyclic; every acyclic orientation is generated because a directed acyclic graph has a topological order. There is consequently no sampling or partial search in this step.

For each mask and each graph edge, the code computes whether flipping that edge produces a mask already in the exhaustive set. This gives *all* one-skeleton degrees, hence the exact set of simple vertices. An ordinary depth-first traversal restricted to these simple masks then computes **all** induced connected components. The script asserts the exact two exceptional partitions and their ordered component-size lists, verifies the 25-profile coverage count, and checks the isolated certificate above. It treats permutations as labelled, while the partition enumeration identifies only isomorphic graph types; relabeling preserves the conclusions.

**4. Independent acyclicity check and boundary.** A second, independent enumeration iterates all \(2^{|E(G)|}\) directed-edge assignments for \(K_{3,3,1}\), \(K_{3,2,2}\), and \(K_{2,2,2}\), and retains an assignment only if repeated source removal deletes every vertex (Kahn's DAG test). Its resulting sets are asserted equal to the topological-order sets before the component traversal. Thus both nontrivial exceptional types and the largest balanced three-partite case of order six have an independent source of orientation completeness. The lemma and script are exact finite certificates; no computation for \(n\ge8\), and no general extrapolation, is used.

**5. Complete output.** For the two exceptional types the source asserts `((3,3,1),[430,430])` and `((3,2,2),[1192]+[1]*48)` in the order shown. It explicitly confirms all 23 remaining profiles have one component. In particular \(K_{2,2,2}\) has 426 zonotope vertices and 288 simple vertices, all connected in the simple-induced subgraph. This exhausts all cases in the theorem.

## Verification
Run `python3 verify_multipartite_simple_connectivity.py` from the directory containing the included checker. It uses Python's standard library only, exact integer masks and sets, and no external graph or geometric packages. The recorded successful terminal sentinel is

`MULTIPARTITE_SIMPLE_STRATUM_PASS profiles=25 independent_direct_DAGs=3 exceptional_types=2 component_counts=(2,49) isolated_witness=1`.

The program prints the full 25-line census before the sentinel. Its assertions fail if any reported count, complete component list, independently enumerated DAG set, or isolated witness differs. Source code and the finite-exhaustion argument above together give the finite proof; a printed success message alone would not constitute proof. No claim about infinite families follows from this finite computation.

## Relationship to prior work
Chapoton--Pilaud (arXiv:2201.06896), Section 1.4 and Propositions 48--50, give the multipartite ordered-block model and vertex-count formula. The present theorem uses that existing combinatorial framework, but asks which *individual* vertices are simple and how those vertices are connected inside the zonotope skeleton; the cited propositions do not state the two exceptional component decompositions or a seven-vertex cutoff. Padrol--Pilaud--Poullot (arXiv:2111.12422) develops the general graphical-zonotope normal fan and deformations, but does not state such a cutoff.

Specific earlier degree-spectrum work for complete-bipartite graphical zonotopes shows that their simple vertices are pairwise nonadjacent, but that two-part statement is **outside** the theorem's three-part domain. A separate exact complete-split result proves that simple vertices remain connected for all part sizes of the form \((s,1,\ldots,1)\); neither exceptional partition has this form. The published octahedral \(K_{2,2,2}\) degree spectrum establishes 288 simple vertices, but not the connectedness of their induced subgraph. All these results are respected rather than subsumed by a spurious novelty claim.

## Limitations
The conclusion is an **exhaustive finite cutoff through order seven**, not an infinite-dimensional connectivity classification or an asymptotic assertion. Although the input graphs have at most seven vertices, their zonotopes can have thousands of vertices; exact exhaustive enumeration is a valid proof of this finite claim, not a proof of any extrapolation. Further equivalent descriptions under simplicial chambers of graphic arrangements could exist in unindexed literature, and no independent scholarly review has been performed. All counts are for the standard graph arrangement with all graph edges present between distinct parts, and not for arbitrary subgraphs or other geometric constructions.

## References
1. A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422 (first public version 2021-11-24), https://arxiv.org/abs/2111.12422; sections 1.3 and 2.
2. F. Chapoton, V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896 (first public version 2022-01-18), https://arxiv.org/abs/2201.06896; Section 1.4, Propositions 48--50.
3. *Degree spectrum and isolated simple vertices of complete-bipartite graphical zonotopes*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-degree-spectrum-and-isolated-simple-vertices-of-complete-biparti--57511bb89831 .
4. *Vertex-degree distribution and connected simple stratum of complete-split graphical zonotopes*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-vertex-degree-distribution-and-connected-simple-stratum-of-compl--22c11a50aaf3 .
5. *The missing degree seven in the octahedral graphical zonotope*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-missing-degree-seven-in-the-octahedral-graphical-zonotope--545b3ee69e57 .
