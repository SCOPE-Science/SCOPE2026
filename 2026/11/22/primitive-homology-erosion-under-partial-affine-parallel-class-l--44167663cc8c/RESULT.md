# Primitive homology erosion under partial affine parallel-class line faults

## Finding

Let \(\mathcal A\) be any finite affine plane of order \(q\ge3\), and fix one of its parallel classes \(\mathcal C=\{\ell_1,\ldots,\ell_q\}\). For each integer \(0\le s\le q\), delete the first \(s\) **line vertices** of \(\mathcal C\), retain all points and all other lines, and recompute the unit-edge shortest-path metric of the remaining incidence graph \(G_s\). Write \(K_s=\operatorname{VR}_{\le2}(G_s)\) for the inclusive-radius-two vertex Vietoris–Rips complex and put \(b_s=(q-1)^2(q+1)-s(q-1)\). Then, integrally,

\[
K_s\simeq
\begin{cases}
\displaystyle\bigvee^{b_s}S^2\;\vee\;\bigvee^{(q-s-1)(q-1)^q}S^q,&0\le s<q,\\[3pt]
\displaystyle\bigvee^{b_q}S^2\;\vee\;\bigvee^{2(q-1)^q}S^{q-1},&s=q.
\end{cases}
\]

These are actual homotopy equivalences, not merely ranks over a field. All groups in positive degree are free abelian. There are natural simplicial inclusions \(K_q\subseteq K_{q-1}\subseteq\cdots\subseteq K_0\), despite the recomputation of distances.

For each \(0\le s<q\), the induced map on **degree-two** integral homology has primitive image and cokernel \(\mathbb Z^{q-1}\). For \(0\le s<q-1\), the degree-two map is a split injection; moreover the degree-\(q\) map is a split injection with cokernel \(\mathbb Z^{(q-1)^q}\), including the last zero-to-nonzero map when \(s=q-2\) (direction \(K_{s+1}\to K_s\)). At the final step \(K_q\hookrightarrow K_{q-1}\), the degree-two map is still injective for \(q\ge4\). For \(q=3\), it has kernel \(\mathbb Z^{16}\), image of rank \(10\), and primitive cokernel \(\mathbb Z^2\); the kernel consists precisely of the two new pure-shore homology summands. No claim that the final map is injective for \(q=3\) is made.

The end stages \(s=0\) and \(s=q\) were previously classified individually; the contribution here is the **entire intermediate erasure family, natural integral maps, and sharp exceptional endpoint**.

## Assumptions and scope

A finite affine plane of order \(q\) has \(q^2\) points, \(q(q+1)\) lines, and \(q+1\) parallel classes, each of \(q\) disjoint lines. Each point is on one line from each class; each line has \(q\) points; two distinct points determine exactly one line; two nonparallel lines meet in one point. The theorem assumes such a plane exists and does not assume coordinates, Desarguesian structure, or existence for an arbitrary integer. Here \(q\ge3\).

The graph distance is measured **after** each vertex deletion, using unit incidence edges. For a graph \(G\), a vertex set is a face of \(\operatorname{VR}_{\le2}(G)\) exactly when every pair has graph distance at most two. The filtration is contravariant in the number of deleted vertices: the natural maps are the inclusions \(K_{s+1}\hookrightarrow K_s\). Homology and primitive sublattices are over \(\mathbb Z\).

We use \(D_m\) for a discrete complex of \(m\) vertices, \(\Delta_m\) for a full simplex on \(m\) vertices, and \(*\) for simplicial join. A wedge of zero spheres is understood to be contractible.

## Proof

**1. Distance-two graph after deleting a partial parallel class.** Every surviving line vertex still has \(q\) neighboring points. Each point has either \(q\) or \(q+1\) surviving line neighbors. The incidence graph \(G_s\) is connected: a pair of points with retained joining line has a path of length two; if its joining line was deleted, choose two distinct retained line directions through the two points and use their intersection to construct a path of length four. Such directions are available because \(q\ge3\). Every surviving line is attached to a point, so the whole graph is connected.

Two distinct points are at distance two precisely when their joining line survives. Since the deleted lines are pairwise parallel, the *only* forbidden point pairs at scale two are pairs on the same one of those \(s\) erased lines. Two surviving lines are at distance two precisely when they are nonparallel; parallel distinct lines have no common point. Opposite-shore point–line distances have odd parity, so distance at most two is equivalent to incidence. This proves that a clique containing two points and two lines is impossible (such a clique would provide a four-cycle of the incidence graph).

**2. The two pure-shore clique complexes.** Let \(A_s\) and \(B_s\) be the induced scale-two clique complexes on points and lines respectively. For \(s<q\), the \(s\) erased lines partition \(sq\) points into groups of size \(q\), whose within-group edges are forbidden; the remaining \(q(q-s)\) points form a full simplex and join to every earlier group. Hence
\[
A_s\cong (D_q)^{*s}*\Delta_{q(q-s)},\qquad
B_s\cong D_{q-s}*(D_q)^{*q}.
\]
The first is contractible, while the second is an integral wedge of \((q-s-1)(q-1)^q\) spheres of dimension \(q\). When \(s=q\), both are \((D_q)^{*q}\), each a wedge of \((q-1)^q\) spheres of dimension \(q-1\). These assertions follow by repeatedly applying \(\widetilde H_0(D_m;\mathbb Z)\cong\mathbb Z^{m-1}\) and the join/suspension formula, or by choosing one point in each discrete factor as a basepoint. All \(A_s,B_s\) are simply connected for \(q\ge3\).

**3. A natural homotopy-pushout cover.** Define \(U_s\) to consist of \(A_s\) together with the simplex on \(\{\ell\}\cup P(\ell)\) for every retained line \(\ell\), where \(P(\ell)\) denotes its points. Define \(V_s\) to consist of \(B_s\) together with the simplex on \(\{p\}\cup L_s(p)\) for every point \(p\), where \(L_s(p)\) denotes its surviving incident lines. The no-four-cycle property implies
\[
K_s=U_s\cup V_s,\qquad U_s\cap V_s=G_s
\]
with the latter equality literally as subcomplexes (no common triangles). Each added mixed simplex in \(U_s\) has a unique line apex whose base is already in \(A_s\), and each added mixed simplex in \(V_s\) has a unique point apex whose base is already in \(B_s\). Deleting the apex by relative elementary collapses gives \(U_s\searrow A_s\) and \(V_s\searrow B_s\).

Because \(A_s\) and \(B_s\) are simply connected and \(G_s\) is a connected graph, both attaching maps \(G_s\to U_s,V_s\) are nullhomotopic. The inclusions of finite subcomplexes are cofibrations, so the homotopy pushout splits
\[
K_s\simeq A_s\vee B_s\vee\Sigma G_s.
\]
The graph has \(2q^2+q-s\) vertices and \(q^2(q+1)-sq\) edges, so its cycle rank is \(b_s\). Since \(\Sigma G_s\simeq\bigvee^{b_s}S^2\), substituting Step 2 establishes every stated integral homotopy type.

**4. Natural degree-two maps.** For \(s<q\), \(H_2(A_s)=H_2(B_s)=0\), since \(A_s\) is contractible and \(B_s\) has reduced homology only in degree \(q\ge3\). The Mayer–Vietoris connecting map for \(K_s=U_s\cup_{G_s}V_s\) thus gives a **natural isomorphism** \(H_2(K_s;\mathbb Z)\cong H_1(G_s;\mathbb Z)\). Its naturality identifies \(K_{s+1}\hookrightarrow K_s\) on this summand with graph-cycle inclusion.

For every \(s<q\), deleting \(\ell_{s+1}\) removes one vertex and its \(q\) incident edges. The graph-cycle group \(H_1(G_{s+1};\mathbb Z)\) sits in \(H_1(G_s;\mathbb Z)\) as cycles supported away from those \(q\) edges. The quotient injects into the free abelian coordinate group \(\mathbb Z^q\) on those edges, hence is torsion-free. Its rank is \(b_s-b_{s+1}=q-1\). The map is thus split-injective, with primitive image, as long as the two Mayer–Vietoris identifications apply, that is, for \(0\le s<q-1\).

At \(s=q\), if \(q\ge4\), both pure-shore homologies vanish in degree two, so the same natural isomorphism holds and the final degree-two map is also a primitive injection. If \(q=3\), the Mayer–Vietoris exact sequence instead gives
\[
0\to H_2(A_q)\oplus H_2(B_q)\to H_2(K_q)\to H_1(G_q)\to0.
\]
The first group has rank \(2(q-1)^q=16\). Under inclusion into \(K_{q-1}\), that entire first group maps to zero because its images factor through \(A_{q-1}\) and \(B_{q-1}\), which have vanishing degree-two homology. Naturality and injectivity of graph-cycle inclusion show there are no other kernel classes. The image is the primitive rank-\(b_q=10\) graph-cycle sublattice in \(H_2(K_{q-1})\cong\mathbb Z^{b_{q-1}=12}\), with cokernel \(\mathbb Z^2\). This proves the sharp exception.

**5. Primitive higher-dimensional maps.** For \(s<q\), degree-\(q\) Mayer–Vietoris gives \(H_q(K_s;\mathbb Z)\cong H_q(B_s;\mathbb Z)\): the graph is one-dimensional, and \(A_s\) is contractible. Put \(T=(D_q)^{*q}\). Then \(B_s=D_{q-s}*T\); for \(s<q-1\) the inclusion \(B_{s+1}\subset B_s\) removes one vertex from the discrete first factor. It induces the canonical primitive inclusion of augmentation lattices \(\widetilde H_0(D_{q-s-1};\mathbb Z)\subseteq\widetilde H_0(D_{q-s};\mathbb Z)\), tensored with \(\widetilde H_{q-1}(T;\mathbb Z)\cong\mathbb Z^{(q-1)^q}\). Its cokernel is \(\mathbb Z^{(q-1)^q}\). The natural Mayer–Vietoris comparison transfers this statement to \(K_{s+1}\hookrightarrow K_s\). For \(s=q-1\), the source \(B_{q-1}=D_1*T\) is contractible and the corresponding higher-degree source group is zero; no injectivity beyond what has just been stated is claimed.

These steps establish the complete theorem. \(\square\)

## Verification

The standalone, standard-library-only Python 3 program `verify_affine_line_fault.py` reconstructs affine incidence graphs over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\), deletes each possible prefix of one fixed parallel class, and recomputes all shortest-path distances. It verifies exact clique adjacency conditions and face inclusions, line/point/edge counts and cycle ranks. For every \(0\le s\le3\) at \(q=3\), it independently enumerates all Rips faces and computes simplicial homology over \(\mathbb F_2\), including the predicted ranks \((16,16),(14,8),(12,0),(26,0)\) in degrees \((2,3)\). Exact mod-two boundary reductions of the **actual inclusion maps** return degree-two image ranks \((14,12,10)\) for the three deletion steps and degree-three ranks \((8,0,0)\). For order four, all five metric and combinatorial stages are checked, but not their exponentially large boundary matrices. The order-two test is only a metric regression check, outside the theorem's stated range.

Run `python3 verify_affine_line_fault.py` and compare with `verification_output.txt`; successful verification ends in `VERIFY_OK`. These calculations do not prove the infinite-family assertion, the integral wedge decomposition or the primitive cokernels; those follow from Steps 1–5. No independent mathematical audit is claimed.

## Relationship to prior work

Adamaszek and Adams (arXiv:2103.01040, first public 2021-03-01) study radius-two Rips complexes of **hypercube** vertex metrics, not affine point–line incidence graphs. Feng and Nukala (arXiv:2302.14664, first public 2023-02-28) study scale-two subset-layer metrics. These sources motivate discrete-metric Rips homotopy classifications but do not entail affine line erasures.

The closest published incidence-graph calculations are *Affine-plane incidence Rips complexes have two sphere dimensions* (the exact \(s=0\) endpoint) and *Complete integral graph-metric Rips filtration after deleting an affine-plane parallel class* (the exact \(s=q\) endpoint). The corresponding full primary `RESULT.md` texts determine only those individual endpoint homotopy types; neither proves the partial-erasure \(1\le s\le q-1\) stages or their integral inclusion homomorphisms. The latter endpoint theorem explicitly deletes the **whole class**, not a partial class. Its graph has a changed point-side metric: a full parallel class becomes q forbidden point groups, whereas every earlier stage retains a nonempty cone of point vertices.

The related published projective-plane vertex-puncture theorem addresses projective rather than affine incidence geometry: there is no parallel class of disjoint lines, and its homology loss is confined to degree two. The present affine partial erasure has two varying homology degrees plus an exceptional final new lower-dimensional contribution. The distinction is mathematical, not merely different names or parameters. The same-source proofs and analogous square-graph results were searched for stronger covering implications; no coverage of these intermediate maps was identified. Unindexed equivalent statements remain possible.

## Limitations

The conclusion requires an existing finite affine plane of order \(q\ge3\), line deletions *within one* fixed parallel class, graph distances recomputed after each deletion, and inclusive radius two. It does not classify arbitrary line-deletion patterns, other Rips radii, weighted graphs, equivariant homotopy, or the existence of planes at unspecified orders. The complete endpoint sphere-wedge types are prior results; no originality is claimed for those endpoints, the general join formula, Mayer–Vietoris naturality or graph-cycle lattice facts. Finite mod-two tests do not independently establish torsion-freeness in all orders; the integral topological proof does. Literature searches are not proofs of bibliographic uniqueness.

## References

- M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040, v1 made public 2021-03-01. https://arxiv.org/abs/2103.01040
- Z. Feng and N. C. P. Nukala, *On Vietoris–Rips complexes of Finite Metric Spaces with Scale 2*, arXiv:2302.14664, v1 made public 2023-02-28. https://arxiv.org/abs/2302.14664
- *Affine-plane incidence Rips complexes have two sphere dimensions*, public full result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-affine-plane-incidence-rips-complexes-have-two-sphere-dimensions--3087baeea0a4/RESULT.md
- *Complete integral graph-metric Rips filtration after deleting an affine-plane parallel class*, public full result, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-complete-integral-graph-metric-rips-filtration-after-deleting-an--86bc27e5515f/RESULT.md
- *Primitive vertex-deletion stability for Vietoris–Rips complexes of finite projective-plane incidence graphs*, public full result, https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-primitive-vertex-deletion-stability-for-vietoris-rips-complexes--6fb5eec5366c/RESULT.md
