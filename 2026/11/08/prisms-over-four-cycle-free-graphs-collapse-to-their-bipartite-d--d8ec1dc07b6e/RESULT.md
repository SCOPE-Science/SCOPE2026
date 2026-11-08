# Prisms over four-cycle-free graphs collapse to their bipartite double covers

## Finding
For every finite nonempty simple graph \(H\) without a four-cycle, the ordinary open Lovász neighborhood complex of its Cartesian prism admits a canonical **simplicial graph spine**:
\[
\mathcal N(H\square K_2)\searrow D(H):=H\times K_2.
\]
Here \(\square\) is the Cartesian graph product, whereas \(\times\) denotes the categorical (Kronecker) product. The displayed arrow is an explicit finite sequence of elementary simplicial collapses, rather than only a homology equivalence. The spine is stable under the natural \(\operatorname{Aut}(H)\times C_2\) action, and the collapse pairs constitute an invariant acyclic matching; the resulting homotopy equivalence is equivariant under this action.

Writing \(d_H(v)\) for vertex degrees, the collapse has exactly
\[
P(H)=2\sum_{v\in V(H)}\bigl(2^{d_H(v)}-d_H(v)-1\bigr)
\]
free-face pairs. If \(H\) is connected with \(v\) vertices and \(e\) edges, its resulting integral homotopy type is
\[
\mathcal N(H\square K_2)\simeq
\begin{cases}
\displaystyle\bigvee^{2e-2v+1}S^1,&H\text{ nonbipartite},\\
\displaystyle\left(\bigvee^{e-v+1}S^1\right)\sqcup\left(\bigvee^{e-v+1}S^1\right),&H\text{ bipartite}.
\end{cases}
\]
A zero-fold wedge is a point. In particular, arbitrary connected four-cycle-free bases, including high-degree stars, trees with branching and graphs with many independent cycles, all yield graph-like neighborhood complexes of their prisms.

## Assumptions and scope
Let \(H=(V,E)\) be a finite nonempty undirected simple loopless graph, with no four pairwise distinct vertices forming a cyclic sequence of four graph edges. Triangles are allowed. Vertices of the prism \(P=H\square K_2\) are \(v_a=(v,a)\) for \(v\in V\) and \(a\in\{0,1\}\). Its edges are \(v_aw_a\) for \(vw\in E\) and the vertical edges \(v_0v_1\). The *open* neighborhood complex \(\mathcal N(P)\) has a nonempty face exactly when its vertices share an adjacent prism vertex; the empty face is included. All prism vertices occur since every one has a vertical neighbor.

The graph \(D(H)=H\times K_2\) uses the same vertex set and the cross-layer edges \(v_aw_{1-a}\) for every \(vw\in E\). It is viewed as a one-dimensional simplicial complex, including isolated vertices. The layers of \(D(H)\) are switched by the involution \(v_a\mapsto v_{1-a}\).

## Proof
**1. Unique neighborhood ownership.** Let \(A_v=N_H(v)\), and let \(W_{v,a}=\{w_a:w\in A_v\}\). The maximal generating simplex of \(\mathcal N(P)\) centered at \(v_a\) is
\[
F_{v,a}=W_{v,a}\cup\{v_{1-a}\}.
\]
Because \(H\) has no four-cycle, any two distinct vertices of \(H\) have at most one common neighbor. Thus every same-layer set \(B\subseteq W_{v,a}\) of cardinality at least two belongs to the generating simplex of exactly one *same-layer center*, namely \(v_a\). An opposite-layer center has only one neighbor in layer \(a\), so cannot contain \(B\) at all. Consequently every coface of \(B\) in the entire neighborhood complex lies in the single simplex \(F_{v,a}\). This uniqueness includes triangles in \(H\); no triangle-free assumption is required.

**2. A complete ordered list of free pairs.** For each \(v\in V\), each \(a\in\{0,1\}\), and every subset \(B\subseteq W_{v,a}\) with \(|B|\ge2\), pair the faces
\[
\bigl(B,\ B\cup\{v_{1-a}\}\bigr).
\]
List all such pairs in decreasing order of \(|B|\), resolving ties arbitrarily. No face participates twice: lower faces have vertices in only one layer and at least two vertices, so Step 1 gives their unique center; upper faces have at least two vertices in one layer and exactly one in the other, which uniquely identifies the apex. At the time a pair is processed, any possible coface of \(B\) other than \(B\cup\{v_{1-a}\}\) must have added one or more further vertices from \(W_{v,a}\); it has already been removed at a strictly larger value of \(|B|\). Its sole remaining immediate coface is therefore \(B\cup\{v_{1-a}\}\), and that coface is maximal. The pair is a legal elementary simplicial collapse. The statement also applies with \(d_H(v)\le1\), when that center supplies no pairs.

**3. Exact residue, count and natural symmetry.** After all pairs are removed, no face with two vertices in the same layer survives. Every cross-layer edge \(v_aw_{1-a}\) for \(vw\in E\) survives, since it has one vertex in each layer and cannot be in a pair. All vertices survive. There are no other surviving faces, so the residue is exactly the graph \(D(H)\). A degree-\(d_H(v)\) neighborhood contributes \(2^{d_H(v)}-d_H(v)-1\) subsets of size at least two per layer, proving the count \(P(H)\). Hence, counting the empty face, the original complex has exactly \(1+2|V|+2|E|+2P(H)\) faces.

Any graph automorphism of \(H\), acting in both layers, and the layer-switching involution send each indicated pair to another indicated pair of the same size. Such pairs at one size are disjoint and have no collapse dependencies within that size; they can be removed by symmetry-stable batches. Thus the associated strong deformation retract may be taken \(\operatorname{Aut}(H)\times C_2\)-equivariant. In particular, integral homology and its automorphism action agree with those of the explicit double-cover graph.

**4. Graph homotopy classification.** For connected bipartite \(H\), the bipartite double cover \(D(H)\) consists of two copies of \(H\). Each has cycle rank \(e-v+1\). For connected nonbipartite \(H\), odd cycles connect both sheets of \(D(H)\), giving one component with \(2v\) vertices and \(2e\) edges, hence cycle rank \(2e-2v+1\). Every connected graph has the homotopy type of a wedge of as many circles as its cycle rank. This yields the stated integral result, including vanishing higher integral homology and free fundamental groups in each component.

**5. A sharp excluded case.** When \(H=C_4\), its Cartesian prism is the cube \(Q_3\). The cube has four vertices in each bipartition class; the open neighborhoods of the four opposite vertices provide precisely the four triangular facets of a tetrahedral boundary on that class. Thus \(\mathcal N(Q_3)\cong\partial\Delta^3\sqcup\partial\Delta^3\simeq S^2\sqcup S^2\). By contrast \(D(C_4)\cong C_4\sqcup C_4\simeq S^1\sqcup S^1\). The four-cycle-free assumption cannot be dropped uniformly.

## Verification
The standalone standard-library Python program `verify.py` reconstructs the original neighborhood complex independently from all prism vertex neighborhoods, enumerates every proposed collapse pair, checks that its lower face has exactly one remaining immediate coface and its upper face is maximal, and checks equality with the claimed graph spine. It exhaustively tests all \(613\) labeled four-cycle-free simple graphs of orders one through five. Additional named examples include \(C_3\), \(C_5\), \(C_7\), the six-vertex star and the Petersen graph. The square-base negative control independently checks the face dimensions of the cube case. The recorded output is `verification_output.txt`. These finite tests corroborate, rather than replace, the universal proof in Steps 1–4.

## Relationship to prior work
Lovász's neighborhood complex and its relation to topological graph coloring are classical; Matoušek and Ziegler (first posted August 9, 2002) give a detailed early account. Kamibeppu (2008, Theorem 3) treats the box complex of a graph **itself** when that graph has no four-cycle; this gives related graph-spine behavior, but a prism over a base with adjacent edges always has overlapping four-cycles. Shukla (2018/2019, Theorem 2.1) shows that the neighborhood complex of a graph with maximum degree at most three has graph-like components, without the claimed all-degree prism-to-cover simplicial collapse. Matsushita (arXiv:1404.1549, Theorem 1.2) relates isomorphisms of *Kronecker double-cover graphs* to isomorphisms of neighborhood complexes, a different implication from the present Cartesian-prism collapse.

The published result *Graph-like neighborhood complexes with edge-disjoint four-cycles* gives a homotopy formula when **all four-cycles of the graph whose neighborhood complex is formed are pairwise edge-disjoint**. In a prism over any connected base with a vertex of degree at least two, the vertical rung through that vertex lies in multiple four-cycles, so that hypothesis fails. The published *Explicit graph spines for neighborhood complexes of square-free bipartite graphs* concerns the graph **without squares itself**, while the prism generally has many squares. The published *A high-girth prism Čech collapse and its integral symmetry modules* concerns a **closed-neighborhood Čech nerve**, rather than the ordinary open Lovász complex here. These distinct results motivate but do not imply the present natural spine theorem.

## Limitations
The theorem proves a simplicial collapse of the **ordinary open-neighborhood complex** of a prism, not the intrinsic Čech nerve or a Vietoris–Rips complex. The base graph must be finite, simple and four-cycle-free; the cube shows the obstruction is substantive. No classification is asserted for arbitrary bases containing four-cycles. The homotopy equivalence is not a simplicial isomorphism in general. Publication-priority assessment is relative to the literature examined, not a claim that all possible unindexed work has been excluded.

## References
1. J. Matoušek and G. M. Ziegler, *Topological lower bounds for the chromatic number: A hierarchy*, arXiv:math/0208072, first submitted 2002-08-09, https://arxiv.org/abs/math/0208072.
2. A. Kamibeppu, *Homotopy type of the box complexes of graphs without 4-cycles*, RIMS Kôkyûroku 1578 (2008), pp. 67–70, Theorem 3, https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1578-13.pdf.
3. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first submitted 2018-02-13, https://arxiv.org/abs/1802.04526.
4. T. Matsushita, *Neighborhood complexes and Kronecker double coverings*, arXiv:1404.1549, first submitted 2014-04-06; Osaka J. Math. 58 (2021), pp. 637–645, https://ir.library.osaka-u.ac.jp/repo/ouka/all/83203/ojm58_03_637.pdf.
5. *Graph-like neighborhood complexes with edge-disjoint four-cycles*, public mathematical record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-graph-like-neighborhood-complexes-with-edge-disjoint-four-cycles--d8f86495e49d.
6. *Explicit graph spines for neighborhood complexes of square-free bipartite graphs*, public mathematical record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-explicit-graph-spines-for-neighborhood-complexes-of-square-free--dd6b91667963.
7. *A high-girth prism Čech collapse and its integral symmetry modules*, public mathematical record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-high-girth-prism-ech-collapse-and-its-integral-symmetry-module--e4f536ceab68.
