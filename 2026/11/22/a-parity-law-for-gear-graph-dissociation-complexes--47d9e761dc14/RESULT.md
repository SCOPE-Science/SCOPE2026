# A parity law for gear-graph dissociation complexes

## Finding
Let \(G_n\) be the gear graph on \(2n+1\) vertices, with \(n\geq3\). Its second-independence (dissociation, equivalently three-vertex-path-free) simplicial complex has the **integral homotopy type**
\[
\operatorname{Ind}_2(G_n)\simeq
\begin{cases}
S^{n-1},&n\text{ odd},\\
\displaystyle\bigvee^{3}S^{n-1},&n\text{ even}.
\end{cases}
\]
In particular, reduced integral homology is free and concentrated in degree \(n-1\), with rank one or three respectively. The result is a homotopy classification, not merely an Euler-characteristic or field-homology calculation.

## Assumptions and scope
For every integer \(n\ge3\), let indices belong to \(\mathbb Z/n\mathbb Z\) and let
\[
V(G_n)=\{h\}\sqcup\{u_i:i\in\mathbb Z/n\mathbb Z\}\sqcup\{w_i:i\in\mathbb Z/n\mathbb Z\},
\]
with edges \(\{h,u_i\}\), \(\{u_i,w_i\}\), and \(\{w_i,u_{i+1}\}\) for all indices \(i\). Thus \(G_n\) is the wheel with each rim edge subdivided exactly once; it is also the simplex graph of a cycle when \(n\ge4\). The complex \(K=\operatorname{Ind}_2(G_n)\) contains exactly those \(S\subseteq V(G_n)\) for which every connected component of the induced graph \(G_n[S]\) has at most two vertices, equivalently every selected vertex has at most one selected neighbor. The empty face is included in the combinatorial face poset.

## Proof
**1. Partition the face poset.** Let \(U=\{u_i\}\) and \(W=\{w_i\}\). The map \(\pi:S\mapsto S\cap (U\cup\{h\})\) is an order-preserving map from the augmented face poset to the Boolean lattice on \(U\cup\{h\}\). It suffices to put acyclic matchings on all nonempty fibers, by the patchwork theorem for acyclic poset matchings.

**2. Fibers containing the hub.** If \(h\in\pi(S)\), then \(\pi(S)\) contains at most one vertex from \(U\), since otherwise the hub would have two selected neighbors. If it contains no \(u_i\), the permitted \(w\)-sets form the full simplex on all \(n\) vertices of \(W\). If it contains one \(u_i\), the two vertices \(w_{i-1}\) and \(w_i\) are forbidden, and the remaining \(n-2\ge1\) vertices are freely selectable. Hence every hub fiber is a nonempty simplex and admits a complete acyclic matching by toggling a free \(w\)-vertex.

**3. Fibers without the hub.** Fix \(A\subseteq\mathbb Z/n\mathbb Z\) and require \(\pi(S)=\{u_i:i\in A\}\). A vertex \(w_i\) is forbidden precisely when both \(i\) and \(i+1\) belong to \(A\), because then \(w_i\) would have two selected neighbors. Among the remaining \(w\)-vertices, the **only** forbidden pairs are \(\{w_{i-1},w_i\}\) for indices \(i\in A\) with \(i-1,i+1\notin A\). Indeed, a selected \(u_i\) forbids simultaneously selecting its two incident \(w\)-vertices; when a neighboring \(u\)-vertex is selected one of those \(w\)-vertices was already forbidden. The surviving pair constraints are disjoint: distinct isolated selected indices have disjoint pairs of adjacent \(w\)-vertices. Consequently this entire fiber is canonically the independence complex of a disjoint union of \(t\) edges and \(r\) isolated vertices, for certain nonnegative integers \(t,r\) depending on \(A\).

If \(r>0\), toggle one isolated allowed \(w\)-vertex to match every face in the fiber. This matching is acyclic and has no critical face. Suppose now \(r=0\). If \(A=\mathbb Z/n\mathbb Z\), all the \(w_i\) are forbidden, so the fiber consists of the single face \(U\), which has \(n\) vertices.

Assume instead that \(A\) is a proper cyclic binary word. It cannot contain two consecutive unselected indices: such a \(00\) pair would make the intervening \(w_i\) both allowed and isolated. It cannot contain two consecutive selected indices either: take the boundary of a maximal nonempty run of at least two consecutive selected indices; the allowed \(w\)-vertex between the last selected index and its next unselected index is isolated, since its selected neighbor is not an isolated selected index. Thus the binary word must alternate \(0,1,0,1,\ldots\) cyclically. This occurs only for even \(n\), with exactly two possible words. Conversely, in either alternating word all \(n\) allowed \(w\)-vertices are partitioned into \(n/2\) disjoint forbidden pairs.

In an alternating fiber, match faces along a chosen endpoint of each forbidden pair, in sequence. For a single pair \(\{a,b\}\), the three allowed subsets are \(\varnothing,\{a\},\{b\}\); pair the first two and leave \(\{b\}\). Repeating on the disjoint pairs is an acyclic element matching and leaves exactly one face: the fixed alternating \(u\)-set together with one selected \(w\)-vertex from each pair. It has \(n/2+n/2=n\) vertices.

**4. Assemble and identify the homotopy type.** Each fiber matching is acyclic. Since \(\pi\) is order preserving, the union of all fiber matchings is acyclic by patchwork. Its critical faces are exactly the all-\(u\) face, and additionally the two alternating-fiber faces when \(n\) is even. Thus there are respectively one or three critical faces, **all of simplicial dimension \(n-1\)**. The empty face is matched to a singleton in the fiber \(\pi^{-1}(\varnothing)\). Dropping that augmented matching pair produces the standard unreduced acyclic matching with one critical vertex and the same top-dimensional critical faces; the empty face is not part of the ordinary nonempty face poset. By the discrete-Morse CW theorem, the complex is homotopy equivalent to a CW complex with one zero-cell and only the indicated \((n-1)\)-cells. Since \(n\ge3\), all attaching maps land in the point, giving the asserted wedges of spheres. All conclusions hold over \(\mathbb Z\).

## Verification
The standalone standard-library program `gear_verifier.py` independently constructs all admissible vertex subsets of \(G_n\) and the explicit fiber matching for every integer \(3\le n\le9\). For all seven cases it checks matching involutivity, incident-face conditions, every oriented Hasse incidence, and global acyclicity by exhaustive topological sorting. For \(3\le n\le7\) it additionally performs independent mod-two simplicial boundary reductions. Its exact expected output is in `expected_output.json`. Run `python3 gear_verifier.py` and compare its stdout byte-for-byte with `expected_output.json`. These finite tests corroborate, but are not substituted for, the all-parameter argument above.

## Relationship to prior work
The construction and motivation come from the recent study of higher-independence complexes, particularly Sawant's 2026 paper on trees. That paper proves vertex decomposability for all tree higher-independence complexes; the gear graphs are cyclic and are not trees. Deshpande and Singh classify higher-independence complexes of complete multipartite, fully whiskered, path, cycle, and perfect rooted-tree families; gear graphs, with a hub and subdivided rim, do not belong to those families for \(n\ge3\). The proof uses the established element-matching and patchwork principles, but its alternating-fiber classification is specific to gear graphs.

The ordinary graph independence polynomial of gear graphs and the homotopy of other wheel-related graph complexes do not determine their second-independence homotopy type. Public research-record searches for *gear graph*, *Jahangir*, *bipartite wheel*, *dissociation*, *three-path-free*, and *simplex graph of a cycle* found no theorem implying the classification stated here. An unindexed equivalent statement remains a priority risk; non-discovery in a search is not a mathematical uniqueness proof.

## Limitations
The statement is restricted to the second-independence complex, and to gear graphs with \(n\ge3\). It does not assert shellability, equivariant homotopy, any classification for larger independence thresholds, or a classification of all Jahangir graphs. No independent audit of the present proof has been performed. The source searches do not rule out undiscovered or unindexed prior equivalent work.

## References
- R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150 (first public version 2026-05-24), https://arxiv.org/abs/2605.25150.
- P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, https://arxiv.org/abs/2001.05448. In particular, the element-matching and patchwork statements appear as Proposition 2.10 and Theorem 2.11.
- F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, https://arxiv.org/abs/2106.10863.
- E. W. Weisstein, *Gear Graph*, MathWorld, https://mathworld.wolfram.com/GearGraph.html (graph-family nomenclature).
