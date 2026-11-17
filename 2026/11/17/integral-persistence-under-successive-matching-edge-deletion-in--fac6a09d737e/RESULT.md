# Integral persistence under successive matching-edge deletion in bicliques

## Finding

Fix integers \(a,b\ge3\), write \(m=\min\{a,b\}\), and label the shores of \(K_{a,b}\) by \(A=\{a_1,\ldots,a_a\}\) and \(B=\{b_1,\ldots,b_b\}\). For \(0\le t\le m\), let \(G_t\) be obtained by deleting the first \(t\) disjoint edges \(a_i b_i\), and let \(X_t=\operatorname{Ind}_2(G_t)\) consist of all vertex sets inducing graph components of order at most two. There are natural inclusions \(X_0\subseteq X_1\subseteq\cdots\subseteq X_m\).

**Theorem (complete integral persistence and coherent bases).** All \(X_t\) are connected and their only nonzero reduced integral homology groups are in degrees one and two. The inclusion maps have the following simultaneous integral bases:

* At stage zero, \(\widetilde H_1(X_0;\mathbb Z)\) has a basis \(c_{ij}\) for all \((i,j)\ne(1,1)\), with \(1\le i\le a\), \(1\le j\le b\). At stage \(t\ge1\), its basis consists precisely of the surviving \(c_{ij}\) with \(i>t\) and \(j>t\). The map \(X_t\hookrightarrow X_{t+1}\) carries \(c_{ij}\) to the identically named class when both indices exceed \(t+1\), and to zero otherwise. In particular all degree-one maps are split surjections over \(\mathbb Z\).
* For \(t\ge3\), \(\widetilde H_2(X_t;\mathbb Z)\) has a basis \(z_{ij}\), where \(2\le i<j\le t\). Every map into the next stage sends each \(z_{ij}\) to the identically named basis class. All degree-two maps are split injections over \(\mathbb Z\). The group is zero for \(0\le t\le2\).

Consequently the **complete reduced barcode over every field**, with filtration parameter \(t=0,1,\ldots,m\) and last-stage classes extended indefinitely, consists of degree-one intervals
\[
[0,1)^{\,a+b-2},\qquad [0,k)^{\,a+b-2k+1}\quad (2\le k\le m),
\]
and degree-two intervals
\[
[t,\infty)^{\,t-2}\quad (3\le t\le m).
\]
No other reduced persistent homology occurs. Here an interval exponent denotes multiplicity, and an empty indicated index range contributes nothing. In particular all transient classes are in degree one, and all new degree-two classes survive.

## Assumptions and scope

Graphs are simple, finite, undirected, with the fixed labeled matching deleted in this order. Since the graphs are bipartite, the condition that induced components have size at most two is equivalent to every selected induced degree being at most one (the dissociation condition). Every homology group and map is over \(\mathbb Z\) unless otherwise indicated. A split map means a split homomorphism of underlying abelian groups; no equivariant splitting is asserted. The half-open interval convention records a class born at the left integer stage and absent at the right. All results hold for every \(a,b\ge3\), including the asymmetric endpoint \(m=\min\{a,b\}\).

## Proof

**1. A natural two-pole quotient.** The full shore simplices \(\Delta_A\) and \(\Delta_B\) are disjoint contractible subcomplexes of every \(X_t\). Collapsing each separately to a point (not identifying the two points) is a homotopy equivalence of CW complexes and is natural with respect to \(t\), because the two simplices and their inclusions remain fixed. A mixed selected face can have no more than two vertices in either shore. All mixed pairs \(\{a_i,b_j\}\) occur. A mixed triple is exactly \(\{a_i,a_j,b_i\}\) or \(\{a_i,b_i,b_j\}\) with \(i\le t\) and distinct labels; and a mixed tetrahedron is exactly \(\{a_i,a_j,b_i,b_j\}\) with \(1\le i<j\le t\). There are no higher mixed faces. This follows because a mixed face with three vertices in a shore forces the opposite vertex to have at least two neighbours, and in a two-by-two face every selected vertex must have the opposite selected same-index non-neighbour.

For every \(t\), define the following *square CW complex* \(Q_t\). Its vertices \(e_{ij}\) are indexed by all pairs \((i,j)\in[a]\times[b]\), independent of \(t\). For each \(k\le t\), add edges between \(e_{kk}\) and \(e_{kj}\) for all \(j\ne k\), and between \(e_{kk}\) and \(e_{ik}\) for all \(i\ne k\). For each \(1\le i<j\le t\), fill the four-edge loop \(e_{ii},e_{ij},e_{jj},e_{ji},e_{ii}\) with one square. Mixed edges, triangles, and tetrahedra in the two-pole quotient are, respectively, suspensions of the vertices, edges, and square cells just described. Thus there are compatible CW identifications
\[
X_t\simeq\Sigma Q_t,
\]
where \(\Sigma\) means the unreduced two-pole suspension. Crucially, these identifications can be chosen **simultaneously for all stages**, and the transition is exactly the unreduced suspension of the inclusion \(Q_t\hookrightarrow Q_{t+1}\); hence their induced integral homology maps agree up to the natural suspension isomorphism. This compatibility, not merely a stagewise homotopy classification, is the basis of the persistence result.

**2. Components and degree-one maps.** At \(t=0\), \(Q_0\) is a discrete set of \(ab\) vertices. At every \(t\ge1\), it has one connected component containing the diagonal \(e_{11}\) and every vertex \(e_{ij}\) with \(i\le t\) or \(j\le t\), while precisely the \((a-t)(b-t)\) vertices with \(i>t,j>t\) remain isolated. In fact each off-diagonal vertex with an index \(\le t\) is adjacent to a matched diagonal, and for any two matched indices \(i,j\), the path \(e_{ii},e_{ij},e_{jj}\) connects their diagonal vertices. These assertions include \(t=1\) and every endpoint.

The suspension isomorphism gives \(\widetilde H_1(X_t;\mathbb Z)\cong\widetilde H_0(Q_t;\mathbb Z)\). Taking \(e_{11}\) as the base component, the differences \([e_{ij}]-[e_{11}]\) are a basis for all nonbase components. At \(t=0\) these are precisely all pairs except \((1,1)\). At \(t\ge1\) they are exactly the labels with both indices greater than \(t\). A vertex never ceases to exist but joins the main component at the first stage when either index is matched. Therefore each difference survives with the same label or becomes zero, proving the split-surjection statement and the degree-one barcode. The drop from stage zero to one is \(ab-1-(a-1)(b-1)=a+b-2\). For \(2\le k\le m\) the drop from stage \(k-1\) to \(k\) is
\[
(a-k+1)(b-k+1)-(a-k)(b-k)=a+b-2k+1.
\]

**3. Primitive coherent two-dimensional cycles.** For \(t\ge1\), discard the isolated vertices and consider the connected component \(Q_t^0\). Every off-diagonal vertex whose other index is unmatched is a leaf and hence can be removed by elementary collapses. For each unordered matched pair \(\{i,j\}\), there are two length-two paths between \(e_{ii}\) and \(e_{jj}\), through \(e_{ij}\) and \(e_{ji}\), respectively; their union is the boundary of the unique filled square. Collapse each square across one of its two-edge routes (as two elementary free-face collapses), retaining the path through \(e_{ij}\) for \(i<j\). These operations use disjoint off-diagonal vertices and square interiors and leave a subdivision of the complete graph on the matched diagonal vertices. Thus \(Q_t^0\simeq K_t\) as a one-dimensional graph; in particular it has no homology in degree above one and
\[
H_1(Q_t;\mathbb Z)\cong\mathbb Z^{\binom{t-1}{2}}.
\]

For clarity, orient the retained path \(P_{ij}:e_{ii}\to e_{ij}\to e_{jj}\) for each \(i<j\), and let \(P_{ji}=-P_{ij}\). For every \(2\le i<j\le t\), the integral cycle \(P_{1i}+P_{ij}-P_{1j}\) gives a homology class \(\zeta_{ij}\). The classes \(\zeta_{ij}\) form the integral *fundamental-cycle basis* of the complete graph with reference spanning star based at vertex \(1\): each contains the unique non-star edge \(\{i,j\}\) with coefficient \(+1\). They therefore form a primitive \(\mathbb Z\)-basis, not just a rational or mod-two basis. When \(t\) increases, all these actual cellular cycles survive unchanged, and the newly available classes indexed by \(j=t+1\) for \(2\le i\le t\) extend them to the next integral basis. The natural suspension carries \(\zeta_{ij}\) to \(z_{ij}\in\widetilde H_2(X_t;\mathbb Z)\), proving split injectivity. Exactly \(t-2\) new degree-two classes appear at stage \(t\ge3\), and none can die later.

**4. Completion.** The square CW models are graphs up to homotopy together with isolated points, so their suspensions have no reduced homology above dimension two. All groups are free with the bases above. The suspensions are connected because every \(Q_t\) is nonempty. The exact inclusion-map forms determine the asserted barcodes over any field by scalar extension, with no possible integral torsion or hidden extension.

## Verification

The standalone `verify_persistence.py` enumerates the original graph-induced face condition for all \(3\le a\le b\le5\). It computes each face's first valid deletion stage, orders the full simplicial filtration, and performs a separate exact mod-two filtered-boundary reduction to obtain birth/death intervals. For all six parameter profiles (a total of \(477\) distinct faces in their final complexes), the computed intervals coincide with the theorem, including the simultaneous disappearing degree-one classes and the permanent degree-two births. The program's actual output is `verification_output.txt`. These finite-field calculations only corroborate the theorem; the full integral and unbounded-parameter statements follow from the natural CW and primitive-cycle proof.

## Relationship to prior work

Two existing, closely relevant published statements already determine **each stage's nonequivariant homotopy type** for the same partially matching-deleted complete bipartite graph. They establish the formula \(X_t\simeq\bigvee^{(a-t)(b-t)}S^1\vee\bigvee^{\binom{t-1}{2}}S^2\) when \(t\ge1\), with the undeleted boundary separately. Those static results are fully credited; no novelty is claimed for their homotopy ranks. Neither inspected theorem determines the **induced maps between different deletion stages**. One explicitly lists these maps as a limitation. Its stagewise decomposition is not, by itself, evidence of the integral persistence barcode: the inclusions must be identified and checked. The new theorem supplies a natural simultaneous quotient and primitive bases proving exactly those maps, all birth/death times, and split integral behaviour.

Sawant's 2026 work on vertex decomposability of higher independence complexes of trees motivates the broader study of these complexes but does not cover edge-deletion persistence in complete bipartite graphs. Carnero Bravo's forest filtration changes the induced forest-degree cutoff for a fixed graph, rather than sequentially deleting graph edges. The distinct filtration parameter prevents either result from implying these exact deletion-induced maps. No comprehensive priority or independent mathematical validation is asserted.

## Limitations

Only deletion of pairwise disjoint cross-edges of a single complete bipartite graph is covered. No equivariant splitting, nonmatching defect, higher \(r\)-independence analogue, or nonlinear graph-perturbation filtration is claimed. The staged homotopy types are already known; the claim of originality is restricted to the coherent maps and persistence. Although full texts of the two most directly comparable results were examined, an equivalent result under other terminology or in unindexed work remains possible. Finite mod-two checks cannot substitute for the integral proof, and independent audit has not been performed.

## References

1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, first public version 2026-05-24; https://arxiv.org/abs/2605.25150.
2. *Mixed-dimensional dissociation homotopy under partial matching deletion from \(K_{a,b}\)*, publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-mixed-dimensional-dissociation-homotopy-under-partial-matching-d--04d61268ad5a.
3. *Homotopy of second independence complexes after deleting a bipartite matching*, publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-homotopy-of-second-independence-complexes-after-deleting-a-bipar--223b7506ca23.
4. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, 2023; https://arxiv.org/abs/2307.13271.
